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

age = 20
is_student = False
has_discount_code = True

if (age > 18 or age < 65) and not is_student or has_discount_code:
    print("Discount applies!!!")
else:
    print("No discount available.")
    





