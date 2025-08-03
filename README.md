## Latte Love - Coffee Shop Ordering System

Welcome to Latte Love, a simple command-line based ordering system for a fictional coffee shop. This Python program allows customers to place orders for a variety of beverages and desserts, and generates a final bill with optional discounts.

***Features***

User-friendly menu-driven interface.

Supports ordering from 5 categories:

Espresso

Frappuccino

Teavana

Latte

Desserts

Dynamic price calculation based on user choices.

5% discount for bills over ₹500.

Order data is serialized using Python's pickle module.

Bill includes date and time, customer name, and contact details.

***Requirements***
Python 3.10

No external libraries are required beyond the Python standard library.

***How to Run***

1. Make sure you have Python 3 installed.

2. Save the code in a file named, for example: latte_love.py

***Program Flow***
The user is greeted and asked for their name and phone number.

They are shown a menu of categories to order from.

For each selected category, sub-options are displayed with prices.

The user can add multiple items and quantities.

Orders are stored in a list and saved to a binary file (coffee.dat).

***A final bill is generated showing:***

1. Items ordered
2. Total amount
3. Discount
4. Final payable amount
5. Timestamp
