# Python-Bookstore_Order_Management_System
A simple Python program that manages book orders and updates inventory using CSV files. It checks stock availability, calculates total cost, and modifies inventory based on customer orders

# BookstoreOrderManager

**BookstoreOrderManager** is a Python command-line application that manages book orders and updates the inventory of a small bookstore using CSV files.

This project is designed for educational purposes and demonstrates how to process structured data using Python.

---

## 📖 Description

BookstoreOrderManager handles two CSV files:

- `Stock.csv`: Contains the available books in stock.
- `Paragelia.csv`: Contains customer orders.

The script allows the user to view available inventory, decide whether to proceed with or cancel the order, and if accepted, it processes the order by checking availability, calculating cost, and updating the stock.

---

## 📂 File Requirements

Make sure you have the following CSV files in the same directory as the Python script:

- **Stock.csv** – Format:
  ```
  Τίτλος βιβλίου;Συγγραφέα;Ποσότητα;Κόστος ανά βιβλίο
  Book A;Author A;10;12.50
  Book B;Author B;5;8.30
  ```

- **Paragelia.csv** – Format:
  ```
  Τίτλος βιβλίου;Ποσότητα
  Book A;2
  Book B;1
  ```

Note: All CSV files use `;` as the delimiter and UTF-8 encoding.

---

## 💡 Features

- Loads and displays stock data from `Stock.csv`.
- Asks the user whether to cancel or proceed with the order.
- If accepted:
  - Checks availability of books in the order.
  - Calculates the total cost (to 2 decimal places).
  - Updates the `Stock.csv` file accordingly.
- If stock is insufficient, the order is cancelled and no changes are made.

---

## 🛠️ How to Run

1. Make sure Python 3 is installed.
2. Place `BookstoreOrderManager.py`, `Stock.csv`, and `Paragelia.csv` in the same folder.
3. Open a terminal in that folder and run:

```bash
python BookstoreOrderManager.py
```

---

## 📌 Notes

- The user is prompted whether they want to cancel the order (`y` for yes, `n` for no).
- Updated stock is printed after processing.
- Proper error handling for missing files is included.

---

## ✍️ Author

Created by **Kosmas Nick**  
Student at Hellenic Open University | Aspiring Software Developer & Network Specialist

---

## 📃 License


