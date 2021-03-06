"""
Author: Trina Jones
Assignment 1
Program 2: Temperature Converter
Description: This program converts Fahrenheit to Kelvin temperatures
the formula is as follows: K = (F + 459.67) x 5/9
This program ask the user to enter a temperature in Fahrenheit,
and then display the temperature converted to Kelvin
"""

# 1. read the user's Fahrenheit input: read fahrenheit_temperature
fahrenheit_temperature = int(input("Please enter a temperature in Fahrenheit: "))  # input statement, store integer value from input

# 2. Convert Fahrenheit to Kelvin: kelvin (fahrenheit + 459.67 * 5/9)
kelvin = (fahrenheit_temperature + 459.67) * 5/9  # assignment statement, create variable name Kelvin, calculate and store value

# 3. Display the kelvin: print Fahrenheit temperature "degress in Fahrenheit =" Kelvin
print( fahrenheit_temperature, "degrees in Fahrenheit    =   ", format(kelvin, '.2f'), "in Kelvin")  # output statement displaying Fahrenheit converted to Kelvin
