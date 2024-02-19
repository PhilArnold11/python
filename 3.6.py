seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('Available Seats: ', seats)
seats_purchased = '2'
while seats_purchased !='0':
    for seat in seats:
        print('Available Seats: ', seats)
    seats_purchased = input('\nPlease enter the seat you would like to purchase from the list of available seats (Enter 0 when complete):  ')
    if seats_purchased in seats:
        seats.remove(seats_purchased)
    
    if len(seats) == 0:
        print('Sorry there are no more seats available.')
