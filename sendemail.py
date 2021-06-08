import smtplib
import os
from GetJobConfig import com_email,email_pass
s = smtplib.SMTP('smtp.gmail.com', 587)
def sendmail(TEXT,email,SUBJECT):
    #print("sorry we cant process your candidature")
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login(com_email,email_pass)
        message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
        s.sendmail(com_email, email, message)
    except Exception as e:
        print("Mail sending failed!",+e)
    finally:
        s.quit()