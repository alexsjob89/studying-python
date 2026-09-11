from manager import ContactManager

def menu():
    print()
    print("*********************")
    print("   CONTACT MANAGER   ")
    print("*********************")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contacts")
    print("4, Delete contact")
    print("Exit")
    
manager = ContactManager()

manager.load_contacts()

while True:
    menu()
    
    choice = input("Choose an option")
    
    if choice == "1":
        manager.add_contact()
        manager.save_contacts()
        
    elif choice == "2":
        manager.show_contacts()
        
    elif choice == "3":
        manager.search_contact()
        
    elif choice == "4":
        manager.delete_contact()
        manager.save_contacts()
        
    elif choice =="5":
        print("Goodbye!!")
        break
    
    else:
        print("invalid option.")
        


         
    
        
        

    