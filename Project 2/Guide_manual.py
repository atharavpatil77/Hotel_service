from colorama import Fore
def show_manual():
   print(f"""Guide Manual for User: Hotel Management Service
{Fore.BLACK}
1. Food Ordering:{Fore.YELLOW}
   - The Food Ordering service offers a variety of options, including Desserts, Appetizers, and Main Courses.
   - To use the service, choose one of the following:
      - 1: Dessert
      - 2: Appetizer
      - 3: Main Course
   - Make a selection based on your preference.
   - After each selection, the chosen item will be displayed with its details and added to the cart.
   - You can continue ordering more items by entering 'y' when prompted.
   - Once you are done, your total bill, including tax, will be displayed.
   - Choose your payment method: Online or Cash.
   - If you choose Online, enter your UPI ID when prompted.
{Fore.BLACK}
2. Dine-In:{Fore.BLUE}
   - The Dine-In service allows you to book tables at the hotel.
   - Choose from the following options:
      - 1: Display Available Tables
      - 2: Display Current Reservations
      - 3: Book a Table
      - 4: Exit
   - If you choose to book a table, enter the table number, date (YYYY-MM-DD), and time (HH:MM AM/PM).
   - The system will confirm the reservation if the table is available.
{Fore.BLACK}
3. Event Management:{Fore.GREEN}
   - The Event Management service allows you to view, enroll, and check enrollment status for various events.
   - Choose from the following options:
      - 1: Display Events
      - 2: Enroll in an Event
      - 3: Check Enrollment Status
      - 4: Exit
   - Follow the prompts to view events, enroll in an event, or check your enrollment status.
{Fore.BLACK}
4. Guide Manual:{Fore.WHITE}
   - This option provides information about using the Hotel Management Service.
   - It includes the functionality of each service and guides the user through the available options.
   - You can refer to this manual if you have any questions about how to use the system.
{Fore.BLACK}
Usage Instructions:{Fore.LIGHTWHITE_EX}
   - Choose the desired service by entering the corresponding number.
   - Follow the prompts and instructions displayed during each service.
   - If you encounter any issues, refer to the Guide Manual (option 4) for assistance.
   - Enjoy your experience with the Hotel Management Service!""")