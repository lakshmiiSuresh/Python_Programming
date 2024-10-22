# Python code to illustrate sending mail with attachments from your Gmail account 
# multipurpose internet mail extensions.
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

# MIMEMultipart is a class used to create a message object that 
# can have multiple parts (e.g body , attachmnts) in MIME format
# It allows you to create a message with plaintext and HTML content,
# as well as attach files.

# MIMEText is a class used to create a MIME message object that represents plain text.
# It is typicallu used to set the body content of the email message.

# MIMEBase is a class used to create a MIME message object that represents  
# genetic binary attachment.
# it is used when you want to attach files (eg: images,documents) to the email message

from email import encoders
fromaddr = "laksqqq2002@gmail.com"#"sender mail id"
toaddr = ["lakshmisuresh012@gmail.com","akshaysuresh0504@gmail.com"]#"receiver mail id"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = 'laksqqq2002@gmail.com'

# storing the receivers emailaddress
msg['To'] = 'lakshmisuresh012@gmail.com'

#storing subject
msg['subject'] = "python"

# string to store the body of the email
# body = "Welcome to the world of python 😊"

body = """ 
<html>
<head></head>
<body>
<h1><i>welcome to python mail programming</i></h1>
</body>
</html>"""

# msg.attach(MIMEText(body,'plain')) #convert to plain text and attach
msg.attach(MIMEText(body,'html'))

filename = "abcc.txt"
attachment = open(filename,"rb")

p = MIMEBase('application','octetstream')
# application is used to indicate it is a file
# octet stream to indicate it is binary

p.set_payload((attachment).read()) # read to read full content
# file ano image ano text ano enn nokkm  - set_payload

encoders.encode_base64(p) #convert to text .earlier it was binary

p.add_header('Content-Disposition',"attachment; filename=%s" % filename)

msg.attach(p)

s = smtplib.SMTP('smtp.gmail.com',587)
# start TLS for security
s.starttls()

# authentication
s.login(fromaddr,"shnj qybf knoh rwhi")

text = msg.as_string()#to convert to string

s.sendmail(fromaddr,toaddr,text)

s.quit()
