# Scenario 4: Data Format

Consider a bulk order processing system that allows vendors to upload their inventory updates via a CSV file.

We pass the raw file path directly into our business logic module.

```python
# main.py
from inventory_manager import process_bulk_update

# The raw file path is passed directly to the business logic
process_bulk_update("vendor_inventory_v1.csv")
```

The business logic is responsible for opening the file, parsing the strings, and handling the specific column indices of the CSV format.

```python
# inventory_manager.py (business logic)

def process_bulk_update(file_path):
    with open(file_path, 'r') as f:
        # Skip header
        next(f)
        for line in f:
            # High coupling: The logic depends on the EXACT order of columns
            # [0] = SKU, [1] = Name, [2] = Price, [3] = Quantity
            data = line.strip().split(',')
            
            sku = data[0]
            price = float(data[2])
            quantity = int(data[3])
            
            # Business logic mixed with parsing logic
            if quantity < 10:
                print(f"Alert: Low stock for {sku} at ${price}")
            
            update_database(sku, quantity)
```
**Question:** Does this create high coupling?
