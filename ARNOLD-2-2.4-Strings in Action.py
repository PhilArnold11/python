def main():  # set up main function
    titles = []  # created empty titles list
    while len(titles) < 10:  # While loop to collect 10 book titles./I used this website to help me form my while loop http://introtopython.org/while_input.html
        new_title = input('Please enter the titles of 10 books one entry at a time:  ') # prompt user to enter book titles until 10 titles have been entered
        new_title = new_title.title() # use the title function to make sure first letter is capitalized before storing into list
        titles.append(new_title)  # store titles in list

    titles.sort()  # create a sorted list

    for title in titles:  # use a for loop to print each title on a separate line
        print(title)


main()
#when I used the autopep8 formatter it moved my comments around so I left it as is