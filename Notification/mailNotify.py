import smtplib,email
from email.mime.text import MIMEText
from email.header import Header
from tabulate import tabulate

class Mail:
    def __init__(self,sender,receivers,server):
        self.sender = sender
        self.receivers = receivers
        self.server = server
        self.message = email.message.Message()
    
    def createMessage(self,subject,body):
        self.message = MIMEText(body, 'html', 'utf-8')
        self.message['Subject'] = Header(subject)

    def sendMail(self):
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(self.server, 25)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("Send to: " + str(self.receivers) + " successfully")
        except smtplib.SMTPException:
            print("Error during send mail to: " + str(self.receivers) )
    
    def formatEmail(data):
        """ 
        :type data: List[tuple]
        rtype: str
        format email body
        """
        html = """
            <html>
            <head>
            <style> 
            body {{font-family: Calibri; font-size: 14px;}}
            table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
            th, td {{ padding: 5px; }}
            </style>
            </head>
            <body><p>Below tests have issue, please check:</p>
            {table}
            </body></html>
            """
        html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))
        return html