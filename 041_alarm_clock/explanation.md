# Problem 41: Alarm Clock with Tkinter

## Problem
Write a simple alarm clock application using Tkinter. The user should be able to set an alarm time (hour and minute). The application should display the current time and show a popup message when the alarm time is reached.

## My Solution

I built a Tkinter GUI with:
- A label showing the current time (updates every second).
- Entry fields for hour and minute.
- A "Set Alarm" button.
- A label showing the currently set alarm time.

When the alarm is set, the application compares the current time with the alarm time every second. When the current time reaches or exceeds the alarm time, a message box appears.