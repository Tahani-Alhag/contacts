import json

print("-------------------------------------------------")
print("                YOUR CONTACT LIST")
print("-------------------------------------------------")



def add_data():
    id =input("Enter id :")
    name =input("Enter Name :")
    phone =input("Enter Phone Number :")
    email =input("Enter Phone Email :")

    dic = {
        "id : " : id ,
        "Name : " : name ,
        "Phone Number : " : phone ,
        "Email : " : email
    }
    
    with open("contacts.json" , "r") as getdata :
        data = json.load(getdata)  # convert json to python

        data[id] = dic

        with open("contacts.json" , "w") as save :
            json.dump(data, save) # convert python to json
            print("Successfully Added")


def view_data():
    with open("contacts.json" , "r") as view :
        data = json.load(view) 

        for i,m in data.items():
            for x,n in m.items():
                print(x,n)
            print("\n")    


def delete_data():
    id = input("Enter id : ")

    with open("contacts.json" , "r") as getdata :
        data = json.load(getdata) 

        if id in data:
            data.pop(id)

            with open("contacts.json" , "w") as delete :
                detal = json.dump(data, delete)
            print("Successfully Deleted")


def update_data():
    id = input("Enter id : ")

    with open("contacts.json" , "r") as getdata :
        data = json.load(getdata) 

        if id in data:
            name =input("Enter New Name :")
            phone =input("Enter New Phone Number :")
            email =input("Enter New Phone Email :")

            dic = {
                "id : " : id ,
                "Name : " : name ,
                "Phone Number : " : phone ,
                "Email : " : email
            }

            data[id] = dic

            with open("contacts.json" , "w") as update :
                json.dump(data, update)
                print("Successfully Update")


def search_data():
    id = input("Enter id : ")
    
    with open("contacts.json" , "r") as getdata :
        data = json.load(getdata)
    
        if id in data:
            for i,m in data.items():
                if i==id:   
                    for x,n in m.items():
                        print(x,n)
                


def main():
    print("\n 1. Add Data")
    print("\n 2. View Data")
    print("\n 3. Delete Data")
    print("\n 4. Update Data")
    print("\n 5. Search Data")
    print("\n 6. Exit")
    print("-------------------------------------------------")

    enter = int(input("\n Enter Choise  : "))
    
    if enter == 1:
        add_data()
        main()
    elif enter == 2:
        view_data()
        main()
    elif enter == 3:
        delete_data() 
        main()
    elif enter == 4:
        update_data()
        main()
    elif enter == 5:
        search_data()
        main()
    else:
        print("THANK YOU ! AND COME AGAIN")


main()

 
