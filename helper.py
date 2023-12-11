import os, json


# opens and reads the json file
def read_animals(my_data_file):
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
            return json.loads(json_string)
    except:
        return []


# prints the animals list
def print_func(animals):
    os.system('cls')
    for animal in animals:
        print(f"ID: {animal['ID']}, Name: {animal['Name']}, Species: {animal['Species']}, Age: {animal['Age']}")
        print("-----------------------------------")


# adds new animals to the list with ID
def add_func(animals):
    os.system('cls')
    # goes through 3 inputs for name/species/age
    name = input("Enter name: ")
    species = input("Enter species: ")
    age = input("Enter age: ")
    # ensures that IDs are not duplicated, adds +1 to the max ID
    new_id = max([animal["ID"] for animal in animals], default=0) + 1 
    # adds the new animal to the list
    animals.append({"ID": new_id, "Name": name, "Species": species, "Age": age})
    print(f"Added animal with ID {new_id}")


# exits the program with an option to save
def exit_func(animals, my_data_file):
    os.system('cls')
    inputAnimal = input("Do you want to save? (y/n)")
    if inputAnimal == "y":
        #write list to file
        json_string = json.dumps(animals)
        # save the list in a file
        with open(my_data_file, 'w') as file:
            file.write(json_string)
        print("Saving and Exiting..")
        exit()
    elif inputAnimal == "n":
        print("Exiting..")
        exit()
    else:
        print("invalid input")



# deletes a animal from the animals list by ID
def del_func(animals):
    os.system('cls')
    print_func(animals)
    input_id = input("Enter ID to delete or -1 to cancel: ")

    ids = [animal["ID"] for animal in animals]
    # checks if the input ID is in the list of IDs
    if int(input_id) in ids:
        # uses input ID to delete the entry
        animals[:] = [animal for animal in animals if animal["ID"] != int(input_id)]
        print(f"Deleted animal with ID {input_id}")
    else:
        print(f"Unable to delete animal with ID {input_id}: Not in the list.")



# searches for an animal in the animals list by ID
def search_func(animals):
    os.system('cls')
    input_id = input("Enter ID to search: ")
    # gets all the IDs
    ids = [animal["ID"] for animal in animals] 
    print("Total IDs: ",ids) # debug
    # checks if the input ID is in the list of IDs
    if int(input_id) in ids:
        # find the animal with the specific ID
        found_animal = next(animal for animal in animals if animal["ID"] == int(input_id))

        # prints the rest of the entry without the ID
        print(f"Animal with ID {input_id} found:")
        for key, value in found_animal.items():
            if key != "ID":
                print(f"{key}: {value}")
    else:
        print(f"Animal with ID {input_id} is not in the list.")




