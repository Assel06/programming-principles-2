import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday.strftime("%A"))
print(today.strftime("%a"))
print(tomorrow.strftime("%A"))