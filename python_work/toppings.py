requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 5-3
alien_color = 'green'
#alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points")

# 5-4
if alien_color == 'green':
    print("You earned 5 points for shooting the alien")
if alien_color != 'green':
    print("You earned 10 points")

if alien_color == 'green':
    print("You earned 5 points for shooting the alien")
else:
    print("You earned 10 points")

# 5-5
if alien_color == 'green':
    print("You earned 5 points for shooting the alien")
elif alien_color == 'yellow':
    print("You earned 10 points")
elif alien_color == 'red':
    print("You earned 15 points")

if alien_color == 'green':
    score = 5
elif alien_color == 'yellow':
    score = 10
elif alien_color == 'red':
    score = 15

print(f"You earned {score} points")

# 5-6
age = 20

if age < 2:
    print("You are a baby")
elif 2  <= age < 4:
    print("You are a toddler")
elif  4 <= age < 13:
    print("You are a kid")
elif  13 <= age < 20:
    print("You are a teenager")
elif  20 <= age < 65:
    print("You are a adult")
else:
    print("You are an elder")

# 5-7
favorites_fruits = ["apple", "banana", "raspberry"]

if 'apple' in favorites_fruits:
    print("You really like apples")

if 'cherry' not in favorites_fruits:
    print("You don't really like cherries")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

