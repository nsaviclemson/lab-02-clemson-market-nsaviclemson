"""
Author: Nicolas Savi
Date: 1/20/26
Assignment: Clemson Market total calculator
Course: 1051
Lab Section: 01


Description: Making a calculator to calculate the cost of the goods for someone buying something 
the market
"""


print("Welcome to the Clemson Market!")

print("We have the following items available:\n")
print("Bag of Chips: $5.99 each")
print("Turkey Sandwich: $13.23 each")
print("Bananas: $2.73 per lb")

print("How many bags of chips do you want?")
chips1 = int(input())
print("How many turkey sandwiches do you want?")
turkey1 = int(input())
print("How many lbs of bananas do you want?")
banana = float(input())
#user inputs for the code

chips1 = float(chips1)
turkey1 = float(turkey1)
#turning the chip and turkey values into floats so we can multiply them
chipscost = 5.99     
turkeycost = 13.23
bananacost = 2.73
#price for each item

totalchips = chips1 * chipscost
totalturkey = turkey1 * turkeycost
totalbanana = banana * bananacost
total_cost = totalchips + totalturkey + totalbanana
#price calculation for each item to quantity


# TODO: Format below output correctly
print(f"Your total before tax is {total_cost:.2f}.")
#making sure that the cost is only 2 decimal places

print("Please enter the tax rate:")

tax_rate = float(input()) / 100
#putting the tax rate into decimals

total_tax_cost = tax_rate * total_cost
total_total = total_tax_cost + total_cost
#total cost and the tax rate added onto it

# TODO: Format below output correctly
print(f"Your total after tax is {total_total:.2f}. Thank you for shopping at the Clemson Market!")
#The total end calculation with the printed text