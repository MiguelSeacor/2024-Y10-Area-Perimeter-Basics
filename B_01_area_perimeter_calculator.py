# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    while True:
        error = "Please enter a number above zero"

        try:
            #ask the user for a number
            response = float(input(question))

            #check if the number is more than aero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

# Main Routine Goes here

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate Area / Perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit: ")
    print()

print("Thank you for using the area / perimeter calculator :)")