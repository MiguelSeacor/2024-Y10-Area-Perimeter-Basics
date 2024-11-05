# ask the user for their name
username = input("What is your name? ")

# ask the user for their favorite number (integer)
fav_num = int(input("What is your favorite number? "))

# Double, halve and square the user's favorite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# Greet the user
print(f"\nHi {username}, your favorite number is {fav_num}")

# Output the results of doubling, halving and squaring their favorite integer
print(f"The double of {fav_num} is {double}")
print(f"The half of {fav_num} is {halve}")
print(f"The square of {fav_num} is {square}")
print()
print("Enjoy yourself now :)")

