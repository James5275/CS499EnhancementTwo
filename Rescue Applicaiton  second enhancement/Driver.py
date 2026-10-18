#James Ehrle

from Dog import dog
from Monkey import monkey

#creating a driver class
class driver:
    #setting up for the monkey species that are allowed
    monkeySpecies = ["capuchin", "guenon", "macaque", "marmoset", "tamarin", "squirrel monkey"]
    
    #saved login username 
    userName = '123'
    #saved login password
    password = '123'

    #setting up inital state of the lists and initializing them
    def __init__(self):
        # Setting up the animalList that will house all of the animals
        self.animalList = []
        #self.dogList = []
        #self.monkeyList = []
        self.initializeDogList()
        self.initializeMonkeyList()

    def initializeDogList(self):
        #initalizing the DogList that houses the current dogs
        #using extend to adding existing to the new list instead of replacing them
        self.animalList.extend([
            dog("spot", "German Shepherd", "male", "1", "25.6", "05-12-2019",
                "United States", "in service", False, "England"),
            dog("rex", "Great Dane", "male", "3", "35.2", "02-03-2020",
                "United States", "in service", False, "United States"),
            dog("bella", "Chihuahua", "female", "4", "25.6", "12-12-2019",
                "Canada", "in service", True, "Canada"),
        ])

    def initializeMonkeyList(self): 
        #initalizing the MonkeyList that houses the current monkeys
        #using extend to adding existing to the new list instead of replacing them
        self.animalList.extend([
            monkey("Bobo", "Capuchin", "22", "30", "35", "male", "4", "55",
                    "07-27-2019", "United States", "in service", False, "england"),
            monkey("George", "Macaque", "20", "26", "32", "male", "1", "54",
                    "04-27-2020", "United States", "in service", False, "United States"),
            monkey("Stella", "Marmoset", "24", "28", "36", "female", "2", "45",
                    "07-19-2021", "Canada", "In service", True, "Canada"),
        ])

    def displayMenu(self):
                print("\n\n")
                print("\t\t\t\tRescue Animal System Menu")
                print("[1] Intake a new dog")
                print("[2] Intake a new monkey")
                print("[3] Reserve an animal")
                print("[4] Print a list of all dogs")
                print("[5] Print a list of all monkeys")
                print("[6] Print a list of all animals that are not reserved")
                print("[q] Quit application")
                print()

    def getUserChoice(self):
            #defining all of the valid options
            options = ['1', '2', '3', '4', '5', '6', 'q']

            while True: 

                self.displayMenu()

                #Getting input and making it lowercase and stripped of whitespace
                choice = input("Enter a menu selection: ").strip().lower()

                if choice in options:
                    return choice
                else: 
                    print("Invalid Choice. Enter valid option")

    def intakeNewDog(self):
        name = input("What is the dog's name?").strip().lower()
        for animal in self.animalList: #changing to searching the animalList by animalType
            if animal.animalType == 'dog' and animal.name == name:
                print("\nthis dog is already in our system\n")
                updateStatus = input("Would you like to update the training status? (yes or no): ").strip().lower()
                
                if updateStatus == "yes":
                    animal.trainingStatus = input("What is the new training status?: ").strip().lower()
                    break 
                else:
                    break
        breed = input("What is " + name + "'s breed? \n").strip().lower()
        gender = input("What is " + name + "'s gender? \n").strip().lower()
        age = input("What is " + name + "'s age? \n").strip().lower()
        weight = input("What is " + name + "'s weight \n").strip().lower()
        acquisitionDate = input("What is " + name + "'s acquisition date? \n").strip().lower()
        acquisitionCountry = input("What is " + name + "'s acquisition country \n").strip().lower()
        trainingStatus = input("What is " + name + "'s training status \n").strip().lower()
    
        while True:
            booleanInput = input("Is " + name + " reserved? (true or false) \n").strip().lower()
            if booleanInput == "true":
                reserved = True
                break
            elif booleanInput == "false":
                reserved = False
                break
            else:
                print("please enter true or false for resered status \n")  
                
        inServiceCountry = input("What is " + name + "'s in service country \n")

        self.animalList.append(dog(name, breed, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus, reserved, inServiceCountry))

        print("Thank you for adding " + name)

    def intakeNewMonkey(self):
        name = input("What is the Monkey's name? \n").strip().lower()
        for animal in self.animalList: #changing to searching the animalList by animalType
            if animal.animalType == 'monkey' and animal.name == name:
                print("\nthis monkey is already in our system\n")
                updateStatus = input("Would you like to update the training status? (yes or no): ").strip().lower()
                
                if updateStatus == "yes":
                    animal.trainingStatus = input("What is the new training status?: ").strip().lower()
                    break 
                else:
                    break
        while True:
            species = input("What is " + name + "'s" + " species \n").strip().lower()
            if species in self.monkeySpecies:
                break
            else:
                print("please enter correct Species \n")

        tailLength = input("What is " + name + "'s" + " tail Length \n").strip().lower()
        height = input("What is " + name + "'s" + " height \n").strip().lower()
        bodyLength = input("What is " + name + "'s" + " body length \n").strip().lower()
        gender = input("What is " + name + "'s gender? \n").strip().lower()
        age = input("What is " + name + "'s age? \n").strip().lower()
        weight = input("What is " + name + "'s weight \n").strip().lower()
        acquisitionDate = input("What is " + name + "'s acquisition date? \n").strip().lower()
        acquisitionCountry = input("What is " + name + "'s acquisition country \n").strip().lower()
        trainingStatus = input("What is " + name + "'s training status \n").strip().lower()
    
        while True:
            booleanInput = input("Is " + name + " reserved? (true or false) \n").strip().lower()
            if booleanInput == "true":
                reserved = True
                break
            elif booleanInput == "false":
                reserved = False
                break
            else:
                print("please enter true or false for resered status \n")  
                
        inServiceCountry = input("What is " + name + "'s in service country \n")

        self.animalList.append(monkey(name, species, tailLength, height, bodyLength, gender,
                    age, weight, acquisitionDate, acquisitionCountry, trainingStatus,
                    reserved, inServiceCountry))

        print("Thank you for adding " + name)

    def reserveAnimal(self):

        while True:
            animalType = input("What animal type would you like to reserve? \n").strip().lower()

            if animalType == "dog":
                country = input("what is the service country? \n").strip().lower()
                for animal in self.animalList:
                    if (animal.inServiceCountry.lower() == country and
                        not animal.reserved and animal.trainingStatus.lower() == "in service"):
                        print(f"{animal.name} is availiable. \n")
                        while True:
                            newReserved = input("Would you like to reserve this dog? (yes or no) \n").strip().lower()
                            if newReserved == 'yes':
                                animal.reserved = True
                                print(f"You have reserved {animal.name}.")
                                break
                            elif newReserved == 'no':
                                print("Okay, Ill take you back to the main menu")
                                break
                            else:
                                print("please enter yes or no")
                    else:
                        print("No dogs matching that description")
                break


            elif animalType == "monkey":
                country = input("what is the service country? \n").strip().lower()
                for animal in self.animalList:
                    if (animal.inServiceCountry.lower() == country and
                        not animal.reserved and animal.trainingStatus.lower() == "in service"):
                        print(f"{animal.name} is availiable. \n")
                        while True:
                            newReserved = input("Would you like to reserve this dog? (yes or no) \n").strip().lower()
                            if newReserved == 'yes':
                                animal.reserved = True
                                print(f"You have reserved {animal.name}.")
                                break
                            elif newReserved == 'no':
                                print("Okay, Ill take you back to the main menu")
                                break
                            else:
                                print("please enter yes or no")
                    else:
                        print("No monkeys matching that description")
                break
                
            else:
                print("please enter a correct animal type")

    def printAnimal(self, userChoice):
        if userChoice == '4':
            print("List of all dogs:")
            for animal in self.animalList:
                if animal.animalType == 'dog':
                    print(f"{animal.name} - Training Status: {animal.trainingStatus}, "
                    f"Acquisition Country: {animal.acquisitionCountry}, "
                    f"In service location: {animal.inServiceCountry}, "
                    f"reserved: {str(animal.reserved).lower()}")
        elif userChoice == '5':
            print("List of all monkeys:")
            for animal in self.animalList:
                if animal.animalType == 'monkey':
                    print(f"{animal.name} - Training Status: {animal.trainingStatus}, "
                    f"Acquisition Country: {animal.acquisitionCountry}, "
                    f"In service location: {animal.inServiceCountry}, "
                    f"reserved: {str(animal.reserved).lower()}")
        elif userChoice == '6':
            print("List of all animials avaliable:")
            print("Monkey:")
            for animal in self.animalList:
                if animal.animalType == 'monkey':
                    if not animal.reserved:
                        print(animal.name)
            print("\nDog: ")
            for animal in self.animalList:
                if animal.animalType == 'dog':
                    if not animal.reserved:
                        print(animal.name)

    def login(self):
        print("+++++LOGIN++++++")

        #this will allow user 3 attempts to logging in 
        for trys in range(3):
            username = input('Username: ').strip()
            user_password = input('Password: ')

            if (username == self.userName and user_password == self.password):
                print ('Login successful!')
                return True

            remaining = 2 - trys

            print(f"Incorrect Usernname or Password." 
            f"You have {remaining} trys left")
        
        print("Too many failed logins, Good Bye.")
        return False

    def main(self):
            # while loop to display menu/getting user input 
            while True: 
                #getting user input
                userChoice = self.getUserChoice()

                if userChoice == '1': #Adding a New Dog
                    self.intakeNewDog()

                elif userChoice == '2': #Adding a New Monkey 
                    self.intakeNewMonkey()

                elif userChoice == '3': #Reserving an Animal
                    self.reserveAnimal()

                elif userChoice in ('4', '5', '6'): #Printing list of all dogs
                    self.printAnimal(userChoice)

                elif userChoice == 'q': #quiting the menu/program
                    print("goodbye!")
                    break 
            
            
        


if __name__ == "__main__":

    #if login comes back true it will go to main otherwise 
    #terminate the program
    if driver().login():
        driver().main()


