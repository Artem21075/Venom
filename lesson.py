def add(x, y):
    if x > 0 and y > 0:
       print("I")
    elif x < 0 and y > 0:
       print("II")
    elif x < 0 and y < 0:
        print("III")
    elif x > 0 and y < 0:
        print("IV")
#add(2,1)
#add(-2,5)
#add(-7,-3)
#add(6,-4)

def ask_password():
    a = "52"
    i = 3
    while i > 0:
        t = input("Пароль:")
        if t == a:
            print("доступ разрешен")
            return
        else:
            t -= 1
            if t > 0:
                print("неверный пароль")
        print("доступ отказан")
ask_password()