# Ask user for width and loop until they enter a number that is morethan zero

while True:
    error = "Please enter a number above zero"

    try:
        #ask the user for a number
        width = float(input("Width: "))

        #check if the number is more than aero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)