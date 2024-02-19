#initialize a seating list
seats = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
seats_purchased = '50'
#ticket purchase process loop
while seats_purchased !='0':
    print('Available Seats: ', seats)#display available seats
    seats_purchased = input('\nPlease enter the seat you would like to purchase from the list of available seats (Enter 0 when complete):  ')
#prompt to end purchase process
    if seats_purchased == '0':
        print('Thank you for purchasing tickets! Your session has ended.')
        break
#update seat availability & ensure user-friendly interaction
    if seats_purchased in seats:
        seats.remove(seats_purchased)
        print('Seat successfully purchased.')
    else:
        print('Please choose another seat, the seat you selected has already been sold or does not exist.')
    
    if len(seats) == 0:
        print('Sorry there are no more seats available.')
