import yagmail

sender = 'sushantsinghruhil@gmail.com'
reciver = 'rampurramya@gmail.com'

subject= 'This is a test Email'

contents = ["""
Hi,
I sent this email using python.
text me when you recive it.
 
Sushant Singh
""",'Email_attachment.txt']

yag = yagmail.SMTP(user=sender,password="")
yag.send(to=reciver,subject=subject,contents=contents)
print("Email Sent")
