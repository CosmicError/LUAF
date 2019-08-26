'''
LUAL or Local User Account Login
LUAL will return false if the account does not exist or the username/password is incorrect

so in your code you could do for example

if lual.login(username, password) == False:
   result of false
elif lual.login == True:
   result of true
'''

import os
import hashlib
from LUAFCONFIG import sql, encoding

class lual:
    def login(username, password):
        encryptun = hashlib.sha512(username.encode())
        encryptpn = hashlib.sha512(password.encode())
        usernl = encryptun.hexdigest()
        passwl = encryptpn.hexdigest()
        try:
            __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
            path2 = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/LA/'
            linedata1 = str(open(os.path.join(path2, username + '.txt'), 'r').readlines()[0:1])
            linedata2 = str(open(os.path.join(path2, username + '.txt'), 'r').readlines()[1:2])
        except FileNotFoundError:
            return False
        except FileExistsError:
            return True
        fuser = linedata1[2:len(linedata1)-4]
        fpass = linedata2[2:len(linedata2)-2]
        try:
            path = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/LA'
            os.mkdir(path)
        except FileExistsError:
            print('working...')
        if os.path.isfile(path + '/' + username + '.txt') == True:
            if usernl == fuser and passwl == fpass:
                print("you did it!")
                return True
            else:
                print('your username or password is incorrect')
                return False
        else:
            print('no user found')
            return False