import authentication as au
import item_management as im
import os

exit=False
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        f.write('[]')
if not os.path.exists('items.json'):
    with open('items.json', 'w') as f:
        f.write('[]')

while not exit:
    user=au.get_cuser()

    if not user:
        print("----VIT Lost & Found----")
        print("""1. Login\n2. Register\n3. Exit""")
        choice=input("Select: ")

        if choice == '1':
            os.system('cls')
            au.login()
        elif choice == '2':
            os.system('cls')
            au.register()
        elif choice == '3':
            exit=True
        else:
            print("Invalid selection.")
    else:
        print(f"----DASHBOARD ({user['name']}, {user['regno']})----")
        print("""1. Report Item\n2. Claim Item\n3. Logout""")
        choice = input("Select: ")

        if choice == '1':
            os.system('cls')
            im.reportitem()
        elif choice == '2':
            os.system('cls')
            im.claimitem()
        elif choice == '3':
            os.system('cls')
            au.logout()
        else:
            print("Invalid selection.")
