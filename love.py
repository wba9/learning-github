import datetime

start = datetime.date(2025, 4, 16)
today = datetime.date.today()

love = (today - start).days

print(f'Your relationship is {love} days old')

