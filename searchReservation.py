import string
import tkinter as tk
from tkinter import StringVar, ttk, Toplevel

import reservationTicket as rtWindow

searchReservationWindow: tk = None

def searchReservation(parentTkClass: tk):
    searchReservationWindow = Toplevel(parentTkClass)
    
    #window elements
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
        srcKey = str(ticketNoEntry.get())

        #tas d2 niyo lalagay yung backend ng src algorithm
        with open("reservations", "r") as file:
            line = file.readlines()
            line_length = len(line)
            counter = 1
            while counter < line_length:
                if line[counter] == srcKey+"\n":
                    print("\nRSVP Number: {}".format(line[counter]), end="")
                    rsvp_no = line[counter].rstrip("\n")
                    line_no1 = counter
                    counter += 1
                    print("\tName: {}".format(line[counter]), end="")
                    stud_name = line[counter].rstrip("\n")
                    line_no2 = counter
                    counter += 1
                    print("\tStudent Number: {}".format(line[counter]), end="")
                    stud_no = line[counter].rstrip("\n")
                    line_no3 = counter
                    counter += 1
                    print("\tArea: {}".format(line[counter]), end="")
                    pe_area = line[counter].rstrip("\n")
                    line_no4 = counter
                    venue = line[counter].strip()
                    counter += 1
                    print("\tTime: {}".format(line[counter]), end="---------------------------------------------------\n")
                    time_slot = line[counter].rstrip("\n")
                    time = line[counter].strip()
                    line_no5 = counter
                    counter +=1

                    values = [rsvp_no, stud_name, stud_no, pe_area, time_slot]
                    rtWindow.reservationTicket(searchReservationWindow, dataToShow=values)
                    

                    break 
                else:
                    counter+=5
            else: #ERROR CHECKPOINT
                print("No reservations made with that RSVP number!")
                input("\nPress enter to continue...")
                #return main()

    submitButton = ttk.Button(
        detailsFrame,
        text = "Search",
        command = searchButton
    )
    submitButton.pack(pady = 30, ipady=5, fill='x', expand=True)
    
    searchReservationWindow.mainloop()

