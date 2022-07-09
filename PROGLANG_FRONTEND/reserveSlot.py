import tkinter as tk
from tkinter import ttk

#window elements
reserveSlotWindow = tk.Tk() #instance of tk that creates window
reserveSlotWindow.title("PE Reservation System | Reserve Slot")
reserveSlotWindow.geometry('600x600')
reserveSlotWindow.resizable(False,False)

#widgets
icon = tk.PhotoImage(file='./icons/fill-out.png')
icon_display = ttk.Label(
    reserveSlotWindow,
    image = icon,
    compound = 'image'
)
icon_display.pack(ipady=50)

reserveSlotLabel = ttk.Label(
    reserveSlotWindow,
    text = "Fill out the following:",
    font = ("Arial", 16)
)
reserveSlotLabel.pack()

detailsFrame = ttk.Frame(reserveSlotWindow)
detailsFrame.pack(padx=50, fill='x', expand=True)

nameLabel = ttk.Label(detailsFrame,text = "Name: ")
nameLabel.pack(pady = 5,fill='x', expand=True)
nameEntry = ttk.Entry(
    detailsFrame,
)
nameEntry.pack(ipady = 5, fill='x', expand=True)

studentNoLabel = ttk.Label(detailsFrame,text = "Student Number: ")
studentNoLabel.pack(pady = 5,fill='x', expand=True)
studentNoEntry = ttk.Entry(
    detailsFrame
)
studentNoEntry.pack(ipady = 5, fill='x', expand=True)

TimeLabel = ttk.Label(detailsFrame,text = "Time: ")
TimeLabel.pack(pady = 5,fill='x', expand=True)
TimeEntry = ttk.Entry(
    detailsFrame
)
TimeEntry.pack(ipady = 5, fill='x', expand=True)

def submitButton():
    pass

submitButton = ttk.Button(
    detailsFrame,
    text = "Submit",
    command = submitButton
)
submitButton.pack(pady = 30, ipady=5, fill='x', expand=True)

reserveSlotWindow.mainloop()
