


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
    
    
    
