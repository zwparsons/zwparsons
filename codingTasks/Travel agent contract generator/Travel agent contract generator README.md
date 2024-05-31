# Basic travel agent contract generator
## Overview of coding task
The original task set was to use functions to calculate the total cost of a person's holiday based on the number of nights, destination city, and number of car rental days.
I took the task further and produced a dynamic contract generator
## Installation
Can be run on your preferred IDE.
## Usage
Once the code has been run, the user will be asked to enter the client's name, the city the client is flying to, the number of nights the client is staying, and the number of car rental days requested.
Once entered, the code will generate the contract, which changes based on the choices made.
The contract will confirm the city, number of nights, hotel, and hotel cost per night.
If the client is travel to anywhere other than London (ie requires a flight), the airline and flight cost is confirmed.
If the client is renting a car, the number of days and cost per day is confirmed.
If the client is staying in London and not renting a car (ie hotel only), a sentence with the total hotel charge is shown. Otherwise, an itemised list is shown with flight, hotel, car rental (if applicable), and total cost.
Then a signatory panel is shown for the client to confirm details and book the holiday.
## Credits and reflections
This code is entirely my own.
These were the first functions I defined, which was a massive leap in my coding ability.
If I were to write the code again, I would create price lists in a data structure, rather than using if statements.
