'''

ELUAR also known as Encrypted Local USer Account Registery

ELUAR will return false is the account exists, too many or too 
little characters in the username or password or if the username 
contains Illegal characters

-- Info --
Started 3/5/2019
Finished Alpha - 3/19/2019
Finished Beta - 3/27/2019
Last Updated - 7/25/19
Current Version - v2
Stability - Stable
Supported Python Versions - 3.5.x
                            3.6.x
                            3.7.x

-- Known Bugs --
1a) LUAR creating FileNotFounError
1b) LUAR creating FileExistsError

-- Bug Reasons --
1a) gives error because the program is creating the account registered
1b) give error because the program has found the file as an existing account


-- Bugs Good or Bad? --
1a - Good (Supposed to)
1b - Good (Supposed to)

'''



import os
import hashlib
import time

class register:
    def reguser(username, password):
        #encrypts the username and password
        usern = hashlib.sha512(username.encode())
        passw = hashlib.sha512(password.encode())
        rname = usern.hexdigest()
        rpass = passw.hexdigest()
        try:
            #gets the current path and makes a folder named LA
            path = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/ELA'
            os.mkdir(path)
        except FileExistsError:
            print('working...')
        if os.path.isfile(path + '/' + username + '.txt') == False:
            if len(username) <= 24 and len(password) <= 40 and len(username) >=3 and len(password) >=1:
            #checks if username and password do not exceed the stated maximum and minimum
                IllegalChars = ['$', '@', '/', '[', ']', '{', '}', '<', '>', '=', '+', '?', '#', '%', '^', '&', '*', '(', ')', '|', ';', ':', ',', '~', '`', '\\', "\'", '\"', '.', ' ']
                if any(x in username for x in IllegalChars):
                    #checks that the username does not have any illegal characters
                    print('Your username cannot contain Illegal characters')
                else:
                    #if everything is true or passes then it will create the account
                    arfile = open(os.path.join(path, str(username) + '.txt'), 'a')
                    wrfile = open(os.path.join(path, str(username) + '.txt'), 'w')
                    wrfile.write(rname + '\n' + rpass)
                    wrfile.close()
                    time.sleep(3)
            else:
                print('your username(3-24) or password(1-40) is too long or too short')
        else:
            print('Either your username exists or it is a system error')
            
            
            
            
