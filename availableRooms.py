import tkinter as tk
from tkinter import ttk, Toplevel

import reserveSlot as rsWindow

availRoomsWindow: tk = None

def availableRooms(parentTkClass: tk):
    availRoomsWindow = Toplevel(parentTkClass)

    #window elements
    availRoomsWindow.title("PE Reservation System | Available Areas ")
    availRoomsWindow.geometry('600x600')
    availRoomsWindow.resizable(False,False)

    #widgets
    icon = tk.PhotoImage(file='./icons/selection.png')
    icon_display = ttk.Label(
        availRoomsWindow,
        image = icon,
        compound = 'image'
    )

    icon_display.pack(ipady=40)

    availRoomsLabel = ttk.Label(
        availRoomsWindow,
        text = "Available Areas",
        font = ("Arial", 16)
    )

    availRoomsLabel.pack(ipady=10)

    poolButton = ttk.Button(
        availRoomsWindow,
        text = "Pool Area",
        command = poolArea
    )

    poolButton.pack(pady = 5, ipadx=150, ipady=10)

    gym3FButton = ttk.Button(
        availRoomsWindow,
        text = "3rd Floor Gym",
        command = Gym3F
    )

    gym3FButton.pack(pady = 5, ipadx=145, ipady=10)

    gym11FButton = ttk.Button(
        availRoomsWindow,
        text = "7th Floor Gym",
        command = Gym7F
    )

    gym11FButton.pack(pady = 5, ipadx=142, ipady=10)

    gym15FButton = ttk.Button(
        availRoomsWindow,
        text = "15th Floor Gym",
        command = Gym15F
    )

    gym15FButton.pack(pady = 5, ipadx=142, ipady=10)

    # mainMenuButton = ttk.Button(
    #     availRoomsWindow,
    #     text = "Main Menu",
    #     command = mainMenu
    # )

    # mainMenuButton.pack(pady = 30, ipadx=149, ipady=10)

    # availRoomsWindow.protocol("WM_DELETE_WINDOW", parentTkClass.deiconify)
    availRoomsWindow.mainloop()

def poolArea():
    choice = "Pool"
    callReserve(choice)

def Gym3F():
    choice = "3rd Floor Gym"
    callReserve(choice)

def Gym7F():
    choice = "7th Floor Gym"
    callReserve(choice)

def Gym15F():
    choice = "17th Floor Gym"
    callReserve(choice)

def callReserve(choice):
    rsWindow.reserveSlot(choice, parentTkClass = availRoomsWindow)
