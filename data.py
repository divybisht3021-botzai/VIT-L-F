import datetime

def new_user(regno, name, passw):
    return {"regno": regno, "name": name, "password": passw}

def new_item(itemid, name, desc, categ, location, finder_regno, distinct, finder_name):
    return {
        'finders_name':finder_name,
        'id':itemid,
        'name':name,
        'description':desc,
        'category':categ,
        'distinction':distinct,
        'location':location,
        'finders_regno':finder_regno,
        'status':"Open",
        'date':str(datetime.date.today()),
        'claimed_by': None,
        'claim_proof': None
    }