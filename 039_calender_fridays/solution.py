"""
Problem #39: Extract Fridays from a Given Month
Date: 2026-09-04

This script uses Python's `calendar` module to list all Fridays in February 2026.
It demonstrates how to iterate over days of a month, group them into weeks,
and filter out specific weekdays.
"""

import calendar

cal = calendar.Calendar()

month_days = list(cal.itermonthdays(2026, 2))
weeks = []

for d in range(0,len(month_days),7):

   weeks.append(month_days[d:d+7])


print(weeks)
fridays = []

for week in weeks:
    if week[4] != 0:
        fridays.append(week[4])
        
print(fridays)
