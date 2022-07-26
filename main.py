import random
import pandas
import datetime as dt
import smtplib
import os

GMAIL_SMTP = "smtp.gmail.com:587"
MY_GMAIL_EMAIL = os.environ["GMAIL_EMAIL"]
MY_GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

# TODO 1 Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays = {(index, row.month, row.day):row for (index, row) in data.iterrows()}

now = dt.datetime.now()
actual_day = (now.month, now.day)

for (key, value) in birthdays.items():
    if actual_day == (key[1], key[2]):
        bd_name = value["name"]
        bd_email = value["email"]
    # TODO 2 If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            def_letter = letter.read()
            named_letter = def_letter.replace("[NAME]", bd_name)
    # TODO 3 Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(GMAIL_SMTP) as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL_EMAIL, password=MY_GMAIL_APP_PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL_EMAIL,
                to_addrs=bd_email,
                msg=f"subject:FELIZ ANIVERSÁRIO! 🎉🎂\n\n{named_letter}".encode('utf-8')
            )
        print("Email sent")