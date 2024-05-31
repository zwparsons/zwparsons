# Ask our rep to enter the client's name
client_name = input("Nice work selling a holiday, \
let's get a contract written up for the client to sign.\n\nWhat is the client's name? ")

# Setting checking variable for while loop that checks city input later in the code
city_flight_okay = False 

# Ask rep to enter the client's desitination city
city_flight = input("\nWhich city is the client going to?\
\na - Paris\nb - Accra\nc - Antananarivo\nd - London\n\nEnter the client's choice (letter only) here: ")

# Check the rep has entered a valid option and, if not, ask to try again
if city_flight == "a" or city_flight == "b" or city_flight == "c" or city_flight == "d":
    city_flight_okay = True    
while city_flight_okay == False:
    city_flight = input("\nLooks like you chose an unavailable option,\
    please try again.\n\na - Paris\nb - Accra\nc - Antananarivo\nd - London\n\n\
    Enter the client's choice (letter only) here: ")
    if city_flight == "a" or city_flight == "b" or city_flight == "c" or city_flight == "d":
       city_flight_okay = True

# Setting a checking variable for num_nights input
num_nights_okay = False

# Ask rep to input number of night client is staying
# If input returns an error (eg by not being an integer), asks to repeat
while num_nights_okay == False:
    try:
        num_nights = int(input("\nHow many nights is the client staying?\n\nEnter a number here: "))
        num_nights_okay = True
    except:
        print("\nThat doesn't look right, please try again.")

# Same code for num_nights to ask rep to enter how many days of car rental the rep requires
rental_days_okay = False
while rental_days_okay == False:
    try:
        rental_days = int(input("\nLastly, how many days of car rental does the client require?\
        \n\nIf they are not planning to rent a car, answer with 0.\n\nEnter a number here: "))
        rental_days_okay = True
    except:
        print("\nThat doesn't look right, please try again.")

# Define cities for merge into f string later
# Define Paris
if city_flight == "a":    
    city = "Paris"
# Define Accra
elif city_flight == "b":    
    city = "Accra"
# Define Tana
elif city_flight == "c":
    city = "Antananarivo"
# Define London
elif city_flight == "d":
    city = "London"

# Define hotel name for merge into f string later
# Define Louvre
if city_flight == "a":    
    hotel = "Louvre View Hotel"
# Define Big Milly's
elif city_flight == "b":    
    hotel = "Big Milly's Backyard"
# Define Saka
elif city_flight == "c":
    hotel = "Sakamanga Hotel"
# Define Islington
elif city_flight == "d":
    hotel = "Islington Inn"

# Define cost of various hotels
# Define cost of Parisian hotel (per night)
if city_flight == "a":    
    hotel_charge = 125
# Define cost of Accra hotel (per night)
elif city_flight == "b":    
    hotel_charge = 65
# Define cost of Tana hotel (per night)
elif city_flight == "c":
    hotel_charge = 35
# Define cost of London hotel (per night)
elif city_flight == "d":
    hotel_charge = 175

# Function that works out total hotel cost
def hotel_cost(num_nights, hotel_charge):
    return num_nights * hotel_charge


# Function that works out how much it will cost for the user to fly (cost is both ways)
def plane_cost(city_flight):
    
    # Return the cost of a flight to Paris
    # Easyjet, yo. So cheap.
    if city_flight == "a":
        return 160
    
    # Return the cost of a flight to Accra
    # You can get them cheaper if you fly direct
    elif city_flight == "b":
        return 650
    
    # Return the cost of a flight to Tana
    # So expensive to fly to Madagascar, those damn penguins did it for free
    elif city_flight == "c":
        return 900
    
    # Return the cost of a flight to London
    # Wait, the clients are already in London... staycation!
    elif city_flight == "d":
        return 0

# Define cost of car rental in various cities  
# Define cost to rent a car in Paris (per day)
if city_flight == "a":    
    car_charge = 25
# Define cost to rent a car in Accra (per day)
elif city_flight == "b":    
    car_charge = 35
# Define cost to rent a car in Tana (per day)
elif city_flight == "c":
    car_charge = 30
# Define cost to rent a car in London (per day)
elif city_flight == "d":
    car_charge = 75

# Function that works out the cost of renting a car for the number of days requested 
def car_rental(rental_days, car_charge):
    return rental_days * car_charge


# Function that calls all other functions and calculates total holiday cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights, hotel_charge) + plane_cost(city_flight) + car_rental(rental_days, car_charge)

# Series of f strings that construct a contract for the client to sign
# Content is dynamic based on input
print(f"Dear {client_name},\n\nWe're excited to offer you a holiday to {city} for {num_nights} nights!\n\n"
f"You will be staying in the fabulous {hotel}, which costs £{hotel_charge} per night.")

# Only include flight details when client is not going to London
# (they are based in London, so do not require a flight)
if city_flight != "d":
    print(f"\nYou will be flying with our partner airline, Dodo Airlines. "\
    f"Your flight will cost £{plane_cost(city_flight)}.")

# Only include car rental details if client has requested rental
if rental_days > 0:
    print(f"\nYou have asked us to arrange car rental for {rental_days} days, "
    f"which will cost £{car_charge} per day.")

# If client is going to London and does not require car rental, the total cost is only the hotel stay
if city_flight == "d" and rental_days == 0:
    print(f"\nThe total cost of your holiday will be "
    f"£{hotel_cost(num_nights, hotel_charge)}.")

# Otherwise, create an itemised list of costs, with total
else:
    # Add hotel stay to itemised list
    print(f"\nThe breakdown of the cost of your holiday is as follows:"
    f"\n\nHotel:\t\t£{hotel_cost(num_nights,hotel_charge)}")
    
    # Where there is a flight, add to itemised cost list
    if city_flight != "d":
        print(f"Flight:\t\t£{plane_cost(city_flight)}")
    
    # Where there is a car rental, add to itemised cost list
    if rental_days > 0:
        print(f"Car rental:\t£{car_rental(rental_days, car_charge)}")
    
    # Provide a total of the breakdown
    print(f"\nTotal:\t\t£{holiday_cost(hotel_cost, plane_cost, car_rental)}")

# For all clients, continue contract and add signatory panel
print("\nIf you are happy with the details outlined above, please sign and date below.\n\n\
Date:\n\nPrint name:\n\nSigned:")
