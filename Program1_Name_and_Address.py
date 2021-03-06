"""
Author: Trina Jones
Program 1: Name and Address
Description: This program asks the user to enter his/her name, then
asks user to enter his/her address, then outputs the following to the console
"""

# 1. read the user's Name: read first name and last name
firstName = input("Please enter your first name: ")  # input statement
lastName = input("Please enter your last name: ")  # input statement
Name = (firstName + "" + lastName)  # assignment statement

# 2. read the user's Address: read address
Address = input("Please enter your address: ")  # input statement

# 3. Display message and user's input
print("We received the following information: ")  # output statement 
print("User Name: ", Name)  # output statement
print("User address: ", Address)  # output statement
