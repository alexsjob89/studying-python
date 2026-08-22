"""
number = 7

if number % 4 == 1:
    print("The number is divisible by 4.")
else:
    print("The number is not divisible by 4.")
"""
"""
temperature = 40

if temperature >= 30:
    print("It's a hot day.")
elif temperature > 20:
    print("It's a nice day.")
elif temperature > 10:
    print("It's a bit chilly.")
else:
    print("It's cold outside.")
"""

username = "Alex"

"""
if len(username) > 0:
    print(f"Welcone, {username}!")
else:
    print(f"Error: Username {username} cannot be found!")
"""
"""
a = 410
b = 512

print("a") if a < b else print("b") if a > b else print("b")
"""
"""
x = 15
y = 23
max_value = x if x > y else y
print("The maximum value is:", max_value)
"""
"""
user_name = ""
name = "Alex"
surname = "Dorultan"

display_name = user_name if user_name else f"{name} {surname}"
print("Welcome,", display_name)
"""
"""
temperature = 25
is_raining = True
is_weekend = True

if (temperature < 20 and is_raining) or is_weekend:
    print("Great day for outdoor activities!!")
"""
"""
user_name = "Alex"
password = "123456"
is_veified = False

if user_name and password and is_veified:
    print("You're logged in!!")
else:
    print("Error: Invalid credentials or account not verified.")
"""
"""
score = 23

if score >= 0 and score <= 15:
    print("Valid score")
else:
    print("Invalid score")
"""

"""
age = 20
has_license = False

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license to drive")
else:
    print("You are too young to drive")
"""

"""
score = 34
attendance = 65
submitted = False

if score >= 65:
    if attendance >= 86:
        if submitted:
            print("Pass with good standing")
    else:
       print("Pass but misiing assigment")
else:
       print("Pass but low attendance")
"""
"""
temperature = 23
is_sunny = True

if temperature < 34 and is_sunny:
    print("It's hot sunny day!!")
else:
    print("it's either too hot or not sunny")
"""

"""
score = 70
extra_credit = 6

if score >= 90:
    if extra_credit >= 0:
        print("You got an A+")
    else:
        print("You got an A grade")
elif score >= 80:
    print("You got a B grade")
else:
    print("You got a C grade")
"""

"""
day = 8
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
"""

"""
day = 5
match day:
    case 2:
        print("Today is Tuesday evening")
    case 3:
        print("Today is Wednesday evening")
    case _:
        print("Looking forward to the weekend!!")
"""

"""
day = 2
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is weekday!!")
    case 6 | 7:
        print("Today is weekends!!")
"""
"""
month = 1
day = 3
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 1:
        print("A day in January")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A day in May")
    case _:
        print("No match")
"""
"""
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]
for x in fruits:
    print(x)
    if x == "Cherry":
        continue
"""

"""
for x in range(23):
    print(x)
else:
    print("LFinally finished!!")
"""
"""
adj = ["red", "big", "tasty", "sweet", "unny"]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for x in adj:
    for y in fruits:
        print(x, y)
"""
"""
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)
"""
"""
name = "Dorultan"
surname = "Alex"
place = "London"
born = 1989

personal_details = str(surname) + " " + str(name) + " " + str(place) + " " + str(born)

def my_names(personal_details):
    print("hello, my name is", personal_details)

my_names(personal_details)
"""
"""
my_fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
textures = ["Smooth", "Soft", "Juicy"]
def my_function(fruits):
    for x in my_fruits:
        for y in textures:
            print(y, x)
        

my_function(my_fruits)
"""
"""
name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

print("\n------ REPORT CARD ------")
print("Student :", name)

print("\nMarks")
for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}")

print("-------------------------")
print("Total   :", total)
print("Average :", round(average, 2))
print("Highest :", highest)
print("Lowest  :", lowest)
print("Grade   :", grade)
print("Result  :", result)
"""
"""
products = {
    "Apple": 1.5,
    "Banana": 0.8,
    "Orange": 2.0,
    "Bread": 3.0,
    "Milk": 4.5
}

cart = []

cart.append("Apple")
cart.append("Milk")

print("\n------ PRODUCTS ------")

for product, price in products.items():
    print(f"{product.title():10} £{price:.2f}")



while True:

    print("\n------ SHOPPING CART ------")
    print("1. View products")
    print("2. Add products")
    print("3. View cart")
    print("4. Remove products")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        print("\n-----PRODUCTS-----")

        for product, price in products.items():
            print(f"{product.title():10} £{price:.2f}")

    elif choice == "2":

        product = input("Enter product name: ").lower()

        if product in products:
            cart.append(product)
            print(f"{product.title()} added to cart.") 

        else:
            print("Product not found.")   

    elif choice == "3":

        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            print("\n-----Your cart-----")

            total = 0

            for index, product in enumerate(cart, start=1):
                price = products[product]
                total += price

                print(f"{index}. {product.title():10} £{price:.2f}")

            print("---------------------")
            print(f"Total: £{total:.2f}")

            enumerate(cart, start=1)

    elif choice == "4":
        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            print("\n-----YOUR CART-----")

            for index, product in enumerate(cart, start=1):
                print(f"{index}. {product.title()}")

            number = int(input("Enter item number to remove: "))

            if 1 <= number <= len(cart):    
                removed = cart.pop(number - 1)
                print(f"{removed.title()} removed from cart.")

    elif choice == "5":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:

            prices = []

            for product in cart:
                prices.append(products[product])

            total = sum(prices)

            print("\n-----CHECKOUT-----")

            for product in cart:
                print(f"{product.title():10} £{products[product]:.2f}")

            print("-------------------")
            print(f"Total: {product.total:.2f}")

            print("Thank you for shopping!")

            cart.clear()
"""
"""
                   #CALCULATOR PROJECT
#GET THE NUMBERS

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#GET THE OPERATOR

operator = input("Enter operator (+, -, *, /): ")

#PERFORM THE CALCULATOR

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

else:
    print("Invalid operator")

    print("Result", result)
"""

