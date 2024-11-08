# Ask user for width and loop until they enter a number more than zero
def num_check(question):...

# Main Routine starts here...

keep_going = "":
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("You can press 'enter' to keep going or any key to quit")
    print()

print("Thank you for your time with the Area / Perimeter Calculator! :)")