from datetime import datetime
current_date = datetime.now()
# print(current_date)


from datetime import datetime
yr = current_date.year
mth = current_date.month
day = current_date.day
hr = current_date.hour
min = current_date.minute
print(yr)
print(mth, day, hr, min)


formatted_date = current_date.strftime("%Y/%M/%d %H:%M:%S")
print(formatted_date)