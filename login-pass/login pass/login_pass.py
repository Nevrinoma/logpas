from module1 import *
stored_login = ['adin', 'bbob2', 'tree']
stored_password = ['pop2', 'bimbus', 'central']

run = True
print(stored_login)
print(stored_password)

while run:
    print("Hello, what u want to do?\n1 >>>Sign Up\n2 >>>Sign In\n3 >>> Quit")
    choise = input("Choise >>> ")
    if choise == "1":
        signUp(stored_login,stored_password)
    elif choise == "2":
        signIn(stored_login,stored_password)
    elif choise == "3":
        run = False
    else:
        print("Try again, something wrong.")
