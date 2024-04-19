# define pet class
class Pet:
    # class variable
    vet_name = "Phil's Vet CLinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):#set defauly value for pet_type "Dog"
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type
#getter and setter methods for all properties
    def get_owner_first_name(self):
        return self.__owner_first_name
    def get_owner_last_name(self):
        return self.__owner_last_name
    def get_pet_id(self):
        return self.__pet_id
    def get_pet_name(self):
        return self.__pet_name
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self, owner_first_name):
        self.__owner_first_name = owner_first_name
    def set_owner_last_name(self, owner_last_name):
        self.__owner_last_name = owner_last_name
    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id
    def set_pet_name(self, pet_name):
        self.__pet_name = pet_name
    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    def print_pet_details(self):
        print("Pet Details:", vars(self))
    
    def print_display_pet_info(self):#Add method display_pet_info
        print(self.__owner_first_name + " " + self.__owner_last_name)
        print(self.__pet_id)
        print(self.__pet_name)
        print(self.__pet_type)

def main():
    pet1 = Pet("Phil", "Arnold", '42412', "Phoebe")#create pet objects
    pet3 = Pet("Joe", "Jackson", "52025", "Tank")


    print(pet1.get_pet_name())
    pet1.print_pet_details()
    print(pet1.print_display_pet_info())
    print("\n\n\n")
    print(pet3.print_display_pet_info())
    pet3.print_pet_details()
    """
    pet2.set_owner_first_name("Joe")    Here I am trying to use the setter method for a pet object but I am not doing this correctly and cannot figure out what I am doing wrong
    pet2.set_owner_last_name("Lee")
    pet2.set_pet_id("45414")
    pet2.set_pet_name("Gabby")
    print(pet2.__owner_first_name)
    
    def check_property():               Here I am trying to write a function for a property existence check. 
        print(hasattr(Pet, "owner_first_name"))
    check_property()
    """

    """ I can't move onto these steps yet because I am stuck on the parts listed above.
    Display Information:
    Use display_pet_info to print details for each pet.
    Show examples of check_property being used on various properties and pets.
    """
main()

