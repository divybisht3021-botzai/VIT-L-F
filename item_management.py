from file_management import loaditems, saveitem
from difflib import SequenceMatcher
from data import new_item
import authentication as au
import os

def reportitem():
    items=loaditems()
    user=au.get_cuser()

    print("----REPORT ITEM----")
    fname=input("Finder's Name (Firstname only): ").strip().lower()
    name=input("Item Name: ")
    desc=input("Description: ")
    distinct=input("Describe any distinctions (if any): ")
    categ=input("Category (Electronics/others): ")
    location=input("Location found: ")

    newid=len(items)+1
    newitem=new_item(newid, name, desc, categ, location, user['regno'],distinct, fname)
    
    items.append(newitem)
    saveitem(items)
    os.system('cls')
    print(f"Item successfully reported. ID: {newid}")

def allitems():
    items=loaditems()
    print(f"{'-'*40}ALL LOST ITEMS{'-'*40}")
    print(f"{'Item ID':<15} {'Name':<20} {'Location (Room no. if any)':<30} {'Status':<10} {'Date Reported':<20}")
    print('-'*95)

    found=False
    for i in items:
        if i['status']=='Open':
            print(f"{i['id']:<15} {i['name']:<20} {i['location']:<30} {i['status']:<10} {i['date']:<20}")
            found=True
    if not found:
        print("No unclaimed/lost items found")
    print('-'*95)

def claimitem():
    items=loaditems()
    proof=""
    allitems()

    try:
        itemid=int(input("Enter item ID (0 to go back): "))
    except ValueError:
        print("Invalid item ID")
        return
    if itemid==0:
        return
    
    for i in items:
        if i['id']==itemid:
            if i['status']=='Claimed':
                print("Item already claimed")
                return
            print('-'*95)
            print(f"Verify details to claim ({i['name']}, ID: {i['id']})")
            distinction = i.get('distinction', "").lower()  
            if not distinction:
                print("No distinction was set for this item by the finder.")
                similarity=1
            else:
                proof = input(f"Describe distinctions of the item: ").lower()
                similarity = SequenceMatcher(None, distinction, proof).ratio()
            if distinction in proof or similarity > 0.3:
                i['status'] = 'Claimed'
                i['claimed_by'] = f"{au.get_cuser()['name']}.{au.get_cuser()['regno']}@vitbhopal.ac.in"
                i['claim_proof'] = proof
                saveitem(items)
                print("Ownership verified.")
                print(f"Please contact ({i['finders_name']}.{i['finders_regno']}@vitbhopal.ac.in) to collect your item.")
                return
            else:
                print(f"Verification Failed. Your description did not match with the finder's.")
            return
    print("Item ID not found.")

