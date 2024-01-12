from datetime import date
from dine_in_Class import *

def dine_in_menu():
    # Predefined tables with details
    tables_info = {
        1: {"availability": True, "cost": 200},
        2: {"availability": True, "cost": 200},
        3: {"availability": True, "cost": 250},
        4: {"availability": True, "cost": 250}
    }

    booking_system = TableBookingSystem(tables_info) # made object of tablebookingsystem class 

    while True:
        print("\n===== Hotel Table Booking System =====")
        print("1. Display Available Tables")
        print("2. Display Current Reservations")
        print("3. Book a Table")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            booking_system.display_tables()
        elif choice == "2":
            booking_system.display_reservations()
        elif choice == "3":
            booking_system.display_tables()
            table_number = int(input("Enter the table number you want to book: "))
            while(not(tables_info[table_number]["availability"])):
                print("Already booked Table you are trying to book")
                table_number = int(input("Enter the table number you want to book: "))
            
            
            while(True):
                a = [int(i) for i in (str(date.today()).split("-"))]
                try:
                    ask = [int(i) for i in input("Enter the date (YYYY-MM-DD): ").split("-")] 
                except:
                    print("Enter only numbers")
                    continue
                if(1000 < ask[0] < a[0]):
                    print("Wrong year")

                else:
                    if(0 < ask[1] < a[1]):
                        print("Wrong month the date has already passed")
                    else:
                        if(ask[1] > a[1]):
                            print("Next month booking is not possible")
                        else:
                            if(ask[1] == a[1]):
                                if(ask[2] < a[2]):
                                    print("Date has passed")
                                else:
                                    break
                            else:
                                break
            while True:
                time = input("Enter the time 24 hr format (HH:MM:(AM/PM)) : ").split(":")
                time[0],time[1]= int(time[0]) , int(time[1])
                

                if(not(time[2].upper() == "AM" or time[2].upper() == "PM" )):
                    print("Only Am/pm")
                    continue
                else:
                    if(not( 0 < time[0] <= 24)):
                        print("Wrong input for time see the format")
                        continue
                    else:
                        if(not(0 <= time[1] < 60)):
                            print("Wrong input for minutes see the format")
                            continue
                        break
            booking_system.book_table(table_number, ask, time)
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

