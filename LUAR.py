'''

ELUAR also known as Encrypted Local USer Account Registery

ELUAR will return false is the account exists, too many or too 
little characters in the username or password or if the username 
contains Illegal characters

'''

import os
import hashlib
import time

class register:
    def reguser(username, password):
        usern = hashlib.sha512(username.encode())
        passw = hashlib.sha512(password.encode())
        rname = usern.hexdigest()
        rpass = passw.hexdigest()
        try:
            path = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/LA'
            os.mkdir(path)
        except FileExistsError:
            print('working...')
        if os.path.isfile(path + '/' + username + '.txt') == False:
            if len(username) <= 24 and len(password) <= 40 and len(username) >=3 and len(password) >=1:
                IllegalChars = ['$', '@', '/', '[', ']', '{', '}', '<', '>', '=', '+', '?', '#', '%', '^', '&', '*', '(', ')', '|', ';', ':', ',', '~', '`', '\\', "\'", '\"', '.', ' ']
                if any(x in username for x in IllegalChars):
                    print('Your username cannot contain Illegal characters')
                else:
                    arfile = open(os.path.join(path, str(username) + '.txt'), 'a')
                    wrfile = open(os.path.join(path, str(username) + '.txt'), 'w')
                    wrfile.write(rname + '\n' + rpass)
                    wrfile.close()
                    time.sleep(3)
            else:
                print('your username(3-24) or password(1-40) is too long or too short')
        else:
            print('Either your username exists or it is a system error')
