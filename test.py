import datetime
from dateutil.relativedelta import relativedelta
month = datetime.datetime.now().month-6
time = datetime.date.today()-relativedelta(month=month)
print(time)
print(str(time)[8:10])