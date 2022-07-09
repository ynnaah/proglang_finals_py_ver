import tkinter as tk
from tkinter import Frame, Label, ttk

#window elements
mainMenuWindow = tk.Tk() #instance of tk that creates window
mainMenuWindow.title("PE Reservation System | Main Menu")
mainMenuWindow.geometry('600x600')
mainMenuWindow.resizable(False,False)

#widgets
icon = tk.PhotoImage(file='./icons/training.png')
icon_display = ttk.Label(
    mainMenuWindow,
    image = icon,
    compound = 'image'
)
icon_display.pack(ipady=50)

icon_label = ttk.Label(
    mainMenuWindow,
    text = "Welcome to PE Reservation!",
    font = ("Arial", 16)
)
icon_label.pack(pady=10)

def reserveSlot():
    pass #function for reserving slots insert here

reserveButton = ttk.Button(
    mainMenuWindow,
    text = "Reserve a Slot",
    command = reserveSlot
)
reserveButton.pack(pady = 5, ipadx=150, ipady=10)

def  viewSlots():
    pass #function for viewing slots insert here

viewButton = ttk.Button(
    mainMenuWindow,
    text = "View Slots",
    command = viewSlots
)
viewButton.pack(pady = 5, ipadx = 152,ipady = 10)


exitButton = ttk.Button(
    mainMenuWindow,
    text = "Exit Program",
    command=lambda: mainMenuWindow.quit()
)
exitButton.pack(pady = 5, ipadx = 151,ipady = 10)

mainMenuWindow.mainloop() #mainloop keeps window visible
