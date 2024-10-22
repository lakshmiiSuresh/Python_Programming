# pop3 protocol
# imap
# smtp - simple mail transfer protocol
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('laksqqq2002@gmail.com',"shnj qybf knoh rwhi")
msg = "hello how are you"
s.sendmail("laksqqq2002@gmail.com","lakshmisuresh012@gmail.com",msg)
s.quit()
