# Fence cost calculator
# Author: Michaela Gardner
# Date: JUne 5th 2024

# This code calculates your total perimetre and the amount of money you will need to spend for the perimetre you have measured

#Ask what persons name is
username = input("What is your name?\n")

# Ask  user for width until they enter a number that is more than zero
def num_check(question):

    error = "Please enter a number more than zero\n"
    while True:

        try:
            # Ask the user for a number
            number = float(input(question))

            # Check that the number is more than zero
            if number > 0:
                return number
            else:
                print(error)

        except ValueError:
            print(error)

# Main Rountine Starts Here
keep_going = ""
while keep_going =="":
    # Get width and height
    width = num_check("What is the width of your fence in metres?\n")
    length = num_check("What is the length of your fence in metres?\n")

    # Calculate area and perimetre
    perimetre = 2 * (width + length)
    # Display output
    print()
    print(f"The total perimetre of your fence is {perimetre:.2f} metres")

    # Ask what the cost per metre is
    cost = num_check("What is the cost of your fencing per metre?\n$")

    # Find total cost for area and perimetre
    total_cost = cost * perimetre

    # Display total cost
    print()
    print(f"The total cost you will have to spend on your fence is ${total_cost:.2f} for {perimetre:.2f} metres")
                 
    # Ask if they want to keep going
    keep_going = input(f"Thank you {username} for using my program.Please press 'enter' to keep going or any key to quit.")
    print()

print("Have a great day!😃")
