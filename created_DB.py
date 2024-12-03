import sqlite3
import random
import datetime

# Define SQL commands for creating the tables
create_products_table = '''CREATE TABLE IF NOT EXISTS Products (
                            product_id INTEGER PRIMARY KEY,
                            product_name TEXT,
                            unit_cost DECIMAL(10, 2)
                         )'''

create_customers_table = '''CREATE TABLE IF NOT EXISTS Customers (
                            customer_id INTEGER PRIMARY KEY,
                            first_name TEXT,
                            last_name TEXT,
                            email TEXT,
                            phone TEXT
                         )'''

create_sales_table = '''CREATE TABLE IF NOT EXISTS Sales (
                        sale_id INTEGER PRIMARY KEY,
                        sale_date DATE,
                        customer_id INTEGER,
                        product_id INTEGER,
                        quantity INTEGER,
                        unit_price DECIMAL(10, 2),
                        total_price DECIMAL(10, 2),
                        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
                        FOREIGN KEY (product_id) REFERENCES Products(product_id)
                     )'''

# Define SQL commands for inserting sample data into the tables
insert_products_data = '''INSERT INTO Products (product_name, unit_cost) VALUES (?, ?)'''
insert_customers_data = '''INSERT INTO Customers (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)'''
insert_sales_data = '''INSERT INTO Sales (sale_date, customer_id, product_id, quantity, unit_price, total_price) VALUES (?, ?, ?, ?, ?, ?)'''

# Define sample data for the products and customers tables
Products = [('Product A', 50.00), ('Product B', 25.00), ('Product C', 75.00), ('Product D', 40.00), ('Product E', 60.00)]

Customers = [
    ('John', 'Doe', 'johndoe@example.com', '555-1234'),
    ('Jane', 'Doe', 'janedoe@example.com', '555-5678'),
    ('Bob', 'Smith', 'bobsmith@example.com', '555-9012'),
    ('Alice', 'Jones', 'alicejones@example.com', '555-3456'),
    ('David', 'Brown', 'davidbrown@example.com', '555-7890'),
    ('Emily', 'Davis', 'emilydavis@example.com', '555-2345'),
    ('Frank', 'Wilson', 'frankwilson@example.com', '555-6789'),
    ('Grace', 'Lee', 'gracelee@example.com', '555-1234'),
    ('Henry', 'Chen', 'henrychen@example.com', '555-5678'),
    ('Isabel', 'Garcia', 'isabelgarcia@example.com', '555-9012')
]

# Define the start and end dates for generating sales data
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)

# Connect to the database and create the tables
with sqlite3.connect('Sales.db') as conn:
    cursor = conn.cursor()
    
    # Create the tables
    cursor.execute(create_sales_table)
    cursor.execute(create_products_table)
    cursor.execute(create_customers_table)
    
    # Insert sample data into the products table
    for product in Products:
        cursor.execute(insert_products_data, product)
    
    # Insert sample data into the customers table
    for customer in Customers:
        cursor.execute(insert_customers_data, customer)
    
    # Insert sample data into the sales table
    for i in range(1000):
        sale_date = start_date + datetime.timedelta(days=random.randint(0, 364))
        customer_id = random.randint(1, len(Customers))
        product_id = random.randint(1, len(Products))
        quantity = random.randint(1, 10)
        unit_price = Products[product_id - 1][1]
        total_price = quantity * unit_price
        cursor.execute(insert_sales_data, (sale_date, customer_id, product_id, quantity, unit_price, total_price))
    
    # Commit the changes
    conn.commit()
    
    print("Database successfully created!")
    
    # Retrieve and print records from the Products table
    cursor.execute('SELECT * FROM Products')
    records = cursor.fetchall()

print("Records in the Products table:")
for record in records:
    print(record)
