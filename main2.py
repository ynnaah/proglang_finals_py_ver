# BOTH - Menu, Constructor/Classes
# JIGGS -  Reserve Slot, Txt Files: Times per Venue (4 Text Files), Student's Reservations 
# BONUS - Search Slot, View, Remove

# MENU

# RESERVE SLOT -> 4 VENUES -> INPUT DETAILS -> SUMMARY 
# SEARCH SLOT -> ENTER RSVP -> VIEW -> DELETE

# Reserve slot function

import os #clear screen
import time as systime

#global variables
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

#functions
def edit_slot(slot, venue, name, s_num):
    '''This function decrements the slot of a specific time and venue'''
    
    #read content
    with open(venue, "r") as file_read:
        file_read.seek(0,0)
        lines = file_read.readlines()

        #change 
        temp = lines[slot-1]
        temp.rstrip("\n")
        temp = int(temp)-1
        lines[slot-1] = str(temp)+"\n"

    #write new
    with open(venue, "w") as file_write:
        file_write.writelines(lines)

    #write student's info to the reservation file
    with open("reservations", "r") as file_read:
        file_read.seek(0,0)
        reservation = file_read.readlines()
        temp = reservation[0]
        temp.rstrip("\n")
        write_student(temp, name, s_num, venue, TIME[slot]) #write student's info

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

def refill_slot(line_no, venue):
    '''This function increments the slot of a specific time and venue'''
    print("HAHA", venue)
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

def read_slot(slot, venue):
    '''This function reads the remaining slot of a specific time and venue, and returns an integer'''

    #read content
    with open(venue, "r") as file_read:
        file_read.seek(0,0)
        lines = file_read.readlines()
        return int(lines[slot-1].rstrip("\n"))

def write_student(rsvp_num, name, stud_num, area, time):
    '''This function writes the student's info in the file for the reservation'''

    with open("reservations", "a") as file:
        file.seek(2)

        file.write(rsvp_num)
        file.write(name+"\n")
        file.write(stud_num+"\n")
        file.write(area+"\n")
        file.write(time+"\n")
    
def reserve_slot():
    '''This function reserves a slot for a students'''

    global TIME

    while(True):
        os.system("clear")
        print("Choose a venue:")
        print("[1] Pool Area")
        print("[2] 3rd Floor Gym")
        print("[3] 7th Floor Gym")
        print("[4] 17th Floor Gym")
        print("[5] Exit")
        
        choice = int(input("Enter choice: "))

        if(choice == 1):
            venue = "Pool"
            break
        elif(choice == 2):
            venue = "3rd Floor Gym"
            break
        elif(choice == 3):
            venue = "7th Floor Gym"
            break
        elif(choice == 4):
            venue = "17th Floor Gym"
            break
        elif(choice == 5):
            return main()
        else:
            print("Please enter a valid answer!")

    #user input
    while(True):
        try:
            os.system("clear")
            name = str(input("Enter your full name: "))

            if(name.isdigit()):
                raise TypeError

            s_num = str(input("Enter your student number: "))

            if(s_num.isalpha()):
                raise TypeError

            break
        except TypeError:
            print("Please enter a valid answer!")
            systime.sleep(2)

    while(True):
        try:
            print("\n\
            [1]8:00am - 9:00am (%s slots left)\n\
            [2]9:00am - 10:00am (%s slots left)\n\
            [3]10:00am - 11:00am (%s slots left)\n\
            [4]12:00nn - 1:00pm (%s slots left)\n\
            [5]1:00pm - 2:00pm (%s slots left)\n\
            [6]2:00pm - 3:00pm (%s slots left)\n\
            [7]3:00pm - 4:00pm (%s slots left)\n\
            [8]4:00pm - 5:00pm (%s slots left)\n" % (str(read_slot(1, venue)), str(read_slot(2, venue)), str(read_slot(3, venue)), str(read_slot(4, venue)), str(read_slot(5, venue)), str(read_slot(6, venue)), str(read_slot(7, venue)), str(read_slot(8, venue))))
            t = int(input("Choose time: "))
            break
        except TypeError:
            print("Please enter a valid answer!")
            systime.sleep(2)

    #checks if a specific time still has a slot
    if(read_slot(t, venue) > 0):
        edit_slot(t, venue, name, s_num) #decrements a slot
    else:
        os.system("clear")
        print("No more slots available!")
        print("Please choose another time or venue")
        systime.sleep(3)
        return main()

    #find rsvp number of latest register
    with open("reservations", "r+") as file:
        file.seek(0,0)
        lines = file.readlines()

        rsvp_num = int(lines[0].rstrip("\n"))-1
        rsvp_num = str(rsvp_num)

    #output
    os.system("clear")
    print("RSVP Number: \t" + rsvp_num)
    print("Name: \t\t" + name)
    print("Student number: " + s_num)
    print("Area: \t\t" + venue)
    print("Time: \t\t" + str(TIME[t]))

    input("Press enter to continue...")
    return main()

def search_slot():
    try:
        rsvp_no = int(input("Enter RSVP Number here: "))
    except ValueError: 
        os.system("clear")
        print("Invalid input!")
        systime.sleep(2)
        os.system("clear")
        return search_slot()
    else:
           with open("reservations", "r") as file:
                line = file.readlines()
                line_length = len(line)
                counter = 1
                while counter < line_length:
                    if line[counter] == str(rsvp_no)+"\n":
                        print("\nRSVP Number: {}".format(line[counter]), end="")
                        line_no1 = counter
                        counter += 1
                        print("\tName: {}".format(line[counter]), end="")
                        line_no2 = counter
                        counter += 1
                        print("\tStudent Number: {}".format(line[counter]), end="")
                        line_no3 = counter
                        counter += 1
                        print("\tArea: {}".format(line[counter]), end="")
                        line_no4 = counter
                        venue = line[counter].strip()
                        counter += 1
                        print("\tTime: {}".format(line[counter]), end="---------------------------------------------------\n")
                        time = line[counter].strip()
                        line_no5 = counter
                        counter +=1
                        answer = input("Do you wish to cancel your reservation? [y/n]: ")
                        if answer == "y" or answer == "Y":
                            print("Reservation has been cancelled.")
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
                            print("\nSee you there!")
                            input("\nPress enter to continue...")
                        break 
                    else:
                        counter+=5 
                else:
                    print("No reservations made with that RSVP number!")
                    input("\nPress enter to continue...")
    return main()

# Main menu
def main():
    os.system("clear")
    print("=============================================================")
    print("P.E. RESERVATION SYSTEM")
    print("=============================================================")
    print("[1] RESERVE SLOT")
    print("[2] SEARCH SLOT")
    print("[3] Exit")
    print("=============================================================")
    choice = int(input("Enter choice: "))
    if choice == 1:
        reserve_slot()
    elif choice == 2:
        #function2
        search_slot()
    elif(choice == 3):
        return
    else:
        print("Invalid option")

#main
os.system("clear")
main()