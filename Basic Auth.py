# register
# - first name, last name, password, email
# - generate user account


# login
# - account number and password

# bank operation

# Initalizing th system
import random

database = {}


def init():

    print("Welcome to AcerBank")

    haveAccount = int(input("Do you have account with us?: 1 (yes) 2 (no) \n"))

    if (haveAccount == 1):
        login()

    elif (haveAccount == 2):
        print(register())

    else:
        print("You have selected invalid option")
        init()


def login():
    print("****** Login ******")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n"

    for accountNumber, userDetails in database.items():
        if (accountNumber == accountNumberFromUser):
            if (userDetails[3] == password)
                bank0peration(userDetails)


     print('Invalid account or password')
     login()


    def register():
        print("****** Register *******")
        email=input("What is your email address? \n")
        first_name=input("What is your first name? \n")
        last_name=input("What is your last name? \n")
        password=input("Create a password for yourself \n")

        accountNumber=generationAccountNumber()

        database[accountNumber]=[first_name, last_name, email, password]

        print("Your account has been created")
        print(" == ==== ===== ==== ===")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print(" == ==== ===== ==== ==")

        login()


    def bankOperation(user):

        print("Welcome %s %s " % (user[0], user[1]))

         selected0ption=int(input(
             "What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

            if (selected0peration == 1):
                deposit0peration()
            elif (selected0peration == 2):
                withdrawal0peration()
            elif (selected0peration == 3):
                login()
            elif (selected0ption == 4):
                exit()
            else:
                print("Invalid option selected")
                bank0peration(user)

    def withDrawal0prations():
        print("Withdrawl")

    def deposit0peration():
        print("Deposit Operations")

    def generationAccountNumber():

        print("Generating Account Number")
        return random.randrange(1111111111, 9999999999)

    def logout():
        login()

    #### ACTUAL BANKING SYSTEM #####

    init()
