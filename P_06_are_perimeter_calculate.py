#Ask the user for their width and height
width = float(input("What is the width you are calculating?"))
height = float(input( "Now what is the height?"))

#Calculate the area / perimetre
area = height * width
perimetre = 2 * (width + height)

# Output the area and perimetre answers
print()
print(f"Your  total perimetre is {perimetre} metres")
print(f"Your total area is {area} metres")