"""
#number guessing game

import random

secret_number = random.randint(1, 100)

guess = int(input("Guess the number: "))

if guess < secret_number:
    print("Too low!")

elif guess > secret_number:
    print("Too high!")

else:
    print("Correct")


while True:

    guess = int(input("Guess a number between 1 and 100: "))

    attempts += 1

    if guess < secret_number:
      print("Too low!")

    elif guess > secret_number:
      print("Too high!")

    else:
      print("Bravo!!")
      print(f"You guess it in {attempts} attempts.")
      break
"""


"""
import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

while True:
    print("\n==== ROCK PAPER SCISSORS ===")
    print("Player:", player_score)
    print("Computer:", computer_score)

    player = input("\nChoose rock, paper or scissors (or 'quit' to exit): ").lower()

    if player == "quit":
        break

    if player not in choices:
        print("invalid choice!")
        continue

    computer = random.choice(choices)

    print("You chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        print("draw!")

    elif (
        player == "rock" and computer == "scissors"
    ) or (
        player == "paper" and computer == "rock"
    ) or (
        player == "scissors" and computer == "paper"
    ):
        print("You win!!")
        player_score += 1

    else:
        print("computer win!!")
        computer_score += 1

print("\n==== FINAL SCORE ===")
print("Player:", player_score)
print("Computer:", computer_score)
"""
"""
def celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9


print("Temperature Converter")
print("1. Celsius -> Fahrenheit")
print("2. Fahrenheit -> Celsius")

choice = input("Chose an option: ")

try:
    temperature = float(input("Enter temperature: "))
    
    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}C = {result:.2f}F")
        
    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}F = {result:.2f}C")
        
    else:
        print("Invalid choice.")
        
except ValueError:
    print("Please enter a valid number.")
"""

"""
#simple to-do list

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks yet.")
        return
    
    print("\nYour Tasks: ")
    for index, task in enumerate(tasks, start=1):
        status = "/" if task["completed"] else " "
        print(f"{index}. [{status}] {task["name"]}")
        
def add_task():
    name = input("Enter a task: ")
    
    tasks.append({
        "name": name,
        "completed": False
    })

    print("Task added!")
    
def complete_task():
    show_tasks()
    
    if not tasks:
        return
    
    number = int(input("Enter the number to complete: "))

    if 1 <= number <= len(tasks):
        tasks[number - 1]["completed"] = True
        print("Task completed!")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    
    if not tasks:
        return
    
    number = int(input("Enter task number to delete: "))
    
    if 1 <= number <= len(tasks):
        deleted = tasks.pop(number - 1)
        print(f"Deleted: {deleted}")
    else:
        print("Invalid task number.")
        
while True:
    print("\n---- TO-DO LIST ----")
    print("1. Add task")
    print("2. View task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_task()
    
    elif choice == "2":
        show_tasks()
    
    elif choice == "3":
        complete_task()
    
    elif choice == "4":
        delete_task()
    
    elif choice =="5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option.")
"""


import string
import secrets

print("==== Password Generator ")

while True:
    try:
        length = int(input("Enter password length: "))
        
        if 8 <= length <= 64:
            break
        
        print("Please enter a length between 8 nad 64.")
        
    except ValueError:
        print("Please enter a number.")
        
characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ''.join(
    secrets.choice(characters)
    for _ in range(length)
)

print("\nGenerated password::", passwod)
