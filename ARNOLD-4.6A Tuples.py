def main():
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals')#create tuple
    for item in programming_classes:#use a loop to print each class
        print(item)
    print('There are', len(programming_classes), 'programming classes.')#use len function to print how many classes are in tuple.
main()