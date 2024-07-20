def add():
    pass

def search():
    pass

def delete():
    pass

def options():
    print("================options===============")
    print("1. ADD")
    print("2. SEARCH")
    print("3. DELETE")
    print("4. QUIT")
    print("======================================")

    choice = int(input("Option no: "))

    if choice == 1:
        add()
    elif choice == 2:
        search()
    elif choice == 3:
        delete()
    elif choice == 4:
        quit()
    else:
        print("Invlid option try again!!")

while True:
    options()