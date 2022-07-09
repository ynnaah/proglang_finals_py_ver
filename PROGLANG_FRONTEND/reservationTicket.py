from cgitb import text
import tkinter as tk
from tkinter import Label, ttk


#window elements
reservationDetailsWindow = tk.Tk() #instance of tk that creates window
reservationDetailsWindow.title("PE Reservation System | Reservation Ticket Details ")
reservationDetailsWindow.geometry('600x600')
reservationDetailsWindow.resizable(False,False)

#widgets
icon = tk.PhotoImage(file='./icons/tickets.png')
icon_display = ttk.Label(
    reservationDetailsWindow,
    image = icon,
    compound = 'image'
)
icon_display.pack(ipady=30)

reservationDetailLabel = ttk.Label(
    reservationDetailsWindow,
    text = "Reservation Ticket Details",
    font = ("Arial", 16)
)
reservationDetailLabel.pack()


detailsFrame = ttk.Frame(reservationDetailsWindow)
detailsFrame.pack(padx=50, pady=5, fill='x', expand=True)


ticketNoLabel = ttk.Label(detailsFrame,text = "Ticket Number: ")
ticketNoLabel.pack(pady = 5, fill='x', expand=True)
ticketNoEntry = ttk.Entry(
    detailsFrame,
    state = "disabled"
)
ticketNoEntry.pack(ipady = 5, fill='x', expand=True)

nameLabel = ttk.Label(detailsFrame,text = "Name: ")
nameLabel.pack(pady = 5,fill='x', expand=True)
nameEntry = ttk.Entry(
    detailsFrame,
    state = "disabled"
)
nameEntry.pack(ipady = 5, fill='x', expand=True)

studentNoLabel = ttk.Label(detailsFrame,text = "Student Number: ")
studentNoLabel.pack(pady = 5,fill='x', expand=True)
studentNoEntry = ttk.Entry(
    detailsFrame,
    state = "disabled"
)
studentNoEntry.pack(ipady = 5, fill='x', expand=True)

areaLabel = ttk.Label(detailsFrame, text = "Area: ")
areaLabel.pack(pady = 5,fill='x', expand=True)
areaEntry = ttk.Entry(
    detailsFrame,
    state = "disabled"
)
areaEntry.pack(ipady = 5, fill='x', expand=True)

timeLabel = ttk.Label(detailsFrame, text = "Time: ")
timeLabel.pack(pady = 5,fill='x', expand=True)
timeEntry = ttk.Entry(
    detailsFrame,
    state = "disabled"
)
timeEntry.pack(ipady = 5, fill='x', expand=True)

def okButton():
    pass

okButton = ttk.Button(
    detailsFrame,
    text = "Ok",
    command = okButton
)
okButton.pack(pady = 10, ipady=5, fill='x', expand=True)

reservationDetailsWindow.mainloop()