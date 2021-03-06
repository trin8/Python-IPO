"""
Author: Trina Jones
Assignment 1
Program 1: Name and Address
Description: This program asks the user to enter his/her name, then
asks user to enter his/her address, then outputs the following to the console
"""

# 1. read the user's Name: read first name and last name
firstName = input("Please enter your first name: ")  # input statement, ask user to enter his/her first name
lastName = input("Please enter your last name: ")  # input statement, ask user to enter his/her last name
Name = (firstName + "" + lastName)  # assignment statement, store first name and last name in variable name Name

# 2. read the user's Address: read address
Address = input("Please enter your address: ")  # input statement, ask user to enter his/her address

# 3. Display message and user's input: message " We received the following information:", Name, Address
print("We received the following information: ")  # output statement displaying message of info received
print("User Name: ", Name)  # output statement displaying variable Name
print("User address: ", Address)  # output statement displaying variable Address
