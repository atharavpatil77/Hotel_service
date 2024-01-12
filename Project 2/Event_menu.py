from event_Class import *

def Events_menu():
    while True:
        print("\nWelcome to Events Management System")
        print("1. Display Events")
        print("2. Enroll in an Event")
        print("3. Check Enrollment Status")
        print("4. Exit")

        Event_Method = Event()
        choice = input("Enter your choice (1/2/3/4): ")
        print("\n\n")
        if choice == "1":
            Event_Method.display_events()
        elif choice == "2":
            Event_Method.display_events()
            event_id = int(input("Enter the Event ID you want to enroll in: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            enrollment_id = Event_Method.enroll(event_id, name, email)
            if enrollment_id is not None:
                print(f"{Fore.GREEN}Enrollment successful! Your Enrollment ID is {enrollment_id}.")
            else:
                print("Invalid Event ID. Please choose a valid event.")
        elif choice == "3":
            ask = 1
            while ask not in Event_Method.enrollments:
                ask = (input("Enter your enrollment ID that was assigned to you on the point of registration  : "))
                
                if (ask in Event_Method.enrollments):
                    user_enrollment_id = Event_Method.enrollments[ask]["Enrollment ID"]
                    name_user = Event_Method.enrollments[ask]["Name"]
                    event_enrolled = Event_Method.enrollments[ask]["Event"]
                    print(f"{Fore.RED}Enrollment ID : {user_enrollment_id}\nYour Name : {name_user}\nEvent : {event_enrolled}")
                    
                else:
                    y = input("If you forgot the enrollment Id(press 0) or Press any button to retry  : ")
                    if(y == "0"):
                        email = input("Please Enter your email : ")
                        for i in Event_Method.enrollments:
                            if Event_Method.enrollments[i]["Email"] == email:
                                print(i,"\nRemember this id and retry :)")
                                return 201
                        print("Sorry Your acc was not found in the data did you mean to register???")
                        return 101
                       
                        
        elif choice == "4":
            print("Exiting the Events Management System. Goodbye!")
            return 101
        else:
            print("Invalid choice. Please enter a valid option.")
