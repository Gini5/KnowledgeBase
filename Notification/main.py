import db, os, csv, argparse
from configparser import ConfigParser
from mailNotify import Mail
from queryManager import Query

parser = argparse.ArgumentParser(
    description='Notification for missed SLA tests')
parser.add_argument("--test", default=False)
args = parser.parse_args()

if __name__ == "__main__":
    curPath = os.path.dirname(os.path.realpath(__file__))
    tests = []
    testDict = {}
    mails = {}
    if args.test: objQuery = Query(-600)
    else: objQuery = Query()
    # read config file
    conf = ConfigParser()
    conf.read(curPath+"/config.ini")

    # open tests to be notified file
    with open(curPath+"/tests.csv",'r') as f:
        testFile = csv.reader(f)        # email, aliasname, expected running time
        for test in testFile: 
            tests.append("'"+test[1]+"'")    # format sql to filter on aliasname ???????????????????
            testDict[test[1]] = {"email":test[0]}   # create dictionary to get information related to this test quickly

    queryAlias = ','.join(tests)
    query = objQuery.genQuery(queryAlias)
    # print(query)

    # connect DB and get all missed tests
    ms = db.MSSQL(host=conf.get('db','host'),user=conf.get('db','user'),
    pwd=conf.get('db','pwd'),db=conf.get('db','db'))
    result = ms.ExecQuery(query,True)

    for i, r in enumerate(result):
        if i == 0: header = r   # first row is column header
        else:
            if r:
                email = testDict[r[header.index('AliasName')]]["email"]
                if email in mails:
                    mails[email].append(r)
                else:
                    mails[email] = [header,r]
    
    for rec, tests in mails.items():
        html = Mail.formatEmail(tests)

        # send email
        receiver = [conf.get('email','receivers')]
        if not args.test: receiver.append(rec)
        mail = Mail(conf.get('email','sender'),receiver,conf.get('email','server'))
        mail.createMessage(conf.get('email','subject'), html)
        # print("receiver:"+str(receiver))
        # print("email:"+html)
        mail.sendMail()