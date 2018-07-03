#My first Python Program#



#5th
#Add: User will set user name and password
#User will input user name and password and the program will check
#Everything else like before


globalCounter = 0

dataStorage = {
    "userName": "",
    "userPassword": ""
    }


def userNameInput():
    print ('Input user name ')
    uName = input('')
    return uName

def userPassInput():
    print ('Input user password ')
    uPassword = input()
    return uPassword

def checkAttempts (i):
    if i > 3:
        print('You have attempted with wrong username or password too many times. Your account is temporary blocked. Try again later! ')
        quit()

def setUserCredentials():
    dataStorage["userName"] = userNameInput()
    dataStorage["userPassword"] = userPassInput()

def checkCredentials(uName, uPassword):

    global globalCounter
    
    #if correct
    if (uName == dataStorage["userName"] and uPassword == dataStorage["userPassword"]):
        print('Now you can proceed ')

    #if wrong
        
    elif (uName == dataStorage["userName"] and uPassword != dataStorage["userPassword"]):
        
        globalCounter = globalCounter + 1
        checkAttempts (globalCounter)
        
        print('You have given a wrong password ')
        uPassword = userPassInput()
        checkCredentials(uName, uPassword)
    elif (uName != dataStorage["userName"] and uPassword == dataStorage["userPassword"]):
        
        globalCounter = globalCounter + 1
        checkAttempts (globalCounter)
        
        print('You have given wrong user name ')
        uName = userNameInput()
        checkCredentials(uName, uPassword)
    elif (uName != dataStorage["userName"] and uPassword != dataStorage["userPassword"]):
        
        globalCounter = globalCounter + 1
        checkAttempts (globalCounter)
        
        print('Both your user name and password is incorrect ')
        uName = userNameInput()
        uPassword = userPassInput()
        checkCredentials(uName, uPassword)
        
    #could there be any other combinations of fails?    
    else:
        print('What'+'s'+' going on?')

setUserCredentials()
print('Now try to log in! ')
uName = userNameInput()
uPassword = userPassInput()
checkCredentials(uName, uPassword)
