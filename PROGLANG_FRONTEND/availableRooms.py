import tkinter as tk
from tkinter import ttk

#window elements
availRoomsWindow = tk.Tk() #instance of tk that creates window
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

def poolArea():
    pass

poolButton = ttk.Button(
    availRoomsWindow,
    text = "Pool Area",
    command = poolArea
)
poolButton.pack(pady = 5, ipadx=150, ipady=10)

def Gym3F():
    pass

gym3FButton = ttk.Button(
    availRoomsWindow,
    text = "3rd Floor Gym",
    command = Gym3F
)
gym3FButton.pack(pady = 5, ipadx=145, ipady=10)

def Gym11F():
    pass

gym11FButton = ttk.Button(
    availRoomsWindow,
    text = "11th Floor Gym",
    command = Gym11F
)
gym11FButton.pack(pady = 5, ipadx=142, ipady=10)

def Gym15F():
    pass

gym15FButton = ttk.Button(
    availRoomsWindow,
    text = "15th Floor Gym",
    command = Gym15F
)
gym15FButton.pack(pady = 5, ipadx=142, ipady=10)

def mainMenu():
    pass

mainMenuButton = ttk.Button(
    availRoomsWindow,
    text = "Main Menu",
    command = mainMenu
)
mainMenuButton.pack(pady = 30, ipadx=149, ipady=10)

availRoomsWindow.mainloop()
