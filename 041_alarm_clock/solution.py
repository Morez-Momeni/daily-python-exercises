"""
Problem #41: Alarm Clock with Tkinter
Date: 2026-09-07

A simple alarm clock application built with Tkinter.
The user can set an alarm time (hour and minute), and a popup appears when the alarm goes off.
"""

import tkinter as tk
from datetime import datetime
from tkinter import messagebox

alarm_time = None

window = tk.Tk()
window.title("alarm clock app".title())
window.resizable(width=False, height=False)
window.geometry("550x400")


def get_current_time():
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime("%H:%M:%S"))
    window.after(1000, get_current_time)
    comare_alarm_with_current_time(current_time)


def set_alarm():
    global alarm_time
    current_time = datetime.now()
    alarm_time = current_time.replace(
        hour=int(hour_alarm_entry.get()),
        minute=int(minute_alarm_entry.get()),
        second=0,
        microsecond=0
    )
    latest_alarm_lable.configure(text=alarm_time.strftime("%H:%M:%S"))


def comare_alarm_with_current_time(current_time):
    global alarm_time
    if alarm_time is not None and current_time >= alarm_time:
        messagebox.showinfo("showinfo", "Your alarm has gone off")
        latest_alarm_lable.configure(text="no alarm has been set".title())
        alarm_time = None


time_label = tk.Label(window, text="Hour")
time_label.pack()

tk.Label(window, text="Hour").pack()
hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()

tk.Label(window, text="Minute").pack()
minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()

tk.Button(window, text="Set Alarm", command=set_alarm).pack()
latest_alarm_lable = tk.Label(window, text="no alarm has been set".title())
latest_alarm_lable.pack()

get_current_time()
window.mainloop()