#Define an Owner class and pass into the constructor a name argument
#Define a Pet and pass into the constructor its name, pet_type, and an optional owner
#Define a class variable PET_TYPES and validate that the pet_type is one of those types in the init method
#Define a class variable all that stores all instances of the Pet class
#write a method called pets(self) that returns a full list of the owner's pet
#In the Owner class, write a method called add_pet(self, pet) 
#returns a sorted list of pets by their names:

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if isinstance(pet.owner, Owner) and pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be of type Pet.")
        pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda x: x.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
