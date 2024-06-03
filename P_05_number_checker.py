# Ask  user for width and until they enter a number that is more than zero
def num_check(question):

    error = "Please enter a number more than zero\n"
    while True:

        try:
            # ask the user for a number
            width = float(input(question))

            # check that the number is more than zero
            if width > 0:
                return width 
            else:
                print(error)

        except ValueError:
            print(error)

#Main Routine Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

    print()

for item1 in range(0, 2):
    height = num_check("Height: ")
    print(height)
