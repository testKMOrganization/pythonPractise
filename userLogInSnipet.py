#My first Python Program#



#Fourth Patch#

# Checks the credentials and if wrong tells the user which input was wrong and asks for new input#

# Added: uses a data storage


dataStorage = {
    "userName": "Kabir",
    "userPassword": "1@K.P"
    }




def userNameInput():
    print ('Input user name ')
    uName = input('')
    return uName

def userPassInput():
    print ('Input user password ')
    uPassword = input()
    return uPassword

def checkCredentials(uName, uPassword):
    if (uName == dataStorage["userName"] and uPassword == dataStorage["userPassword"]):
        print('Now you can proceed ')
        
    elif (uName == dataStorage["userName"] and uPassword != dataStorage["userPassword"]):
        print('You have given a wrong password ')
        uPassword = userPassInput()
        checkCredentials(uName, uPassword)
    elif (uName != dataStorage["userName"] and uPassword == dataStorage["userPassword"]):
        print('You have given wrong user name ')
        uName = userNameInput()
        checkCredentials(uName, uPassword)
    elif (uName != dataStorage["userName"] and uPassword != dataStorage["userPassword"]):
        print('Both your user name and password is incorrect ')
        uName = userNameInput()
        uPassword = userPassInput()
        checkCredentials(uName, uPassword)
    else:
        print('What'+'s'+' going on?')


uName = userNameInput()
uPassword = userPassInput()
checkCredentials(uName, uPassword)
