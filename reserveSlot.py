import time as systime
import tkinter as tk
from tkinter import ttk, Toplevel

import reservationTicket as rtWindow

reserveSlotWindow: tk = None #instance of tk that creates window

def reserveSlot(choice, parentTkClass: tk):
    # from here... vv
    reserveSlotWindow = Toplevel(parentTkClass)
    
    def fillSet():
        #gamitin niyo yung choice var as key para malaman ano ilalagay sa list
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

        new_list = list(TIME.values())   
        return new_list

    def submitButton():
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
        name = nameEntry.get()
        studentNo = studentNoEntry.get()
        time = current_time.get()

        key_list = list(TIME.keys())
        val_list = list(TIME.values())

        position = val_list.index(time)
        slot = key_list[position]

        #reading slots based on venue and time
        with open(choice, "r") as file_read:
            file_read.seek(0,0)
            lines = file_read.readlines()
            current_slot = int(lines[slot-1])

        #check if current slot is full or not
        if(current_slot > 0):
             #read content
            with open(choice, "r") as file_read:
                file_read.seek(0,0)
                lines = file_read.readlines()

                #change 
                temp = lines[slot-1]
                temp.rstrip("\n")
                temp = int(temp)-1
                lines[slot-1] = str(temp)+"\n"

            #write new
            with open(choice, "w") as file_write:
                file_write.writelines(lines)

            #write student's info to the reservation file
            with open("reservations", "r") as file_read:
                file_read.seek(0,0)
                reservation = file_read.readlines()
                temp = reservation[0]
                temp.rstrip("\n")
                write_student(temp, name, studentNo, choice, TIME[slot]) #write student's info

            #increment RSVP number
            with open("reservations", "r") as file:
                file.seek(0,0)
                reservation = file.readlines()

            #change
            temp = reservation[0]
            temp.rstrip("\n")
            temp = int(temp)+1
            reservation[0] = str(temp)+"\n"

            #writing incremented rsvp number
            with open("reservations", "w") as file:
                file.writelines(reservation)

            #find rsvp number of latest register
            with open("reservations", "r+") as file:
                file.seek(0,0)
                lines = file.readlines()

                rsvp_num = int(lines[0].rstrip("\n"))-1
                rsvp_num = str(rsvp_num)

            #output
            #os.system("clear")
            print("RSVP Number: \t" + rsvp_num)
            print("Name: \t\t" + name)
            print("Student number: " + studentNo)
            print("Area: \t\t" + choice)
            print("Time: \t\t" + str(TIME[slot]))

            confirmation = [rsvp_num, name, studentNo, choice, str(TIME[slot])]
            rtWindow.reservationTicket(reserveSlotWindow, dataToShow=confirmation)

        else:
            print("Slot is full! Please choose another venue or time.")
            systime.sleep(2)

    #yung choi var ang magiindicate ng pinili ni user na area gawan niyo na lang if else or switch
    #d2 lalagay ni bonus and jiggs yung code for reservations

    def write_student(rsvp_num, name, stud_num, area, time):
        '''This function writes the student's info in the file for the reservation'''

        with open("reservations", "a") as file:
            file.seek(2)

            file.write(rsvp_num)
            file.write(name+"\n")
            file.write(stud_num+"\n")
            file.write(area+"\n")
            file.write(time+"\n")

    #window elements
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

    TimeLabel = ttk.Label(detailsFrame,text = "Select Time: ")
    TimeLabel.pack(pady = 5,fill='x', expand=True)

    current_time = tk.StringVar()
    availableTimes = ttk.Combobox(detailsFrame, textvariable = current_time)

    availableTimes['values'] = fillSet() #data type is list

    availableTimes['state'] = 'readonly'

    availableTimes.pack(ipady = 5, fill='x', expand = True)

    submitButton = ttk.Button(
        detailsFrame,
        text = "Submit",
        command = submitButton
    )
    submitButton.pack(pady = 30, ipady=5, fill='x', expand=True)

    reserveSlotWindow.mainloop()
    # until here uwu ^^
