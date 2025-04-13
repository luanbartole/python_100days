import pandas
import random
import smtplib
import datetime as dt

# Read birthdays and get today's date
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

current = dt.datetime.now()

# Email credentials (hide in production)
user_email = "email@gmail.com"
user_password = "password"


def birthday_letter(name: str, email: str):
    """
    Generates and sends a personalized birthday email to a person.

    Args:
        name (str): The name of the birthday person.
        email (str): The email address of the birthday person.
    """
    letter_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter_number}.txt") as birthday_template:
        custom_letter = birthday_template.readlines()
        custom_letter[0] = custom_letter[0].replace("[NAME]", name)
        final_letter = "".join(custom_letter)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user_email, user_password)
        connection.sendmail(
            from_addr=user_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday {name} \n\n{final_letter}"
        )


# Check if today is someone's birthday and send email
for person in data_dict:
    if current.day == person["day"] and current.month == person["month"]:
        birthday_letter(name=person["name"], email=person["email"])
