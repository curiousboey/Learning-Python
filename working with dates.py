import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())
print(datetime.datetime.now().month)

#formatting dates
now = datetime.datetime.now()
print(now)
print(now.strftime('%d/%m/%y %H:%M:%S'))