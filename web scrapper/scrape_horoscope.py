import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TIMEOUT = 30
FAULT = "�"

def get_horoscope():
    url = "https://collective.world/"+ get_date()+ "/#capricorn"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_horoscope = soup.find_all('p')
    # for index,horoscope in enumerate(all_horoscope):
    #     print(f"Index: {index},Text: {horoscope}")
    return all_horoscope[13].text.replace(FAULT, " ")

def get_date():
    current_date = datetime.now()
    day_name = current_date.strftime("%A").lower()
    day = current_date.day
    month = current_date.strftime("%B").lower()
    year = current_date. year
    return (f'horoscope-for-today-{day_name}-{month}-{day}-{year}')

# with smtplib.SMTP("smtp.gmail.com", 587, timeout=TIMEOUT) as connection:
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     connection.sendmail(from_addr="MY_EMAIL",
#                         to_addrs="...",
#                         msg=f"Subject:Have a good day Best Wishes \n"
#                             f"Capricorn: Horoscope \n"
#                             f"{get_horoscope().encode('utf-8').replace()}")

print(get_horoscope())
