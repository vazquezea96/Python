name = input("What is your name? \n")
allowedUsers = ['Eddie', 'Ed','Edd']
allowedPassword = ['passwordEddie','passwordEd','passwordEdd']
Balance = ['1000','1500','2000']

if(name in allowedUsers):
    password = input("Your password? \n")
    userID = allowedUsers.index(name)

    if(password == allowedPassword[userID]):
        
        print('Welcome %s' % name)
        import datetime as dt

        current_datetime = dt.datetime.now()

        print(current_datetime)
        print('these are the available options:')
        print('1. Withdrawl')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        print(selectedOption)

        if(selectedOption == 1):
            print('you selected %s' % selectedOption + ': Withdrawl')
            withdrawlAmt = input('How much do you want to Withdrawl?')
            print('Your cash is dispensing..Take your cash')
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption + ': Cash Deposit')
            depositAmt = input('How much would you like to deposit?')
            userBalance = allowedUsers.index(name)
            currentBalance = (Balance[userID])
            newBalance = str(currentBalance + depositAmt)
            print('Your new balance is $' + newBalance)
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption + ': Complaint')
            complaint = input('What issue would you like to report?')
            print('Thank you for contacting us.')
            
        else:
            print('Invalid Option selected, please try again')
        
    else:
        print('Password Incorrect, please try again')
        
else:
    print('Name not found, please try again')
    





