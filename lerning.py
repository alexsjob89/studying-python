

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
    