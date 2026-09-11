import json

from contact import Contact

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print("Contact added!!")
        
    def show_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        
        for contact in self.contacts:
            contact.display()
            print("-----------------")
            
    def search_contact(self):
        name = input("Enter name to search: ")
        
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.display()
                return
            
        print("Contact not found.")
        
    def delete_contact(self):
        name = input("Enter name to delete: ")

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted!")
                return

        print("Contact not found.")
        
    def save_contacts(self):
        data = []
        
        for contact in self.contacts:
            data.append({
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email
            })
            
        with open("contact.json", "w") as file:
            json.dump(data, file, indent=4)
        
    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file: data = json.load(file)
            
            for item in data:
                contact = Contact(
                    item["name"],
                    item["phone"],
                    item["email"]
                )
                
                self.contacts.append(contact)
                
        except FileNotFoundError:
            self.contacts = []
    