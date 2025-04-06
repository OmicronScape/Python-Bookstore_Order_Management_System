# BOOKSTORE ORDER MANAGEMENT SYSTEM

"""
|--------------------------------------------- PROGRAM USAGE INSTRUCTIONS ------------------------------------------------|
|           This program manages book orders and updates the inventory (Stock).                                           |
|   Make sure you have the files Paragelia.csv (orders) and Stock.csv (inventory) in the same folder as this script.     |
|                                                                                                                         |
|-----> The program reads Stock.csv and displays the available quantities of books. <-----                                |
|--------> The program asks if the current order should be canceled (y = Yes / n = No) <--------                           |
|-----> Order Processing:  1. Availability Check  2. Order Cost Calculation  3. Inventory Update <------                  |
|                                                                                                                         |
|                                                   NOTES                                                                 |
|       The program uses semicolon-separated (;) data in CSV files.                                                       |
|       If there are not enough books for the order, the stock remains unchanged.                                         |
|       Cost is calculated with 2 decimal point accuracy.                                                                 |
|-------------------------------------------------------------------------------------------------------------------------|
"""

import csv
import os

# Function to read a CSV file and return the data as a list of dictionaries
def read_csv_to_dict(filename):
    if not os.path.isfile(filename):
        print(f"The file {filename} was not found.")
        return []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            return [row for row in reader]
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return []

# Function to update & write the stock back to Stock.csv after order processing
def write_dict_to_csv(filename, data, fieldnames):
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(data)

# Function to display the available stock
def display_stock(stock):
    print("Current book stock:")
    print(f"{'Book Title':<40} {'Quantity':<10}")
    print(f"{'-' * 40} {'-' * 10}")
    for item in stock:
        print(f"{item['Τίτλος βιβλίου']:<40} {item['Ποσότητα']:<10}")

# Function to process the order and update the stock
def process_order(order_list, stock):
    total_cost = 0
    print("------------------------------------------------------------------")
    print("\n-------> PROCESSING ORDER")
    print("------------------------------------------------------------------")
    for order in order_list:
        book_title = order['Τίτλος βιβλίου']
        order_quantity = int(order['Ποσότητα'])
        for item in stock:
            if item['Τίτλος βιβλίου'] == book_title:
                stock_quantity = int(item['Ποσότητα'])
                if stock_quantity >= order_quantity:
                    cost_per_book = float(item['Κόστος ανά βιβλίο'])
                    cost = order_quantity * cost_per_book
                    total_cost += cost
                    item['Ποσότητα'] = str(stock_quantity - order_quantity)
                    print(f"Book Title: {book_title}")
                    print(f"Author: {item['Συγγραφέα']}")
                    print(f"Cost per Book: {cost_per_book}")
                    print(f"Quantity: {order_quantity}")
                    print(f"{order_quantity} copy/copies of '{book_title}' by {item['Συγγραφέα']} cost {cost:.2f} EUR.")
                    print("__________________________________________________________________")
                else:
                    print(f"Not enough stock available for book: {book_title}")
                    return False
    print(f"Total order cost: {total_cost:.2f} EUR.")
    return total_cost

# Main function
def main():
    stock_filepath = r'D:\Program Files (x86)\VIsual-Studio_code\GitHub\EAP\PliPro\ERGASIA_3\Ypoergasia_2\Stock.csv'
    order_filepath = r'D:\Program Files (x86)\VIsual-Studio_code\GitHub\EAP\PliPro\ERGASIA_3\Ypoergasia_2\Paragelia.csv'

    stock = read_csv_to_dict(stock_filepath)
    if not stock:
        return

    order_list = read_csv_to_dict(order_filepath)
    if not order_list:
        return

    display_stock(stock)

    cancel_order = input("Do you want to cancel the order? (y/n): ").strip().lower()
    if cancel_order == 'y':
        print("The order has been canceled.")
    elif cancel_order == 'n':
        total_cost = process_order(order_list, stock)
        if total_cost:
            print(f"Total order cost is {total_cost:.2f} EUR.")
            print("Inventory updated.")
            display_stock(stock)
        else:
            print("The order has been canceled.")
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()
