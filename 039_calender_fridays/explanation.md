# Problem 39: Extract Fridays from a Given Month

## Problem
Write a script that extracts and prints all Fridays in a specific month (e.g., February 2026) using Python's `calendar` module.

## My Solution

I used the `calendar.Calendar().itermonthdays()` method to generate a list of day numbers for the given month, including zeros for days outside the month (to complete the weeks). Then I grouped the list into weeks of 7 days and extracted the 5th element (index 4) of each week, which corresponds to Friday (since Monday is index 0). I then filtered out any zeros (which would indicate that the Friday falls outside the month).