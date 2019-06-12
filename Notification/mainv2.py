import db, os, csv
from configparser import ConfigParser
from mailNotify import Mail
from tabulate import tabulate
from queryManager import Query

if __name__ == "__main__":
    curPath = os.path.dirname(os.path.realpath(__file__))
    tests, testsExp = [], []
    testDict, testExpDict = {}, {}
    mails = {}
    # read config file
    conf = ConfigParser()
    conf.read(curPath+"/config.ini")

    # open tests to be notified file
    with open(curPath+"/tests.csv",'r') as f:
        testFile = csv.reader(f)        # email, aliasname, expected running time
        for test in testFile: 
            if test[2]:         #has expected running time
                testsExp.append("'"+test[1]+"'")
                testExpDict[test[1]] = {"email":test[0]}
            else:
                tests.append("'"+test[1]+"'")    # format sql to filter on aliasname ???????????????????
                testDict[test[1]] = {"email":test[0]}   # create dictionary to get information related to this test quickly

    queryAliasExp = ','.join(testsExp)
    queryExp = Query.genQuery(queryAliasExp)

    queryAlias = ','.join(tests)
    query = Query.genQuery(queryAlias)

    # connect DB and get all missed tests
    ms = db.MSSQL(host=conf.get('db','host'),user=conf.get('db','user'),
    pwd=conf.get('db','pwd'),db=conf.get('db','db'))
    result = ms.ExecQuery(query,True)

    for i, r in enumerate(result):
        if i == 0: header = r   # first row is column header
        else:
            email = testDict[r[header.index('AliasName')]]["email"]
            if email in mails:
                mails[email].append(r)
            else:
                mails[email] = [r]

    print(mails)

    # html = Mail.formatEmail(result)
    # print(html)
    # for i in result:
    #     print(i)

    # send email
    # mail = Mail(conf.get('email','sender'),conf.get('email','receivers'),conf.get('email','server'))
    # mail.createMessage(conf.get('email','subject'), html)
    # mail.sendMail()