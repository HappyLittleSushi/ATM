import os
import sys
from getpass import getpass

userList = []

userList.append({"userID": "00123", "userPin": "1234", "userBalance": "5000", "overdraft": True})
userList.append({"userID": "00234", "userPin": "2345", "userBalance": "499" , "overdraft": False})
userList.append({"userID": "00345", "userPin": "3456", "userBalance": "25", "overdraft": True})


def loginOrRegister():
    print("Please select from the following:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    
    print("Please choose an option (1-3): ")
    choice = readUserInputInteger(3, 1)
    if type(choice) != int:
        loginOrRegister()
    else:
        return choice


def login():
    print("Please input your User ID and User Pin.")
    userId = input("User ID: ")
    userPin = getpass("User Pin: ")
    
    userFound = False
    for user in userList:
      if user["userID"] == userId:
          userFound = True
          if user["userPin"] != userPin:
              print ("Pin for user", userId, "is incorrect, please try again...")
              login()
          else:
              print("Login Successful!")
              currentUser = user["userID"]
              showMenu(currentUser)
    if not userFound:
      print("User", userId, "not found on system.")
      login()     


def registerUser():
    print("Please input User ID and User Pin to register.")
    userId = input("User ID: ") 
    for user in userList:
        if user["userID"] == userId:
            print("User ID already exists. Please use a different one")   
                
    userPin = input("User Pin: ")
    userList.append({'userID': userId, 'userPin': userPin, 'userBalance': "0"})
    
    print("Registration Succesful! Please login into your account.")
    login()
    
    
def readUserInputInteger(maxNumber, minNumber):
    choice = int(input("Enter your choice here: "))
    if type (choice) != int:
        print ("Choice is an invalid type, please use integers...\n")
    elif choice < minNumber and choice > maxNumber:
        print ("Choice", choice, "is out of range, choose again...")
    else:
        return choice


def clearScreen():
    os.system('cls')


def showMenu(currentUser):
    clearScreen()
   
    print("Menu options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Statement")
    print("4. Change Pin")
    print("5. Exit\n")

    print("Please choose an option (1-5): ")
    choice = readUserInputInteger(5, 1)
    if type(choice) != int:
        showMenu()
    else:
        menuSelection(choice, currentUser)

def menuSelection(choice, currentUser):
    if (choice == 1):
        print("You have selected Deposit.\n")
        input("Return to continue...")
    elif(choice == 2):
        print("You have selected Withdraw.\n")
        input("Return to continue...")
    elif(choice == 3):
        displayStatement(currentUser)
        input("Return to continue...")
    elif(choice == 4):
        print("You selected Change Pin\n")
        input("Return to continue...")
    elif(choice == 5):
        print("Exiting the application, goodbye...")
        sys.exit() 

def deposit():
    print("")

  
def withdraw():
    print("")  
  
    
def displayStatement(currentUser):
    print("Statement:")
    print("============================================================")
    print(f"userID".ljust(20), "userBalance".ljust(20), "Overdraft ") 
    print("============================================================")
    
    for user in userList:
        if user["userID"] == currentUser:
            print(f"{user['userID'].ljust(20)} {user['userBalance'].ljust(20)} {str(user['overdraft'])}\n")

def changePin():
    print("")  
      

def main():
    choice = loginOrRegister()
    if choice == 1:
        login()
    elif choice == 2:
        registerUser()
    else:
        print ("Exiting the application, goodbye...")
        sys.exit()
        

if __name__ == "__main__":
    main()
