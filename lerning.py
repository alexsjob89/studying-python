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
            print("\n-----Your-----")

            total = 0

            for index, product in enumerate(cart, start=1):
                price = products[product]
                total += price

                print(f"{index}. {product.title():10} £{price:.2f}")

            print("---------------------")
            print(f"Total: £{total:.2f}")












    





