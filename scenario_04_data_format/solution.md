# Scenario 1: Configuration - Solution

**Answer: High Coupling**

**Explanation:** If the vendor decides to add a "Description" column as the second item in the CSV, or if they switch from a CSV to a JSON API, the business logic itself breaks. Even though the "Low stock alert" rules haven't changed, the code fails because it is too intimately familiar with how the data was stored on disk.

**Solution:** Separate input data parsing from business logic. 
Introducing Data Transfer Objects (DTO) - light weight objects for simply passing data to and from application layer.

```python
# application/dto/inventory_item.py
from dataclasses import dataclass

@dataclass
class InventoryItem:
    sku: str
    price: float
    quantity: int

```

We will parse CSV into InventoryItem objects outside of the application layer.

```python
# csv_adapter.py
import csv
from models import InventoryItem

def parse_inventory_csv(file_path):
    items = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f) # Using DictReader makes it less sensitive to column order
        for row in reader:
            items.append(InventoryItem(
                sku=row['sku'],
                price=float(row['price']),
                quantity=int(row['quantity'])
            ))
    return items
```

Now, we can decouple business logic from format with:
```python
# inventory_manager.py (Business Logic)

def process_bulk_update(inventory_items):
    for item in inventory_items:
        # Logic is now clean and readable
        if item.quantity < 10:
            print(f"Alert: Low stock for {item.sku} at ${item.price}")
        
        update_database(item.sku, item.quantity)
```

In the decoupled version, the inventory items could come from CSV, database, API, etc. The busienss logic is unaware of the external format of this data. If the external format changes, we can add a new parser to handle this new format.
