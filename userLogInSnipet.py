#My first Python Program#

#Takes user input and checks conditions and then proceeds#
#Does the similar actions such as the previous commit but using functions#

#User name and user password now declared as global#
userName = 'Kabir'
userPassword = '1@K.P'



def userNameInput():
    print ('Input user name ')
    uName = input('')
    return uName
def userPassInput():
    print ('Input user password ')
    uPassword = input()
    return uPassword

def checkCredentials(uName, uPassword):
    if (uName == userName and uPassword == userPassword):
        print('Now you can proceed ')
    else:
        print('Who the hell are you?')


uName = userNameInput()
uPassword = userPassInput()
checkCredentials(uName, uPassword)
