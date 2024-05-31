# Basic Cafe POS using dictionaries
## Overview of coding task
The original task set was to print the total stock value using a menu list, a stock dictionary, and a price dictionary.
I took the task further and produced a point-of-sale system that enabled staff to build a customer order, restock and reprice menu items, and print an itemised stock inventory.
## Installation
Can be run on your preferred IDE.
## Usage
Once run, the user will be presented with the main menu and input. The user is asked to select which action to take. Validation will prevent user from entering an invalid option.
### Making an order
If the user selects 'customer order', they will shown the menu and asked to input the item code. If the item doesn't exist or a non-numeric input is entered, the user will be asked to input again.
The user is then asked to enter the quantity the customer is ordering. If there is not enough stock or a non-numeric input is entered, the user will be asked to input again. In the case of the former, the quantity left in stock is presented.
After an item and quantity are entered, the user has the option to add another item to the order or complete the order.
If the order is completed, the user is shown an itemised list of quantity and price, along with total price.
### Doing a restock
If the user selects 'restock', they will shown the menu and asked to input the item code. If the item doesn't exist or a non-numeric input is entered, the user will be asked to input again.
The user is then asked to enter the quantity to restock. If a non-numeric input is entered, the user will be asked to input again.
After an item and quantity are entered, the user has the option to restock another item or finish restocking.
If restocking is finished, an updated inventory is shown to the user.
### Update price list
If the user selects 'price change', they will shown the menu and asked to input the item code. If the item doesn't exist or a non-numeric input is entered, the user will be asked to input again.
The user will be asked what the new price is. If a non-numeric input is entered, the user will be asked to input again.
After an item and quantity are entered, the user has the option to reprice another item or finish repricing.
If repricing is finished, an updated price list is shown to the user.
### Showing total inventory
If the user selects 'total stock value', they will be shown an itemised list of stock levels, total value per item, and total value of all items.
### Quitting the programme
If the user selects 'quit programme', the programme will end. Dictionary values will return to their global presets.
## Credits and reflections
This code is entirely my own.
Discovering how to combine while loops and try-except to keep asking for valid input was an exciting progression in my ability to code. I previously had to rerun code when invalid inputs were entered.
This was my first introduction to using dictionaries, and it's always exciting to use a new type of data structure.
This was the first time I used for loops to print an itemised list.
I made a conscious decision that all inputs are number-based to enable usage on a numpad only device.
If I were to develop the code further, I would add an ability to record breakage/wastage and would figure out how to update the global dictionary values not to lose changes once the programme had been closed.
