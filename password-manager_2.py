def view():
    file = open('passwords.txt', 'r')
    for line in file.readlines():
        data = line.rstrip()
        user, passw = data.split("|")
        print("Username:", user, "| Password:", passw)
    file.close()


def add():
    name = input("Account name: ")
    pwd = input('Password: ')

    file = open('password.txt', 'a')
    file.write(name + '|' + pwd + '\n')
    file.close()


while True:
    mode = input("To add a new password or view an existing one, type view or add. Press Q to quit: ").lower()

    if mode == "q":
        print("GoodBye!")
        quit()
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode')
        quit()
