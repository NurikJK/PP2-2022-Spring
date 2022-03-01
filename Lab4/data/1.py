from datetime import date,timedelta
today = date.today()
print("Today:",today)
print("Bedore 5 days date was:", today - timedelta(5))