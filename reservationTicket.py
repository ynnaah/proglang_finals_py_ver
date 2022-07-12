from cgitb import text
import tkinter as tk
import time as systime
from tkinter import Label, ttk, Toplevel

def reservationTicket(parentTkClass: tk, dataToShow):
    reservationDetailsWindow = Toplevel(parentTkClass)
    
    #                   0        1          2        3        4
    # dataToShow = [rsvp_no, stud_name, stud_no, pe_area, time_slot]

    def okButton():
        #ako na gagawa ne2
        pass

    def cancelButton():
        srcKey = dataToShow[0]

        #tas d2 niyo lalagay yung backend ng src algorithm
        with open("reservations", "r") as file:
            line = file.readlines()
            line_length = len(line)
            counter = 1
            while counter < line_length:
                if line[counter] == srcKey+"\n":
                    print("\nRSVP Number: {}".format(line[counter]), end="")
                    rsvp_no = line[counter]
                    line_no1 = counter
                    counter += 1
                    print("\tName: {}".format(line[counter]), end="")
                    stud_name = line[counter]
                    line_no2 = counter
                    counter += 1
                    print("\tStudent Number: {}".format(line[counter]), end="")
                    stud_no = line[counter]
                    line_no3 = counter
                    counter += 1
                    print("\tArea: {}".format(line[counter]), end="")
                    pe_area = line[counter]
                    line_no4 = counter
                    venue = line[counter].strip()
                    counter += 1
                    print("\tTime: {}".format(line[counter]), end="---------------------------------------------------\n")
                    time_slot = line[counter]
                    time = line[counter].strip()
                    line_no5 = counter
                    counter +=1
                
                    filelines = []
                    with open("reservations", 'r') as fp:
                        filelines = fp.readlines()
                    with open("reservations", 'w') as fp:
                        for i, line in enumerate(filelines):
                            if i not in [line_no1, line_no2, line_no3, line_no4, line_no5]:
                                fp.write(line)
                    if time == "8:00am to 9:00am":
                        line_no = 1
                    elif time == "9:00am to 10:00am":   
                        line_no = 2
                    elif time == "10:00 am to 11:00 am:":
                        line_no = 3
                    elif time == "12:00nn to 1:00pm":
                        line_no = 4
                    elif time == "1:00pm to 2:00pm":
                        line_no = 5
                    elif time == "2:00pm to 3:00pm":
                        line_no = 6
                    elif time == "3:00pm to 4:00pm":
                        line_no = 7
                    else:
                        line_no = 8
                    refill_slot(line_no, venue)
                    systime.sleep(2)
                    break 
                else:
                    counter+=5 
            else: #ERROR CHECKPOINT
                print("No reservations made with that RSVP number!")
                input("\nPress enter to continue...")

    def refill_slot(line_no, venue):
        '''This function increments the slot of a specific time and venue'''
        slot = int(line_no)
        #read content
        with open(venue, "r") as file_read:
            file_read.seek(0,0)
            lines = file_read.readlines()
    
            #change 
            temp = lines[slot-1]
            temp.rstrip("\n")
            temp = int(temp)+1
            print(temp)
            lines[slot-1] = str(temp)+"\n"
    
        #write new
        with open(venue, "w") as file_write:
            file_write.writelines(lines)

    #window elements
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


    ticketNoLabel = ttk.Label(detailsFrame,font = ("Arial", 12),text = "Ticket Number: " + dataToShow[0])
    ticketNoLabel.pack(pady = 5, fill='x', expand=True)
    # ticketNoEntry = ttk.Entry(
    #     detailsFrame,
    #     state = "disabled"
    # )
    # ticketNoEntry.pack(ipady = 5, fill='x', expand=True)

    nameLabel = ttk.Label(detailsFrame,font = ("Arial", 12),text = "Name: " + dataToShow[1])
    nameLabel.pack(pady = 5,fill='x', expand=True)
    # nameEntry = ttk.Entry(
    #     detailsFrame,
    #     state = "disabled"
    # )
    # nameEntry.pack(ipady = 5, fill='x', expand=True)

    studentNoLabel = ttk.Label(detailsFrame,font = ("Arial", 12),text = "Student Number: " + dataToShow[2])
    studentNoLabel.pack(pady = 5,fill='x', expand=True)
    # studentNoEntry = ttk.Entry(
    #     detailsFrame,
    #     state = "disabled"
    # )
    # studentNoEntry.pack(ipady = 5, fill='x', expand=True)

    areaLabel = ttk.Label(detailsFrame,font = ("Arial", 12), text = "Area: " + dataToShow[3])
    areaLabel.pack(pady = 5,fill='x', expand=True)
    # areaEntry = ttk.Entry(
    #     detailsFrame,
    #     state = "disabled"
    # )
    # areaEntry.pack(ipady = 5, fill='x', expand=True)

    timeLabel = ttk.Label(detailsFrame,font = ("Arial", 12), text = "Time: " + dataToShow[4])
    timeLabel.pack(pady = 5,fill='x', expand=True)
    # timeEntry = ttk.Entry(
    #     detailsFrame,
    #     state = "disabled"
    # )
    # timeEntry.pack(ipady = 5, fill='x', expand=True)

    okButton = ttk.Button(
        detailsFrame,
        text = "Ok",
        command = okButton
    )
    okButton.pack(pady = 10, ipady=5, fill='x', expand=True)

    cancelButton = ttk.Button(
        detailsFrame,
        text = "Cancel Reservation",
        command = cancelButton
    )
    cancelButton.pack(pady = 10, ipady=5, fill='x', expand=True)

    reservationDetailsWindow.mainloop()