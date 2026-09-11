
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
            
    
"""
contacts = [
    {
        "name": "Alex",
        "age": 36,
        "address": "East ham"
    },
    {
        "name": "Ianos",
        "age": 30,
        "address": "Stratford"
    },
    {
        "name": "Elisa",
        "age": 28,
        "address": "Beckton"
    }
]
search = input("Enter name: ")
search_age = input("Enter age: ")


for contact in contacts:
   
   if contact["name"].lower() == search.lower():
       print("Contact found!")
       print(contact["age"], contact["address"])
"""
"""                              
class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        self.balance -= amount
        
    def show_balance(self):
        print("Owner:", self.owner)
        print("Balance:£", self.balance)
        
account = BankAccount("Alex", 1000)
account2 = BankAccount("Elisa", 300)
account3 = BankAccount("Kevin", 30)
account4 = BankAccount("Alin", 234)

account.deposit(500)

account.withdraw(200)

account.show_balance()

print(account.balance)
print(account2.balance)
print(account3.balance)
print(account4.balance)
"""
"""
class Contact:
    
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

class ContactManager:
    
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        
    def show_contact(self):
        for contact in self.contacts:
            contact.display()
            
manager = ContactManager()

contact1 = Contact(
    "Alex",
    "07345435345",
    "alex@jdsadh.com"
)

contact2 = Contact(
    "Elisa",
    "0734532345",
    "elisa@jdsadh.com"
)

manager.add_contact(contact1)
manager.add_contact(contact2)
    
manager.show_contact()
"""

"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favorite_food = input("What is your fav food?")
favorite_number = int(input("What is your fav number?"))

total_age = age + 10

print("Name:", name)
print("You are", age, "years old in", "10 years you'll be", total_age)
print("favorite food", favorite_food)
print("favorite number", favorite_number)
print("registration complete!!")
"""
"""
users1 = {"Alex", "Elisa", "Kevin", "Ecveline"}
users2 = {"Jhon", "Draid", "Kevin", "Clark"}

all_users = users1 - users2

for user in all_users:
    print(user)
"""



person = {
    "name": "Alex",
    "age": 36,
    "job": "construction"
}

person["new_job"] = "developer"

if "email" in person:
    print("email exist")
    
elif "email" not in person:
    person["email"] = "alex@fdfsd.com"

print(person, "email added!")
    
    


    







    

        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





