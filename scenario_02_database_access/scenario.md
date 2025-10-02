# Scenario 2: Database Access

Consider an e-commerce application, where the user can add items to the shopping cart and purchase those items.

We define a database connection in our main script and pass that connection to the different operations, such as calculate_final_price.

```python

# main.py
import mysql.connector
DB_CONNECTION = mysql.connector.connect(user='root', database='ecommerce')
final_price = calculate_final_price([101, 205], "CA", DB_CONNECTION)
```

We use the database connection passed to our business logic, accessing the database directly and using functions from mysql package.

```python
# cart_calculator.py (business logic)

def calculate_final_price(product_ids, user_location, db_connection):
    cursor = db_connection.cursor()
    
    # Direct SQL query to get prices
    total_price = 0
    for product_id in product_ids:
        cursor.execute(f"SELECT price FROM Products WHERE id = {product_id}")
        price = cursor.fetchone()[0]
        total_price += price
        
    # Another direct SQL query to get tax rate
    cursor.execute(f"SELECT tax_rate FROM TaxRates WHERE state = '{user_location}'")
    tax_rate = cursor.fetchone()[0]
    
    final_price = total_price * (1 + tax_rate)
    cursor.close()
    
    return final_price

# Any other part of the app can also do this...
# user_profile.py
# db_connection.cursor().execute("UPDATE Users SET ...")
```

**Question:** Is this high coupling?
