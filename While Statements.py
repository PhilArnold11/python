count = 99

while count >= 2:
    print(count, 'bottles of beer on the wall')
    print(count, 'bottles of beer')
    print('Take one down, pass it around')
    count -= 1
    print(count, 'bottles of beer on the wall!\n')

if count == 1:
    print(count, 'bottle of beer on the wall')
    print(count, 'bottle of beer')
    print('Take it down, pass it around')
    count -= 1
    print('No more bottles of beer on the wall!')
