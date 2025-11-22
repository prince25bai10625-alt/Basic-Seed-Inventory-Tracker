# Basic-Seed-Inventory-Tracker
This project is a minimal, console-based application designed for a rural seed distribution center to quickly and easily manage its stock. It allows an administrator to check the current inventory levels, prices, and total estimated value of the stock.


Rural Seed Distribution Center Inventory Tracker

Overview of the Project

This project is a minimal, console-based application designed for a rural seed distribution center to quickly and easily manage its stock. It allows an administrator to check the current inventory levels, prices, and total estimated value of the stock.

The application is built using only core Python features, ensuring maximum simplicity and portability without needing to install any external libraries.

Important Note: Since this version does not use file-saving libraries, all data is temporary and will reset to the default list every time the script is closed and reopened.

Features

Real-time Stock Check: Displays the name, current quantity left, and price per unit (₹) for every seed variety.

Inventory Summary: Calculates and displays the total number of units in stock and the estimated total inventory value.

Low Stock Alerts: Automatically displays a warning message for seed varieties with less than 100 units left.

Add New Seed: Allows entry of new seed varieties, including initial stock and price.

Update Stock: Provides a simple way to adjust stock levels (add or remove quantity) for existing seeds.

Basic User Interface: Uses a simple, numbered menu for navigation.

Technologies/Tools Used

This project is built using only the following technology:

Python 3: The core application logic.

Standard Library Only: No external libraries, packages, or frameworks are required.

Steps to Install & Run the Project

Prerequisite: Ensure you have Python 3 installed on your computer. You can download it from python.org.

Save the Code: Save the provided Python code as a file named seed_inventory_simple.py.

Open Terminal: Open your computer's terminal or command prompt.

Navigate: Use the cd command to navigate to the directory where you saved seed_inventory_simple.py.

Run the Script: Execute the file using the Python interpreter:

python seed_inventory_simple.py


Instructions for Testing

When you run the script, the inventory table and the main menu will appear. Follow the numbered instructions:

Menu Option

Action

Instructions

1

Add New Seed Variety

Enter the seed name, initial quantity (as a whole number), and price per unit (e.g., 45.00).

2

Update/Adjust Stock

Enter the number corresponding to the seed you want to change. Then, enter the quantity to add (positive number, e.g., 50) or remove/sell (negative number, e.g., -20).

3

Refresh/View

Redisplays the latest inventory table.

4

Exit

Closes the application. (Note: Changes are lost upon exit in this version).

Example of Expected Output Structure:

==========================================================
       RURAL SEED DISTRIBUTION CENTER INVENTORY
==========================================================
No. Seed Name                  Quantity Left  Price (₹) 
----------------------------------------------------------
1   Hybrid Maize (Red)         550            45.00     
2   Local Wheat (Sona)         1200           32.50     
3   Paddy (Basmati 1509)       80             60.75     
  *** LOW STOCK WARNING for Paddy (Basmati 1509) ***
4   Mung Bean (Summer)         300            70.00     
----------------------------------------------------------
Total Stock: 2130 units
Estimated Total Value: ₹125,550.00
==========================================================
