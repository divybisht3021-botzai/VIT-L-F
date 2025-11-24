from file_management import loadusers, saveuser
from data import new_user
import os

cuser = None

def register():
    users=loadusers()
    print("----REGISTER----")
    regno=input("Enter registration number (Example: 25BCE10418): ")
    
    for i in users:
        if i['regno'] == regno:
            print("Student ID already exists.")
            return
    name=input("Enter Name: ")
    passw=input("Enter Password: ")

    newuser=new_user(regno, name, passw)
    users.append(newuser)
    saveuser(users)
    print(f"{name} registered successfully.")

def login():
    global cuser
    users=loadusers()
    print("----LOGIN----")
    regno=input("Enter registration number: ")
    passw=input("Enter password: ")

    for i in users:
        if i['regno']==regno and i['password']==passw:
            cuser=i
            os.system('cls')
            print(f"Welcome {i['name']}.")
            return True
    print("Student ID does not exist.")
    return False

def get_cuser():
    return cuser

def logout():
    global cuser
    cuser=None
    print("Logged out.")

