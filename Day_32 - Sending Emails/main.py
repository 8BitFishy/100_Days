import smtplib
import datetime as dt
import random
import pandas as pd
import time
import os


def get_date():
    now = dt.datetime.now()
    todays_date = [(now.strftime('%d')), (now.strftime('%m'))]
    return todays_date

def read_birthday_data():
    birthday_data = pd.read_csv("birthdays.csv")
    return birthday_data


def check_birthdays(birthday_data, todays_date):
    email_list = []
    for row in birthday_data.iterrows():
        try:
            birthday_info = row[1].Birthday.split("/")
            birth_date = [birthday_info[0], birthday_info[1]]
            if birth_date == todays_date:
                email_list.append(row[1])
        except Exception as e:
            print(e)
    return email_list


def Generate_Email(recipient):

    #print(recipient.Name)
    message = Generate_Message(recipient.Name.title())
    subject = f"Happy Birthday {recipient.Name.title()}!"
    recipient = recipient.Email
    send_email(recipient, subject, message)
    return


def Generate_Message(recipient):
    letter_folder = "letters"
    message = ""
    for files in os.walk(letter_folder):
        filelist = list(files[2])
        with open(os.path.join(letter_folder, random.choice(filelist)), 'r') as letter:
            message = letter.read()
            message = message.replace("[NAME]", recipient)
        message = message + "\n\n\n" + get_quote()
        return message




def get_quote():
    with open("quotes.txt", 'r') as file:
        lines = file.readlines()
        quote = random.choice(lines)
        return quote



def send_email(recipient, subject, message):
    send_email = "4utomationtest@gmail.com"
    password = "V3Png7h#By7#f9QcD5z"

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=send_email, password=password)
            connection.sendmail(from_addr=send_email, to_addrs=recipient, msg=f"Subject:{subject}\n\n{message}")
            print(f"\nSending Email\nFrom: {send_email}\nTo: {recipient}\nSubject: {subject}\nMessage: {message}\n"
                  f"___________________________________\n")
    except Exception as e:
        print("Sending failed.")
    return





def start_loop():
    while True:
        todays_date = get_date()
        birthday_data = read_birthday_data()
        email_list = check_birthdays(birthday_data, todays_date)
        for item in email_list:
            Generate_Email(item)
        print("Sleeping...")
        time.sleep(60*60*24)


if __name__ == '__main__':
    start_loop()




'''

now = dt.datetime.now()

if now.weekday() == 4:
    quote = get_quote()
    #send_email(quote)

date_of_birth = dt.datetime(year=1992, month=12, day=22, hour=20)
print(date_of_birth)

'''