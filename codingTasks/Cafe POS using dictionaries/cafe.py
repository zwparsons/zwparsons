
# Creating a list for the menu
menu = ["Cake", "Sandwich", "Coffee", "Tea"]

# Creating dictionaries for menu item stock levels and price 
stock = {"Cake": 5, "Sandwich": 10, "Coffee": 20, "Tea": 15}
price = {"Cake": 2.5, "Sandwich": 3.25, "Coffee": 1.75, "Tea": 1.5}

# Creating a variable to store total stock value
total_stock = 0

# Creating a dictionary for user to create a customer order
# Will house item and number ordered
order = {"Cake": 0, "Sandwich": 0, "Coffee": 0, "Tea": 0}

# Creating a variable to store total order value
total_order = 0

# Defualt variable value for the main menu 
action = ""


# House the entire programme in a while loop
# This will keep it running until the user selects option to quit
while action != "9":

    # Set a variable to check whether the user input is valid
    # Default to False, changes to True when user input is valid
    action_okay = False

    # Ask for user input to select what action to carry out
    action = input(f"Welcome Park Cafe's POS, what are you doing today?"
        f"\n\n0 - customer order\n1 - restock\n2 - price change\n"
        f"3 - total stock value\n9 - quit programme\n\nEnter option here: ")

    # If the user input is valid, set okay variable to True
    if action == "0" or action == "1" or action == "2" \
        or action == "3" or action == "9":
        action_okay = True
    
    # If the user input is not valid, repeatedly ask
    # until a valid option is given.
    while action_okay == False:
        action = input("!!!\nPlease select a valid option: ")
        if action == "0" or action == "1" or action == "2" or \
            action == "3" or action == "9":
            action_okay = True
    
    # MAKING AN ORDER

    if action == "0":
        
        # Define a variable that will enable user to end the order
        order_end = ""

        # Print a selection list of all the items on the menu
        # Each item has an index num to be used for user selection
        print("\nWhich item is being ordered?\n")
        for i in range(0, len(menu)):
            print(f"{i} - {menu[i]}")
        
        # Enable the user to keep adding items to the order
        # until they select it is finished
        while order_end != "n":
            
            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid 
            item_okay = False

            # If the user input is not valid, repeatedly ask
            # until a valid option is given.
            # Asking the user to choose an item from the menu
            while item_okay == False:

                # Use try except to flag if entry returns an error
                # mMinly to catch non-int entry
                try:
                    # Ask user to input item code
                    item = int(input("\nEnter item code here: "))

                    # Break the loop if no errors occur
                    item_okay = True

                    # If no errors occur but entry is not 
                    # one of the possible items...
                    if item >= len(menu) or item < 0:
                         
                        # then restart loop to ask again...
                        item_okay = False

                        # and inform user that the item doesn't exist
                        print("!!!\nItem does not exist.")
                
                # If the try returns an error... 
                except:
                    # tell what the issue is (loop restarts)
                    print("!!!\nMust be an item code.")
            
            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            qty_okay = False

            # If the user input is not valid, repeatedly ask
            # until a valid option is given.
            # Asking the user to specify how many items ordered
            while qty_okay == False:

                # Use try except to ensure int entry
                try:

                    # Ask user to input order quantity
                    qty = int(input(f"\nEnter qty of {menu[item]} "
                                    f"ordered: "))
                    
                    # Break the loop if no errors occur
                    qty_okay = True

                    # If no errors occur but there are not
                    # enough items in stock...
                    if qty > stock.get(menu[item]):

                        # restart the loop to ask again...
                        qty_okay = False
                        # and inform user how many left in stock
                        print(f"!!!\nNot enough stock."
                              f"\nAmount left: {stock.get(menu[item])}")
                
                # If the try returns an error... 
                except:
                    # tell what the issue is (loop restarts)
                    print("!!!\nMust be a whole number.")
            
            # Once both item and qty have valid inputs...
            # reduce the amount in stock...
            stock[menu[item]] = stock.get(menu[item]) - qty
            # and add item and qty to order
            order[menu[item]] = order.get(menu[item]) + qty

            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            order_end_okay = False

            # Ask user if they want to add more to the order
            order_end = input("\nAdd another item to order? y/n: ")

            # If input is valid...
            if order_end == "y" or order_end == "n":
                # continue
                order_end_okay = True
            
            # If input is not valid...
            while order_end_okay == False:
                # repeatedly ask user to input until valid
                order_end = input(f"!!!\nMust be y or n.\n\n"
                                  f"Add another item to order? y/n: ")
                if order_end == "y" or order_end == "n":
                    order_end_okay = True
            # If input is 'y', restart 'while order_end != "n":' loop
            # If input is 'n', continue
        
        # Print the headings of an order summary
        print(f"\nThe customer's order is:\n\nItem\t\tQty\tTotal")

        # Print the item, qty, and total cost for each item ordered
        # Check each item on the menu to see if it's been ordered
        for i in range(0,len(menu)):

            # Where at least one of the item has been ordered...
            if order.get(menu[i]) > 0:
                
                # Print the name of the item...
                # (trunc'd to not mess with tab alignment)
                print(f"{menu[i][:6]}\t\t"
                      # then the qty ordered...
                      f"{order.get(menu[i])}\t"
                      # and the cost (to 2dp)
                      f"{(price.get(menu[i]) * order.get(menu[i])):.2f}")
            
            # In each iteration of the loop,
            # add to the running total of the order
            total_order += (price.get(menu[i]) * order.get(menu[i]))
        
        # Under the itemised order details, print the order total cost
        print(f"\nTotal\t\t\t{total_order:.2f}\n")

        # Reset order total for next order (if applicable)
        total_order = 0

        # Reset qtys in order dictionary to 0 for next order (if applicable)
        for i in range(0,len(menu)):
            order[menu[i]] = 0
    
    # DOING A RESTOCK

    elif action == "1":    
        
        # Define a variable that will enable user to finish restocking
        restock_end = ""

        # Print a selection list of all the items on the menu
        # Each item has an index num to be used for user selection
        print("\nWhich item are you restocking?\n")
        for i in range(0, len(menu)):
            print(f"{i} - {menu[i]}")
        
        # Enable the user to keep restocking items
        # until they have finished
        while restock_end != "n":

            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            item_okay = False

            # If the user input is not valid, repeatedly ask
            # until a valid option is given.
            # Asking the user to choose an item from the menu to restock
            while item_okay == False:
                
                # Use try except to flag if entry returns an error
                # Mainly to catch non-int entry
                try:
                    # Ask user to input item code
                    item = int(input("\nEnter item code here: "))

                    # Break the loop if no errors occur
                    item_okay = True

                    # If no errors occur but entry is not 
                    # one of the possible items...
                    if item >= len(menu) or item < 0:

                        # then restart loop to ask again...
                        item_okay = False

                        # and inform user that the item doesn't exist
                        print("!!!\nItem does not exist.")
                
                # If the try returns an error... 
                except:
                    # tell what the issue is (loop restarts)
                    print("!!!\nMust be an item code.")
            
            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            qty_okay = False

            # If the user input is not valid, repeatedly ask
            # until a valid option is given.
            # Asking the user to specify how many items to restock
            while qty_okay == False:

                # Use try except to ensure int entry
                try:
                    
                    # Ask user to input restock quantity
                    qty = int(input(f"\nEnter qty of {menu[item]} "
                                    f"to add to existing stock: "))

                    # Break the loop if no errors occur
                    qty_okay = True
                
                # If the try returns an error... 
                except:
                    # tell what the issue is (loop restarts)
                    print("!!!\nMust be a whole number.")
            
            # Once both item and qty have valid inputs
            # increase amount in stock
            stock[menu[item]] = stock.get(menu[item]) + qty

            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            restock_end_okay = False

            # Ask user if they want to restock another item
            restock_end = input("\nRestock another item? y/n: ")

            # If input is valid...
            if restock_end == "y" or restock_end == "n":
                # continue
                restock_end_okay = True
            
            # If input is not valid...
            while restock_end_okay == False:
                # repeatedly ask user to input until valid
                restock_end = input(f"!!!\nMust be y or n.\n\n"
                                    f"Restock another item? y/n: ")
                if restock_end == "y" or restock_end == "n":
                    restock_end_okay = True
            # If input is 'y', restart 'while restock_end != "n":' loop
            # If input is 'n', continue
        
        # Print the stock dictionary to outline new stock levels
        print(f"\nYour updated stock levels are: {stock}")
        
    # UPDATE PRICE LIST

    elif action == "2":
        
        # Define a variable that will enable user to
        # finish changing prices
        price_end = ""
        
        # Print a selection list of all the items on the menu
        # Each item has an index num to be used for user selection
        print("\nWhich item are you repricing?\n")
        for i in range(0, len(menu)):
            print(f"{i} - {menu[i]}")
        
        # Enable the user to keep repricing items
        # until they have finished
        while price_end != "n":
            
            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            item_okay = False

            # If the user input is not valid, repeatedly ask
            # until a valid option is given.
            # Asking the user to choose an item from the menu to reprice
            while item_okay == False:
                
                # Use try except to flag if entry returns an error
                # Mainly to catch non-int entry
                try:
                    # Ask user to input item code
                    item = int(input("\nEnter item code here: "))
                    
                    # Break the loop if no errors occur
                    item_okay = True
                    
                    # If no errors occur but entry is not 
                    # one of the possible items...
                    if item >= len(menu) or item < 0:
                        
                        # then restart loop to ask again...
                        item_okay = False
                        
                        # and inform user that the item doesn't exist
                        print("!!!\nItem does not exist.")
                
                # If the try returns an error... 
                except:
                    # tell what the issue is (loop restarts)
                    print("!!!\nMust be an item code.")
            
            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            new_price_okay = False
            
            # If the user input is not valid, repeatedly ask
            # until a valid option is given.
            # Asking the user to specify the new price
            while new_price_okay == False:
                
                # Use try except to ensure float entry
                try:

                    # Ask user to input new price 
                    new_price = float(input(f"\nEnter new price for "
                                            f"{menu[item]}: "))
                    
                    # Break the loop if no errors occur
                    new_price_okay = True
                
                # If the try returns an error... 
                except:
                    # tell what the issue is (loop restarts)
                    print("!!!\nMust be a number.")    
            
            # Once both item and new price have valid inputs
            # update the price dictionary with the new price
            price[menu[item]] = new_price

            # Set a variable to check whether the user input is valid
            # Default to False, changes to True when user input is valid
            price_end_okay = False

            # Ask user if they want to reprice another item
            price_end = input("\nChange price of another item? y/n: ")

            # If input is valid...
            if price_end == "y" or price_end == "n":
                # continue
                price_end_okay = True
            
            # If input is not valid...
            while price_end_okay == False:
                # repeatedly ask user to input until valid
                price_end = input(f"!!!\nMust be y or n.\n\n"
                                  f"Change price of another item?? y/n: ")
                if price_end == "y" or price_end == "n":
                    price_end_okay = True
            # If input is 'y', restart 'while price_end != "n":' loop
            # If input is 'n', continue

        # Print the price dictionary to outline new price(s)
        print(f"\nYour updated price list is: {price}")
    
    # PRINT TOTAL STOCK VALUE
    
    elif action == "3":
        
        # Print intro and headings of a stock value breakdown
        print("\nYour total stock value is:"
              f"\n\nItem\t\tQty\tTotal")

        # For all the items on the menu...
        for i in range(0,len(menu)):
                
                # Print the name of the item...
                # (trunc'd to not mess with tab alignment)
                print(f"{menu[i][:6]}\t\t"
                      # then the qty in stock
                      f"{stock.get(menu[i])}\t"
                      # and the value of the stock (to 2dp)
                      f"{(price.get(menu[i]) * stock.get(menu[i])):.2f}")
                
                # In each iteration of the loop,
                # add to the running total of total stock value
                total_stock += (price.get(menu[i]) * stock.get(menu[i]))
        
        # Under the itemised order details, print the total stock value
        print(f"\nTotal\t\t\t{total_stock:.2f}\n")
    
    # QUIT THE PROGRAMME

    elif action == "9":
        
        # Print a goodbye message before break
        print("\nGoodbye!")
