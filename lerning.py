

"""
# quiz game

# questions

questions = [
    {
        "question": "waht is the capital of France",
        "options": ["A. London", "B. Paris", "C. Madrid", "D. Rome"],
        "answer": "B"
    },
    {
        "question": "Which language are we using?",
        "options": ["A. Java", "B. C++", "C. Python", "D. PHP"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 5?",
        "options": ["A. 8", "B. 10", "C. 15", "D. 23"],
        "answer": "B"
    }
]

# score
score = 0

for question in questions:
    
    print("\n" + question["question"])
    
    for option in question["options"]:
        print(option)
        
    answer = input("Your answer: ").upper()
    
    if answer == question["answer"]:
        print("Correct!")
        score += 1
    
    else:
        print("Wrong!")
        print("Correct anwer:", question["nswer"])
        
print("\nQuiz finished!")
print(f"Your score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"you scored {percentage:.0f}%")
    """
    
# contact book begginer project
"""
contact = {
    "name": "Alex",
    "phone": "07412984283",
    "email": "alex@example.com"
}


contacts = []

while True:
    print("\n---- CONTACT book -----")
    print("---------------------")
    print("| 1. Add Contact    |")
    print("| 2. View Contacts  |")
    print("| 3. Search Contact |")
    print("| 4. Delete Contact |")
    print("| 5. Exit           |")
    print("---------------------")
   
    choice = input("Choose an option: ") 
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })
    
        print("Contact added!")
    
    elif choice == "2":
        for contact in contacts:
            print(
                contact["name"],
                contact["phone"],
                contact["email"]
            )
            
    elif choice == "3":
        name = input("Search name: ")
        
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                     print(contact)
                     
    elif choice == "4":
        name = input("Name to delete: ")
        
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted!")
                break
            
    elif choice == "5":
        print("Goodbye!!")
        break
    
    else:
        print("Invalid option")
"""



class BankAccount:
    def __init__(self, name, account_number, pin):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = 0
        self.transitions = []
        
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be greater than £0.")
            return 
        
        self.balance += amount
        
        self.transition.append(
            f"Deposited: £{amount:.2f}"
        )
        
        print(f"{amount:.2f} deposited successfully.")
        
    