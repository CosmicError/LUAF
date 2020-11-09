import os
import hashlib
import time

def localRegister(username, password):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    illegalChars = ['$', '@', '/', '[', ']', '{', '}', '<', '>', '=', '+', '?', '#', '%', 
                    '^', '&', '*', '(', ')', '|', ';', ':', ',', '~', '`', '\\', "\'", '\"', '.', ' ']
    try:
        os.mkdir(__location__+os.sep()+'LA')
    except:
        pass
    if os.path.isfile(__location__+os.sep()+'LA'+username+'.txt') == False:
        inuser = hashlib.sha512(username.encode()).hexdigest()
        inpass = hashlib.sha512(password.encode()).hexdigest()
        if (len(username) <= 24 and len(username) >= 3) and (len(password) <= 40 and len(password) >= 1) and not any(x in username for x in illegalChars):
            with open(__location__+os.sep()+'LA'+str(username)+'.txt', 'w') as f:
                f.write(inuser+'\n'+inpass)
                f.close()
            return True
        else:
            return False
    else:
        return False

def localLogin(username, password):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    try:
        os.mkdir(__location__+os.sep()+'LA')
    except:
        pass
    if os.path.isfile(__location__+os.sep()+'LA'+username+'.txt') == True:
        inuser = hashlib.sha512(username.encode()).hexdigest()
        inpass = hashlib.sha512(password.encode()).hexdigest()
        outuser = open(__location__+os.sep()+'LA'+username+'.txt', 'r').readlines()[0:1]
        outpass = open(__location__+os.sep()+'LA'+username+'.txt', 'r').readlines()[1:2]
        outuser = outuser[2:len(outuser)-4]
        outpass = outpass[2:len(outpass)-2]
        if (inuser == outuser) and (inpass == outpass):
            return True
        else:
            return False
    else:
        return False
