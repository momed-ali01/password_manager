def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("Username:", user, "| Password:", passw)


def add():
    name = input("Account name: ")
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')


while True:
    mode = input("Would you like to add a new password or view an existing ones (view,add) press 'Q' to quit: ").lower()

    if mode == "q":
        quit()
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Mode')
        break

print('GoodBye!')
