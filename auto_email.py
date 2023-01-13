# Learnings
## from yahoo
import smtplib


def send_mail(to_ad, massage,from_ad=YOUR_EMAIL_ID, password= YOUR_APP_PASSWORD):
    with smtplib.SMTP("smtp.gmail.com") as con:
        # securing
        con.starttls()
        # login
        con.login(user=from_ad, password=password)
        con.sendmail(from_addr=from_ad, to_addrs=to_ad, msg=massage)
        
        
def msg_format(from_p="", to="", body="",subject=""):
    msg = f"""From:{from_p} 
        Subject: {subject} 


        {body} 
        """
    return msg


