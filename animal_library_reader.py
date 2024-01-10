

file_path = "animal_library.txt"

#reading animal names from the text file into a list
animal_names = []
with open(file_path, 'r') as file:
    animal_names = file.read().splitlines()

#converting the animal names in animal_library into lowercase
animal_names_lower = [name.lower() for name in animal_names]

#displaying the list of animal names
print(animal_names_lower)  