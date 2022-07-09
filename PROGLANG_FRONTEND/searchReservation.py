import tkinter as tk
from tkinter import ttk

#window elements
searchReservationWindow = tk.Tk() #instance of tk that creates window
searchReservationWindow.title("PE Reservation System | Search Reservation")
searchReservationWindow.geometry('600x600')
searchReservationWindow.resizable(False,False)

#widgets
icon = tk.PhotoImage(file='./icons/search.png')
icon_display = ttk.Label(
    searchReservationWindow,
    image = icon,
    compound = 'image'
)
icon_display.pack(ipady=50)

reserveSlotLabel = ttk.Label(
    searchReservationWindow,
    text = "Enter Ticket Number:",
    font = ("Arial", 16)
)
reserveSlotLabel.pack(pady=30)

detailsFrame = ttk.Frame(searchReservationWindow)
detailsFrame.pack(padx=50, fill='x', expand=False)

ticketNoLabel = ttk.Label(detailsFrame,text = "Ticket Number: ")
ticketNoLabel.pack(pady = 10,fill='x', expand=True)
ticketNoEntry = ttk.Entry(
    detailsFrame
)
ticketNoEntry.pack(ipady = 5, fill='x', expand=True)

def searchButton():
    pass

submitButton = ttk.Button(
    detailsFrame,
    text = "Search",
    command = searchButton
)
submitButton.pack(pady = 30, ipady=5, fill='x', expand=True)

searchReservationWindow.mainloop()
