# Ask user for width and loop until they enter a number that is morethan zero
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

# Main Routine goes here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)