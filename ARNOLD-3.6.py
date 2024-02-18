# Initialize the seating list
seats = list(range(1, 21))
# display available seats
def display_available_seats():
    print("Available Seats:", seats)

# implement ticket purchase process
def ticket_purchase_process():
    while True:
        display_available_seats()
        selected_seat = input("Enter the seat number you want to purchase (enter '0' to finish): ")
        
        # Continue the process until customer enters 0, indicating they are done buying tickets
        if selected_seat == '0':
            break
        
        # Check if the input is a valid seat number
        try:
            selected_seat = int(selected_seat)
            if selected_seat < 1 or selected_seat > 20:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a valid seat number.")
            continue
        
        # Check if the selected seat is available
        if selected_seat in seats:
            print(f"You have successfully purchased seat {selected_seat}.")
            seats.remove(selected_seat)
        else:
            print("Sorry, the selected seat is not available. Please choose another seat.")

#run program
print("Welcome to the ticket purchase system!")
ticket_purchase_process()
print("Thank you for using our ticket purchase system.")