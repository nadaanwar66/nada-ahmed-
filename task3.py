class Magical_contacnt_book:
    def __init__(self,name,email,phone_num):
        self.__name= name
        self.__email= email
        self.__phone_num= phone_num
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email
    def get_phone_num(self):
        return self.__phone_num
    def set_email(self,new_email):
        self.__email= new_email
    def set_phone_num(self,new_phone_number):
        self.__phone_num = new_phone_number
    def describe(self):
        print(f"hello my name is{self.__name}, my email is {self.__email}, my phone number is{self.__phone_num}")

class WizardOrWitch(Magical_contacnt_book):  
    def __init__(self, name, email, phone_num, wand, house):
        super().__init__(name, email, phone_num)

        valid_houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        if house not in valid_houses:
            print("Invalid house provided!") 

        self.__wand = wand
        self.__house = house

    def get_wand(self):
        return f"{self.__wand['length']}, {self.__wand['wood']}, {self.__wand['core']}"

    def get_house(self):
        return self.__house
    def describe(self):
        print(f"Name: {self.get_name()}, "
              f"Email: {self.get_email()}, "
              f"Phone: {self.get_phone_num()}, "
              f"Wand: {self.get_wand()}, "
              f"House: {self.__house}")
class Magicalcreature(Magical_contacnt_book):
    def __init__(self, name, email, phone_num,species,is_tame):
        super().__init__(name, email, phone_num)
        self.__species = species
        self.__is_tame = is_tame
    def get_species(self):
        return self.__species
    def tame(self):
        return self.__is_tame
    def describe(self):
        if self.__is_tame:
            tame_status = "Tame"
        else:
            tame_status = "Not tame"
        
        print(f"Name: {self.get_name()}, Email: {self.get_email()}, Phone: {self.get_phone_num()}, Species: {self.__species}, Tame: {tame_status}")
class MagicalContactBook:
    def __init__(self):
        self.__contacts = []  

    def add_contact(self, contact):
        self.__contacts.append(contact)  

    def list_contacts(self):
        for contact in self.__contacts:
            contact.describe()   

    def find_contact(self, name):
        for contact in self.__contacts:
            if contact.get_name() == name:
                contact.describe()
                return
        print("Contact not found.")

  
    

