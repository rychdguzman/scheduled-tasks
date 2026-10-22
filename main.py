##################### Extra Hard Starting Project ######################
import smtplib
import random as rnd
import datetime as dt
import pandas as pd
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

def greeting_letter(name):
    letter_name = rnd.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
    with open(f'./letter_templates/{letter_name}', 'r') as file:
        letter = file.read()
        return letter.replace('[NAME]', name)

df = pd.read_csv('birthdays.csv')
birthday_list = df.to_dict('records')

date_today = dt.datetime.today()
day = date_today.day
month = date_today.month

birthday_celebrant = [bday_celebrant for bday_celebrant in birthday_list
                      if bday_celebrant['day'] == day and bday_celebrant['month'] == month]

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    for celebrant in birthday_celebrant:
        connection.sendmail(to_addrs=celebrant['email'], from_addr=EMAIL,
                            msg=f'Subject: Happiest Birthday! {celebrant["name"]} \n\n '
                                f'{greeting_letter(celebrant['name'])}')
