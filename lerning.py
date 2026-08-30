
"""
number1 = float(input("Enter first number: "))
number2 = float(input("Enter secound number: "))

print("Addition:", number1 + number2)
print("Multiplication:", number1 * number2)
print("Subtraction:", number1 - number2)
print("Division:", number1 / number2)
print("Procentage:", number1 % number2)
"""
"""
names = ["Alex", "Elisa", "Kevin", "Even", "Ianos"]

for name in names:
    print(name)
"""

"""
shopping_list = ["Milk", "Bread", "Meat", "Eggs"]
print(shopping_list)

item = input("Enter item: ").lower()

shopping_list.append(item)
print("Item added: ")

    
for index,item in enumerate(shopping_list, start=1):
    print(index, item)



while True:
    print("\n====== SHOPPING LIST =====")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Clear shoppint list")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        print("View list")
        
    elif choice == "2":
        print("Add item")
        
    elif choice == "3":
        print("Remove item")
        
    elif choice == "4":
        print("Clear list")
        
    elif choice == "5":
        print("Goodbye!")
        
    else:
        print("Invalid option")
        """
        
"""
contacts = []

while True:
    print("\n---- CONTACT LIST ----")
    print("1- View contacts")
    print("2-Add contacts")
    print("3-Search contact")
    print("4-Delete contact")
    print("5-Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        
        if len(contacts) == 0:
            print("No contacts found.")
            
        else:
            print("\nYour contacts")
            
            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print("------------------------")
                
    elif choice == "2":
        
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        
        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        
        contacts.append(contact)
        print("Contact added")
        
        #search contact
        
    elif choice == "3":
        
        name = input("Enter name to search: ")
        found = False
        
        for contact in contacts:
            
            if contact["name"].lower() == name.lower():
                print("\nContact found!")
                print("Name", contact["name"])
                print("Phone", contact["phone"])
                print("Email", contact["email"])
                
                
                found = True
                break
            
            if found == False:
                print("Contact not found.")
                
        #delete contact
        
    elif choice == "4":
        
        name = input("Enter name to delete: ")
        found = False
        
    for contact in contacts:
        
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            
            print("Contact deleted!")
            
            found = True
            break
        
        if found == False:
            print("Contact not found.")
            
        elif choice == "5":
            print("Goodbye!!")
            break
        
        else:
            print("Invalid option!!")
            """
            
    
    
person = {
    "name": "Alex",
    "age": 36,
    "city": "London",
}


for key in person.keys():
    print(key)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





