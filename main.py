# birthday dictionarry can be made
# date and moth can be conv to tuple
from auto_email import send_mail, msg_format
import pandas as pd
import datetime as dt
import random as rd

datetime = dt.datetime
current = datetime.now()

email_data = pd.read_csv("birthdays.csv")


for (index, person_bday) in email_data.iterrows():
     #checking if the today is birthday of anyone from list
    if person_bday.day == current.day and person_bday.month == current.month:
        #choosing a random letter format
        letter_no = rd.randint(1, 3)
        with open(f"letter_templates/letter_{letter_no}.txt") as letter:
            msg_body = letter.read()
            
            msg_body = msg_body.replace("[NAME]", person_bday['name'])
        msg_sub = "Happy Birthday!"
        msg_from = YOUR_NAME
        #formating the massage
        msg = msg_format(from_p=msg_from, subject=msg_sub, body=msg_body)
        #finaly sending Email
        send_mail(to_ad=person_bday.email, massage=msg)


