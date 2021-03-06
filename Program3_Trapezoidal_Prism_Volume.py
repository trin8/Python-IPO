"""
Author: Trina Jones
Assignment 1
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
length = int(input("Please enter the Length: "))  # input statement, ask and store integer typed value in variable name length

# 2. read the user's Height: read height
height = int(input("Please enter the Width: "))  # input statement, ask and store integer typed value in variable name height

# 3. read the user's Base Width: read baseWidth
baseWidth = int(input("Please enter the Base Width: "))  # input statement, ask and store integer typed value in variable name baseAWidth

# 4. read the user's Top Width: read topWidth
topWidth = int(input("Please enter the Top Width: "))  # input statement, ask and store integer typed value in variable name topWidht

# 5. Calculate the volumes of trapezoidal prisms Volume(V) = L x H x ((P + Q)/2): get VolumeOfTrapezoidal = length * height * ((baseWidth + topWidth)/2)
volumeOfTrapezoidal = length * height * ((baseWidth + topWidth)/2)  # assignment statement, calculate the volume of trapezoidal prism and store in volumeOfTrapezoidal

# 5. Display all four measurements: print length, height, baseWidth, topWidth
print("\nOriginal Measurements:")  # output statement, display message "Measurement:"
print("Length: ", length, "Height: ", height, "Base Width: ", baseWidth, "Top Width: ", topWidth)  # output statement, display length, height, base width and top width value

# 6. Display the volumes of trapezoidal prisms: print "Volume of trapezoidal prisms:", volumeOfTrapezoidal
print("volumes of trapezoidal prisms: ", volumeOfTrapezoidal)  # output statement, display the calculated Volume of Trapezoidal prisms

# 8. Reduce by 25% all four measurements: read newLength, newHeight, newBaseWidth, newTopWidth
TWENTY_FIVE_PERCENT = 0.25  # assignment statement, store 25% to constant variable name TWENTY_FIVE_PERCENT

newLength = (length - (length * TWENTY_FIVE_PERCENT)) # assignment statement, length minus 25%  and store in new variable name newLenth
newHeight = (height - (height * TWENTY_FIVE_PERCENT))  # assignment statement, height minus 25% and store in new variable name newHeight
newBaseWidth = (baseWidth - (baseWidth * TWENTY_FIVE_PERCENT))  # assignment statement, baseWidth minus 25% and store in new variable name newBaseWidth
newTopWidth = (topWidth - (topWidth * TWENTY_FIVE_PERCENT)) # assignment statement, topwidth minus 25% and store in new variable name newTopWidth

# 9. Calculate the volume reduce by 25%: get newVolumeOfTrapezoidal = newLength * newHeight * ((newBaseWidth + newTopWidth)/2)
newVolumeOfTrapezoidal = newLength * newHeight * ((newBaseWidth + newTopWidth)/2)   # assignment statement, calculate the new volume of trapezoidal prism and store in newVolumeOfTrapezoidal

# 10. Display measurements and volume reduced by 25%: print "New Measurements reduced by 25%: ", newLength, newHeight, newBaseWidth, newTopWidth, newVolumeOfTrapezoidal
print("\nNew Measurements reduced by 25%:")  # output statement, display new measurement message "New Measurements:"
print("Length:", newLength, "Height:", newHeight, "Base Width:", newBaseWidth, "Top Width:", newTopWidth)  # output statement, display new length, height, base width, top width
print("Volume of trapezoidal prisms: ", newVolumeOfTrapezoidal)  # output statement, display new volume of trapezoidal
