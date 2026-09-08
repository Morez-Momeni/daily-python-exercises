"""
Problem #44: Login Form with Tkinter
Date: 2026-09-09

A simple login form built with Tkinter.
Users enter a username and password; credentials are checked against a predefined list.
The current time is displayed at the top, and a status label shows login result.
"""

# modules and global var
import tkinter as tk
from datetime import datetime

current_time = ""
users = [
    ("Ali",1234),
    ("Morez",1234)
]

# make instance from tk 
window = tk.Tk()

window.title("Login")

# window size
window.geometry("500x300")

# time
def clock():
    global current_time
    current_time = datetime.now()
    time_lable.configure(text=current_time.strftime("%H:%M:%S"))
    window.after(1000,clock)

time_lable = tk.Label(window,foreground="black",font="times 15 bold")
time_lable.pack()



# username lable & input
user_name_lable = tk.Label(window,text="username",foreground="green",font="times 25 bold").pack()
user_name = tk.Entry(window)
user_name.pack()

# password lable & input
user_password_lable = tk.Label(window,text="password",foreground="red",font="times 25 bold").pack()
user_password = tk.Entry(window)
user_password.pack()

# login
def login():
    username = user_name.get()
    password = user_password.get()
    for user in users:
        if username == user[0] and password == str(user[1]):
            print("Login successful")
            status_lable.configure(text="Logged In!", foreground="green")
            status_lable.pack()
            window.after(2000,window.destroy)
            
            return True

    print("Login failed")
    status_lable.configure(text="Failed!", foreground="red")
    status_lable.pack()
    return False

login_button = tk.Button(window,text="Login",command=login).pack()   # type: ignore
status_lable = tk.Label(window, foreground="green")


#run

clock()
window.mainloop()