Coffee_Object_Oriented_Programming

This repository features a Python coffee machine simulator with both functional and OOP versions. Users can order espresso, latte, or cappuccino, manage resources, and make payments with change calculation. The OOP approach improves modularity and readability, offering a more scalable solution.

Features

a. Coffee Options: Choose between espresso, latte, and cappuccino.
b. Resource Management: Automatically checks the availability of ingredients (water, milk, and coffee) for each order.
c. Coin Handling: Accepts quarters, dimes, nickels, and pennies as input, ensuring the user pays enough for their coffee.
d. Change Calculation: Calculates and returns change when more money is inserted than required.
e. Inventory Report: A report command shows the current status of the machine's resources and money.
f. Shutdown: Use the off command to turn off the machine.

How It Works:

Choose a Coffee: The program prompts the user to choose a type of coffee.
Resource Check: It checks if enough ingredients are available for the chosen coffee.
Insert Coins: If ingredients are sufficient, the program asks for coin input.
Sufficient Payment: If the inserted amount covers the coffee's cost, it dispenses the drink and updates the resource inventory. If not, it refunds the money.
View Report: The report command displays the remaining ingredients and total money collected.
