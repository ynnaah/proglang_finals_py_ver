import os, time as systime
import tkinter as tk
from tkinter import Frame, Label, ttk

import availableRooms as arWindow
import searchReservation as srWindow

mainMenuWindow = tk.Tk() #instance of tk that creates window
 
def mainMenu():
    #window elements
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

    TIME = {
        1: "8:00am to 9:00am",
        2: "9:00am to 10:00am",
        3: "10:00am to 11:00am",
        4: "12:00nn to 1:00pm",
        5: "1:00pm to 2:00pm",
        6: "2:00pm to 3:00pm",
        7: "3:00pm to 4:00pm",
        8: "4:00pm to 5:00pm"
    }

    reserveButton = ttk.Button(
        mainMenuWindow,
        text = "Reserve a Slot",
        command = availableRooms
    )
    reserveButton.pack(pady = 5, ipadx=150, ipady=10)

    viewButton = ttk.Button(
        mainMenuWindow,
        text = "Query Reservation",
        command = searchReservation
    )
    viewButton.pack(pady = 5, ipadx = 137,ipady = 10)


    exitButton = ttk.Button(
        mainMenuWindow,
        text = "Exit Program",
        command=lambda: mainMenuWindow.quit()
    )
    exitButton.pack(pady = 5, ipadx = 151, ipady = 10)

    mainMenuWindow.mainloop() #mainloop keeps window visible

def availableRooms():
    # mainMenuWindow.withdraw()
    arWindow.availableRooms(parentTkClass=mainMenuWindow)

def searchReservation():
    # mainMenuWindow.withdraw()
    srWindow.searchReservation(parentTkClass=mainMenuWindow)

if __name__ == '__main__':
    mainMenu()