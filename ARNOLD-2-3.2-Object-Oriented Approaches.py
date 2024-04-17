# class creation
class Person:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number
# write get and set methods for each piece of data    
    def get_info(self):
        return f"{self.__name}, Address:  {self.__address}, Age:  {self.__age}, Phone #:  {self.__phone_number}"
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
# create 3 instances and display data
def main():
    person1 = Person("Phoebe Arnold", "25714 IL RT 173, Harvard, IL", "3", "224-422-2222")
    person2 = Person("Jack Black", "123 School of Rock Rd, Rock, IL", "54", "412-222-2122")
    person3 = Person("Max Holloway", "155 MMA Lane, UFC, IL", "32", "541-145-5151")

    print(person1.get_info())
    print(person2.get_info())
    print(person3.get_info())
main()
