from datetime import date

d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)

days = (d2 - d1).days
print("Number of days:", days)
