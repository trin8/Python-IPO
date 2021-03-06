"""
Author: Trina Jones
Program 3: Trapezoid Prism Volume
Description: This program calculates volumes of trapezoidal prisms
Ask the user to enter Length, Height, Base Width, and Top Width values'
then stores the values in variables (Python variables use lower case and camel casing)
Display outputs of all measurements and the volume to the console
Reduce all four measurements of the prism by 25%, and calculate the
volume again using the reduced values, Display outputs of reduced
measurements and reduced volume to the console
"""

# 1. read the user's Length: read length
length = int(input("Please enter the Length: "))  # input statement

# 2. read the user's Height: read height
height = int(input("Please enter the Width: "))  # input statement

# 3. read the user's Base Width: read baseWidth
baseWidth = int(input("Please enter the Base Width: "))  # input statement

# 4. read the user's Top Width: read topWidth
topWidth = int(input("Please enter the Top Width: "))  # input statement

# 5. Calculate the volumes of trapezoidal prisms Volume(V) = L x H x ((P + Q)/2)
volumeOfTrapezoidal = length * height * ((baseWidth + topWidth)/2)  # assignment statement

# 5. Display all four measurements: print length, height, baseWidth, topWidth
print("\nOriginal Measurements:")  # output statement
print("Length: ", length, "Height: ", height, "Base Width: ", baseWidth, "Top Width: ", topWidth)  # output statement

# 6. Display the volumes of trapezoidal prisms
print("volumes of trapezoidal prisms: ", volumeOfTrapezoidal)  # output statement

# 8. Reduce by 25% all four measurements: read newLength, newHeight, newBaseWidth, newTopWidth
TWENTY_FIVE_PERCENT = 0.25  # assignment statement

newLength = (length - (length * TWENTY_FIVE_PERCENT)) # assignment statement
newHeight = (height - (height * TWENTY_FIVE_PERCENT))  # assignment statement
newBaseWidth = (baseWidth - (baseWidth * TWENTY_FIVE_PERCENT))  # assignment statement
newTopWidth = (topWidth - (topWidth * TWENTY_FIVE_PERCENT)) # assignment statement

# 9. Calculate the volume reduce by 25%: get newVolumeOfTrapezoidal = newLength * newHeight * ((newBaseWidth + newTopWidth)/2)
newVolumeOfTrapezoidal = newLength * newHeight * ((newBaseWidth + newTopWidth)/2)   # assignment statement

# 10. Display measurements and volume reduced by 25%
print("\nNew Measurements reduced by 25%:")  # output statement
print("Length:", newLength, "Height:", newHeight, "Base Width:", newBaseWidth, "Top Width:", newTopWidth)  # output statement
print("Volume of trapezoidal prisms: ", newVolumeOfTrapezoidal)  # output statement
