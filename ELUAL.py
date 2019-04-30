'''
ELUAL or Encrypted Local User Account Login
ELUAL will return false if the account does not exist or the username/password is incorrect

so in your code you could do for example

if ulogin.login(username, password) == False:
   result of false
elif ulogin.login == True:
   result of true
'''

import os
from cryptography.fernet import Fernet
from ELUAFK import key

class ulogin:
    global f
    f = Fernet(key)
    def login(username, password):
      usern = username
      passw = password
      #removed the b' at the beginning of the encrypted username
      #and password and removes the last '
      try:
         __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
         path2 = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/ELA/'
         linedata1 = str(open(os.path.join(path2, username + '.txt'), 'r').readlines()[0:1])
         linedata2 = str(open(os.path.join(path2, username + '.txt'), 'r').readlines()[1:2])
      except FileNotFoundError:
         return False
      except FileExistsError:
         return True
      lineuser = str(f.decrypt(linedata1.encode()))
      linepass = str(f.decrypt(linedata2.encode()))
      fuser = lineuser[2:len(lineuser) - 1]
      fpass = linepass[2:len(linepass) - 1]
      try:
         #gets the current path and makes a folder named ELA
         path = str(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))) + '/ELA'
         os.mkdir(path)
      except FileExistsError:
         print('working...')
      if os.path.isfile(path + '/' + username + '.txt') == True:
         if usern == fuser and passw == fpass:
            print("you did it!")
            return True
         else:
            print('your username or password is incorrect')
            return False
      else:
         print('no user found')
         return False

   #clear the recorded decrypted information
      lineuser = ""
      linepass = ""
      fuser = ""
      fpass = ""
      usern = ""
      passw = ""
