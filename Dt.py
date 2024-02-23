'''import datetime

print(datetime.datetime.now())'''

from datetime import datetime , timedelta
#print(datetime.now())
day = timedelta(days=1)
current_time = datetime.now()
print(current_time)
print(current_time - day)

