class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self,name,pet_type, owner = None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.name = name
        self.owner =owner
        self.pet_type = pet_type
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
    def pets(self):
        return self._pets 
    
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception(f"{pet} is not a valid pet")
        self._pets.append(pet)
        pet.owner = self
        
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)