from random import *
    
def signUp(stored_login,stored_password):
    while True:
        newlogin = input("Write ur login >>> ")
        if newlogin not in stored_login:
            stored_login.append(newlogin)
            break
        else:
            print("This login is already taken, try again another one!")
    while True:
        print("You want to generate your password or write by yourself?")
        paschoice=input("1 >>> Generate\n2 >>> Wryte by myself\n")
        if paschoice == 1:
            str0=".,:;!_*-+()/#¤%&"
            str1 = '0123456789'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            str4 = str0+str1+str2+str3
            ls = list(str4)
            random.shuffle(ls)
            newpassword = ''.join([random.choice(ls) for x in range(12)])
            stored_password.append(newpassword)
            break
        elif paschoice == 2:
           while True:
               print("Your password must be at least 6 characters and include:uppercase and lowercase letters, numbers, and signs(.,:;!_*-+()/#¤%&)")
                newpassword = input("")
                numbers=0
                upper=0
                loww=0
                specs=0
                for i in newpassword:
                    if i.isupper():
                        upper+=1
                    elif i.islower():
                        loww+=1
                    elif i.isdigit():
                        numbers+=1
                    else:
                        specs+=1
                if len(newpassword)<=5:
                    print("Try again!")
                    continue
                elif numbers==0:
                    print("Try again!")
                    continue
                elif upper==0:
                    print("Try again!")
                    continue
                elif loww==0:
                    print("Try again!")
                    continue
                elif specs==0:
                    print("Try again!")
                    continue
                else:
                    stored_password.append(newpassword)
                    break















#def matchUserIdx(_login,stored_login):
#    for l in stored_login:
#        if l == _login:
#            return stored_login.index(_login)
#    return None
    
#def signIn(_login, _password,stored_login,stored_password):
#    u_idx = matchUserIdx(_login,stored_login)
#    if u_idx != None:
#        if _login != stored_login[u_idx]:
#            return False
#        if _password != stored_password[u_idx]:
#            return False
#        return True
#    return False
    
#def signUp(_login, _password,stored_login,stored_password):
#    stored_login.append(_login)
#    stored_password.append(_password)

#def rndpassword():
#    str0=".,:;!_*-+()/#¤%&"
#    str1 = '0123456789'
#    str2 = 'qwertyuiopasdfghjklzxcvbnm'
#    str3 = str2.upper()
#    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
#    str4 = str0+str1+str2+str3
#    print(str4)
#    ls = list(str4)
#    print(ls)
#    random.shuffle(ls)
#    print(ls)
#    # Извлекаем из списка 12 произвольных значений
#    psword = ''.join([random.choice(ls) for x in range(12)])
#    # Пароль готов
#    print(psword)

#def check():