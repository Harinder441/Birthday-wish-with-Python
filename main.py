# birthday dictionarry can be made
# date and moth can be conv to tuple
from auto_email import send_mail
import pandas as pd
import datetime as dt
import random as rd
from letter_format import msg_format

datetime = dt.datetime
current = datetime.now()

email_data = pd.read_csv("birthdays.csv")
# person=email_data.sample()
# print(person['email'].item())
# print(email_data)

for (index, person_bday) in email_data.iterrows():
    # print(person_bday)
    # print(person_bday['name'])
    if person_bday.day == current.day and person_bday.month == current.month:
        letter_no = rd.randint(1, 3)
        with open(f"letter_templates/letter_{letter_no}.txt") as letter:
            msg_body = letter.read()
            msg_body = msg_body.replace("[NAME]", person_bday['name'])
        msg_sub = "Happy Birthday!"
        msg_from = "Harinder Singh"
        msg = msg_format(from_p=msg_from, subject=msg_sub, body=msg_body)
        send_mail(to_ad=person_bday.email, massage=msg)

# print(is_birthday())
