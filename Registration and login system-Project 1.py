def register():
    db = open("dbb.txt", "r")
    Username = input("create username: ")
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))
    import re
    eReg = "(\w+)@((\w+\.)+(\w))"
    us = 0
    while us == 0:
        us = 0
        if re.match(eReg,Username):
            print("username criteria is satisfied")
            if Username in d:
                Username = input("username alrady exists! please enter another username: ")
                if re.match(eReg, Username):
                    print("username criteria is satisfied, please proceed for creating password!")
                    break
                else:
                    Username = input("Username criteria not met, it must be in the form of xxx@yy.ss, please enter another username: ")
                    us = 0
            else:
                print("please proceed for creating password")
                break
        else:
            Username = input("Username criteria not met, it must be in the form of xxx@yy.ss, please enter another username: ")
            us = 0

    Password = input("Create password: ")
    numerics = '0123456789'
    capital_alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_alphas = 'abcdefghijklmnopqrstuvwxyz'
    special_chars = '!@#$%^&*()-_+=:;{}[]|\?<>,.?`~'
    sum = 0; w = 0; x = 0; y = 0; z = 0

    while sum != 4:
        while len(Password) < 5 or len(Password) > 16:
            Password = input("password is too short or too long,it must contain 5 to 16 characters.Please enter another password: ")

        for i in range(len(Password)):
            if Password[i] in numerics:
                w = 1
            elif Password[i] in capital_alphas:
                x = 1
            elif Password[i] in small_alphas:
                y = 1
            elif Password[i] in special_chars:
                z = 1
        sum = w + x + y + z
        if sum != 4:
            Password = input("Password criteria is not met, it must have minimum one special character,one digit, one uppercase, one lowercase.Please enter another password: ")
            w = 0; x = 0; y = 0; z = 0; sum = 0
        else:
            print("Password criteria met and it is accepted.")

    if Username not in d:
        db = open("dbb.txt", "a")
        db.write(Username + ", " + Password + "\n")
        print("Registration successful! Thank you for registering.")


def login():
    db = open("dbb.txt", "r")
    Username = input("Enter your username: ")
    Password = input("Enter your password: ")

    if not len(Username or Password) < 1:
        d = []
        f = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[Username]:
                try:
                    if Password == data[Username]:
                        print("Login successful")
                        print("Hi!,", Username,", Thank you for logging in")
                    else:
                        print("password is not correct, please choose Forget password or try to login again")
                        home()
                except:
                    print("Incorrect password of the username")
            else:
                print("username doesn't exist")
        except:
            print("username or password doesn't exist, please choose your option required option again!")
            home()
    else:
        print("Please enter a value")


def forgetpass():
    db = open("dbb.txt", "r")
    Username = input("Enter your username: ")
    d = []
    f = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if Username in d:
        originalpass = data[Username]
        print("Your password is: " + originalpass)
        print("please login now")
        login()
    else:
        print("username doesn't exist, please enter your required option again!")
        home()


def home(option = None):
    option = input("Login | Register | Forget password: ")
    if option == "Login":
        login()
    elif option == "Register":
        register()
    elif option == "Forget password":
        forgetpass()
    else:
        print("please enter correct option 'Login' or 'Register' or 'Forget password'.")
        home()


home()
