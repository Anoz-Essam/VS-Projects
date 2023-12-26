import shelve

contacts = {
    'name': [],
    'nums': [] 
}

def menu(choice , x, y):
    match choice:
        case 1:
            addElement(x , y)
        case 2:
            searchElement(x)
        case 3:
            viewElement()
        case 4:
            editElement(x)
        case 5:
            deleteElement(x)
        case 6:
            delAllElement(x)
        case _:
            print("Invalid Choice")

def addElement(x , y):
    if(len(str(y)) == 4):
        contacts['name'].extend([x])
        contacts['nums'].extend([y])
        cont = shelve.open('myfile.db')
        cont['name'] = contacts['name']
        cont['nums'] = contacts['nums']
        cont.close()
        print(contacts)
    else:
        print("This is invalid number")

def searchElement(x):
    if(x == 1):
        name = input("Enter Name:").lower()
        for i in range(0 , len(contacts['name']), 1):
            if(name == contacts['name'][i]):
                print(contacts['nums'][i])
    elif(x == 2):
        number = int(input("Enter Number:"))
        for i in range(0 , len(contacts['nums']), 1):
            if(number == contacts['nums'][i]):
                print(contacts['name'][i])

def viewElement():
    cont = shelve.open('myfile.db')
    contacts['name'] = cont['name'] 
    contacts['nums'] = cont['nums']
    cont.close()
    print(contacts)

def editElement(x):
    if(x == 1):
        name = str(input("Enter Name:").lower())
        for i in range(0 , len(contacts['name']), 1):
            if(name == contacts['name'][i]):
                contacts['name'][i] = str(input("Enter New Name:"))
                cont = shelve.open('myfile.db')
                cont['name'] = contacts['name']
                cont['nums'] = contacts['nums']
                cont.close()
                print(contacts)
                break    
    elif(x == 2):
        num = int(input("Enter Number:"))
        for i in range(0 , len(contacts['nums']), 1):
            if(num == contacts['nums'][i]):
                contacts['nums'][i] = int(input("Enter New 4 Digit Number:"))
                cont = shelve.open('myfile.db')
                cont['name'] = contacts['name']
                cont['nums'] = contacts['nums']
                cont.close()
                print(contacts)
                break
    else:
        print("Invalid Choice")

def deleteElement(x):
    if(x == 1):
        name = input("Enter Name:").lower()
        for i in range(0 , len(contacts['name']), 1):
            if(name == contacts['name'][i]):
                del contacts['name'][i]
                del contacts['nums'][i]
                cont = shelve.open('myfile.db')
                cont['name'] = contacts['name']
                cont['nums'] = contacts['nums']
                cont.close()
                print(contacts)
                break    
    elif(x == 2):
        num = int(input("Enter Number:"))
        for i in range(0 , len(contacts['nums']), 1):
            if(num == contacts['nums'][i]):
                del contacts['nums'][i]
                del contacts['name'][i]
                cont = shelve.open('myfile.db')
                cont['name'] = contacts['name']
                cont['nums'] = contacts['nums']
                cont.close()
                print(contacts)
                break
    else:
        print("Invalid Choice")

def delAllElement(x):
    if(x == "y" or "Y"):
        contacts.clear()
        print("{'name': [],'nums': [] }")



y = 0
print("      ====Welcome To Your Conatacts===\n\
      ================================\n\
      =========Add Contact(1)=========\n\
      ========SearchContact(2)========\n\
      ========View Contacts(3)========\n\
      ========Edit Contacts(4)========\n\
      ========Delete Contact(5)=======\n\
      ========Del All Contact(6)======\n\
      =========End Session(7)=========\n\
      ================================")
choice = int(input("(1/2/3/4/5/6/7):"))
while(choice == 1 or 2 or 3 or 4 or 5 or 6 or 7):
    if(choice == 1):
        na = input("Enter Name:").lower()
        num = int(input("Enter 4 Digit Number:"))
        menu(choice , na , num)
        choice = int(input("(1/2/3/4/5/6/7):"))
    elif(choice == 2):
        choice2 = int(input("By Name(1) or Number(2):"))
        menu(choice , choice2 ,y)
        choice = int(input("(1/2/3/4/5/6/7):"))
    elif(choice == 3):
        menu(choice,choice,y)
        choice = int(input("(1/2/3/4/5/6/7):"))
    elif(choice == 4):
        choice3 = int(input("Name(1) Or Number(2):"))
        print(contacts)
        menu(choice , choice3 , y)
        choice = int(input("(1/2/3/4/5/6/7):"))
    elif(choice == 5): 
        choice4 = int(input("By Name(1) or Number(2):"))
        menu(choice , choice4, y)
        choice = int(input("(1/2/3/4/5/6/7):"))
    elif(choice == 6):
        choice5 = str(input("Are You Sure?(y/n):"))
        menu(choice , choice5 , y)
        contacts = {'name': [],'nums': [] }
        cont = shelve.open('myfile.db')
        cont['name'] = contacts['name']
        cont['nums'] = contacts['nums']
        cont.close()
        choice = int(input("(1/2/3/4/5/6/7):"))
    elif(choice == 7):
        print("See You Next Time <3")
        break
    else:
        print("Wrong Choice!")
        choice = int(input("(1/2/3/4/5/6/7):"))