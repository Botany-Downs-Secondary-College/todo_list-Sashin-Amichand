# Imports system module to quit the program
import sys

# The to do list 
todo_list = []
routine = "1: Add a task \n2: View List \n3: Exit"

# Asks the user what they want to do
def choices(name):
    while True:
        modeChoice = int(input("Enter a number to choose what to do {}.\n{}\n".format(name, routine)))
        try:
            if modeChoice == 1:
                addingTask()

            elif modeChoice == 2:
                print(todo_list)
            
            elif modeChoice == 3:
                sys.exit()

            else:
                print("Enter only 1, 2 or 3")

        except ValueError:
            print("Please enter a valid number")
                
# The loop to add stuff to the to do list
def addingTask():
    taskadd = input("Please enter things you need to add to the to do list. \n")
    todo_list

# What to run when the user wants to exit

# It will print the to do list


# Calls the choice and asks the persons name
name = input("What is your name? ")
print("Hello {}!".format(name))
choices(name)