from random import *
    
def signUp(stored_login,stored_password):
    while True:
        newlogin = input("Write ur login >>> ")
        if newlogin not in stored_login:
            stored_login.append(newlogin)
            print(stored_login)
            print(stored_password)
            break
        else:
            print("This login is already taken, try again another one!")
    while True:
        print("You want to generate your password or write by yourself?")
        paschoice=input("1 >>> Generate\n2 >>> Wryte by myself\n")
        if paschoice == "1":
            str0=".,:;!_*-+()/#¤%&"
            str1 = '0123456789'
            str2 = 'qwertyuiopasdfghjklzxcvbnm'
            str3 = str2.upper()
            str4 = str0+str1+str2+str3
            ls = list(str4)
            shuffle(ls)
            newpassword = ''.join([choice(ls) for x in range(12)])
            stored_password.append(newpassword)
            print(stored_login)
            print(stored_password)
            break
        elif paschoice == "2":
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
                    print(stored_login)
                    print(stored_password)
                    break



def signIn(stored_login,stored_password):

    passwordtry = 0
    login = input("Enter your login >>> ")
    while True:
        password = input("Enter your password >>> ")
        if password not in stored_password:
            passwordtry +=1
            print(f"Wrong password, you have {3-passwordtry} attemps more!")
        if passwordtry == 3:
            print("No more attemps u have! t_t")
            break

        if login in stored_login and password in stored_password and stored_login.index(login) == stored_password.index(password):
            print("Welcome back!")
            break

