#My first Python Program#

#Takes user input and checks conditions and then proceeds#
#Does the similar actions such as the previous commit but using functions#

userName = 'Kabir'
userPassword = '1@K.P'

print ('Input user name ')
uName = input('')
print ('Input user password ')
uPassword = input()

if (uName == userName and uPassword == userPassword):
    print('Now you can proceed ')
else:
   print('Who the hell are you?')
