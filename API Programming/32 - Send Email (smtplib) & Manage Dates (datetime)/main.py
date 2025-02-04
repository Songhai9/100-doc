##################### Extra Hard Starting Project ######################
import smtplib
import random
import datetime as dt
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
my_email=os.getenv('MY_EMAIL')
my_password=os.getenv('MY_PASSWORD')
# 1. Update the birthdays.csv and get the current date
data = pd.read_csv('birthdays.csv')
current_date = dt.datetime.now()
# 2. Check if today matches a birthday in the birthdays.csv
for row in data.itertuples():
    if (int(row.month), int(row.day)) == (current_date.month, current_date.day):
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        random_letter_num = random.randint(1, 3)
        with open(f'letter_templates/letter_{random_letter_num}.txt') as file:
            letter = file.read()
            letter = letter.replace('[NAME]', row.name)
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(
                user=my_email,
                password=my_password
            )
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row.email,
                msg=f'Subject:Happy Birthday\n\n{letter}'
            )




