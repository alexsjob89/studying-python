

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
    
    # Python Quiz Game — Version 2
    
import random

questions = {
    "easy": [
        {
            "question": "what is correct way to print Hello?",
            "options": ["print('Hello')", "echo('Hello')", "console.log('Hello')", "printf('Hello')"],
            "answer": "print('Hello)"
        },
        {
            "question": "What type of data is 25?",
            "options": ["str", "int", "list", "bool"],
            "answer": "int"
        },
        {
            "question": "Which symbul is used for comments in Python?",
            "options": ["//", "#", "/", "bool--"],
            "answer": "#" 
        }
    ],
    
    "medium": [
        {
            "question": "Which methon adds an item at the of a list?",
            "options": ["add()", "insert()", "append()", "push()"],
            "answer": "append()"
        },
        {
            "question": "What does lne([10, 20, 30]) return?",
            "options": ["2", "3", "10", "30"],
            "answer": "3"
        },
        
        [
            "question": "Which kyeword is used to create a function?",
            "options": ["function", "func", "def", "create"],
            "answer": "def"
        ]
    ],
    
    "hard": [
        {
            "question": "What does [x * 2 for x in range(3)] produce?",
            "options": ["[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]", "[1, 2, 3]"],
            "answer": "[0, 2, 4]"
        },
        {
            "question": "What does a Python dictionary store?",
            "options": [
                "Only numbers",
                "Key-value pairs",
                "Only strings",
                "Only lists" 
    ],
    "answer": "Key-value pairs"
        },
{
            "question": "What does == do in Python?",
            "options": [
                "Assigns a value",
                "Checks equality",
                "Checks inequality",
                "Creates a variable"
            ],
            "answer": "Checks equality"
        }
    ]
}

def choose_difficulty():
    print("\nchoose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3.Hard")
    
    choice = input("choose: ")
    
    difficulties = {
        "1": "easy",
        "2": "medium",
        "3": "hard"
    }
    
    return difficulties.get(choice, "easy")

def ask_question(question, number):
    print(f"\nQuestion {number}:")
    print(question["question"])
    
    # randomize answers
    options = question["options"].copy
    random.shuffle(options)
    
    for index, option in enumerate(option, start=1):
        print(f"{index}, {option}")
        
    while True:
        try:
            answer = int(input("Your answer: "))
            
            if 1 <= answer <= len(option):
                break
            
            print("Pleasec choose a val;id number.")
            
        except ValueError:
            print("Please enter a number.")
            
    selected_answer = option[answer - 1]
    
    if selected_answer == question["answer"]:
        print("/ Correct!")
        return True
    else:
        print("X Wrong!")
        print(f"Correct answer: {question['answer']}")
        return False
    
def play_game():
    print(f"\n|===========================|")
    print("   |    PYTHON QUIZ GAME       |")
    print("   |===========================|")
    
    difficulty = choose_difficulty()
    
    question_list = questions[difficulty].copy()
    
    random.shuffle(question_list)
    
    score = 0
    
    for number, question in enumerate(question_list, start=1):
        
        if ask_question(question, number):
            score += 1
            
    total = len(question_list)
    percentage = (score / total) * 100
    
    print("\n|=====================|")
    print("  |    QUIZ FINISHED    |")
    PRINT("  |=====================|")
    
    print(F"Score: {score}/{total}")                          
    print(F"Pecentage: {percentage:.0f}%")
    
    if percentage == 100:
        print("🏆 Perfect score!")
    elif percentage >= 70:
        print("🎉 Great job!")
    elif percentage >= 50:
        print("👍 Good effort!")
    else:
        print("📚 Keep practicing!")
        
def main():
    
    while True:
        
        play_game()
        
        print("\nWould you like to play again?")
        choice = input("yes/no: ".lower())
        
        if choice != "yes":
            print("\nThanks for playing!")
            break
        
main()                      