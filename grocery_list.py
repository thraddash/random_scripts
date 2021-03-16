#!/usr/bin/env python
'''
User Input
loop through grocery list
provide output to console
'''

# create empty data structure
grocery_item = {}

grocery_history = [] 

# variable for while loop condition
start = 'True'

while start:
  #Input item name 
  name = input("Item name: ")

  #Input item quantity
  quantity = input("Item quantity: ")

  #Input item price
  price = input("Price per item: ")

  #Create a dictionary entry to hold the name, quantity and price of item
  grocery_item = {'name':name, 'quantity':int(quantity), 'price':float(price)}

  #Add the grocery_item to the grocery_history list using the append function
  grocery_history.append(grocery_item)

  #Accept input from the user asking if they have finished entering grocery item
  response = input("Would you like to enter another item? (y/n): ")
  if response == 'n':
    start = False

# Define variable to hold grand total called 'grand_total'
grand_total = 0

# Define a 'for' loop.

for item in grocery_history:

  # Calculate the item total for the grocery_item
  item_total  = item['quantity'] * item['price']

  #Add the item_total to the grand_total
  grand_total += item_total

  #Output the information for the grocery item to match this example
  # 2 pears @ $.50 ea $3.00
  print("%d %s @ $%.2f ea $%.2f" %(item['quantity'], item['name'], item['price'], item_total))

  #set the item_total equal to 0
  item_total = 0

#print the grand total
print("Grand total: $%.2f" %(grand_total))
