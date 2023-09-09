import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

sender = 'Sushant.Singh@harman.com'
reciver = 'sushantsinghruhil@gmail.com'
password = 'xxxxxxxxxxxxxx'

message=MIMEMultipart()
message['From']=sender
message['To']=reciver
message['Subject']="This is a test email"
body="""
<h1>Hi there</h1>
This is a test email
"""

mimetext=MIMEText(body,'plain')
message.attach(mimetext)

attachment_path="Email_attachment.txt"
attachment_file= open(attachment_path,'rb')
payload = MIMEBase('application','octate-stream')
payload.set_payload(attachment_file.read())
payload.add_header('Content-Disposition','attachement',filename=attachment_path)
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password=password)
message_text=message.as_string()
print(message_text)
server.sendmail(sender,reciver,message_text)
server.quit()