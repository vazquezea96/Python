#name = input("What is your name? \n") 
#allowedUsers = ['Eddie', 'Ed','Edd']
#allowedPassword = ['passwordEddie','passwordEd','passwordEdd']
Balance = [1000, 1500 , 2000]

import random 

database = {} 

def init():
    print("Welcome to AcerBank!")

    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) \n "))

    if(haveAccount == 1):

        login()
    elif(haveAccount == 2):

        print(register())
    else:
        print("You have selected invalid option")
        init()

def bankOperation(user):

    print("Welcome %s %s " % ( user [0], user[1] ) )
    print('these are the available options:')
    print('1. Withdrawl')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))

    print(selectedOption)

    if(selectedOption == 1):

        print('you selected %s' % selectedOption + ': Withdrawl')
        withdrawalAmt = input('How much do you want to Withdrawl? \n')
        print('Your cash is dispensing...\nPlease take your cash')
        bankOperation()

    elif(selectedOption == 2):

        print('You selected %s' % selectedOption + ': Cash Deposit')
        depositAmt = input('How much would you like to deposit? \n')
        userBalance = allowedUsers.index(name)
        currentBalance = (Balance[userID])
        newBalance = str(currentBalance = depositAmt)
        print('Your new balance is $' + newBalance)
        bankOperation()

    elif(selectedOption == 3):

        print('You selected %s' % selectedOption + ': Complaint')
        complaint = input('What issue would you like to report? \n')
        print('Thank you for contacting us.')

    elif(selectedOption == 4):

        login()

    else:
        print('Invalid option selected. Please try again.')
        bankOperation()
        
        
def register():
    print("******* Register ******")
    name = input("What is your name? \n")
    User = input("Please create a username for yourself \n")
    password = input("Please create a password \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ name, User, password ]

    print("Your account has been created")
    print("Your account number is: %d" % accountNumber) 
    print("Make sure you keep it safe")

    login()


def login():
    print("****** Login ******")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
        

    print('Invalid account or password')
    login()
    

def generationAccountNumber():

    return random.randrange(111111111,999999999)




#### ACTUAL BANKING SYSTEM ####
init() 
