from datetime import datetime,time

def difference(day1,day2):
    timedelta = day1 - day2
    return timedelta.days * 24 * 3600 + timedelta.seconds
day1 = datetime.now()
day2 = datetime.strptime('2021-04-17 10:10:10','%Y-%m-%d %H:%M:%S')
print(difference(day1, day2))