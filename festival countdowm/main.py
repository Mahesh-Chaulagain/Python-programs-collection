import datetime

today = datetime.date.today()
makar_sankranti = datetime.date(today.year, 1, 14)
days_left = (makar_sankranti - today).days

if days_left > 0:
    print(f"Makar Sankranti is in {days_left} days!")
else:
    print("It's Makar Sankranti today!")