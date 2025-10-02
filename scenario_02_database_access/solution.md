# Scenario 2: Database Access - Solution

**Answer: High Coupling**

**Explanation:** Business logic, such as calculating the final price, is coupled to database schema and mysql functionality. If we change the schema or choose to use a different database, we would need to update code that contains business logic. Additionally, we'll need to that everywhere where our business logic relies on mysql.

**Solution:** Encapsulate database access in a dedicated module, hiding behind  a well defined interface. All modules that need to communicate with the database must go through your dedicated module. No module cares about how exactly the data is stored or retrieved, they rely on your well-defined interface. This interface can be abstracted out, to make your application even more flexible.

First, let's define the interface for accessing a pricing repository.
```python
# interfaces.py

from typing import Protocol, List

class PricingRepository(Protocol):
    """
    Defines the contract for any class that provides access to product
    pricing and tax rate data.
    """
    def get_product_price(self, product_id: int) -> float:
        """Fetches the price for a single product ID."""
        ...

    def get_tax_rate(self, state: str) -> float:
        """Fetches the sales tax rate for a given state."""
        ...
```

We can have one or more concrete implementations of this interface.

```python
# repositories.py
import mysql.connector
from interfaces import PricingRepository # Import the interface

class SQLPricingRepository(PricingRepository):
    """A concrete implementation that gets data from a MySQL database."""
    
    def __init__(self, db_config: dict):
        # In a real app, connection management would be more robust
        self._connection = mysql.connector.connect(**db_config)

    def get_product_price(self, product_id: int) -> float:
        cursor = self._connection.cursor()
        cursor.execute("SELECT price FROM Products WHERE id = %s", (product_id,))
        price = cursor.fetchone()[0]
        cursor.close()
        return float(price)

    def get_tax_rate(self, state: str) -> float:
        cursor = self._connection.cursor()
        cursor.execute("SELECT tax_rate FROM TaxRates WHERE state = %s", (state,))
        tax_rate = cursor.fetchone()[0]
        cursor.close()
        return float(tax_rate)
```

And now, let's updte the business logic such that it depends on the PricingRepository interface, rather than mysql.

```python
# cart_calculator.py
from typing import List
from interfaces import PricingRepository

def calculate_final_price(
    product_ids: List[int],
    user_location: str,
    repository: PricingRepository) -> float:
    """
    Calculates the total price of a list of products, including tax.
    
    This function is completely decoupled from the data source.
    """
    # Calculate subtotal by calling the repository's method
    subtotal = sum(repository.get_product_price(pid) for pid in product_ids)
    
    # Get the tax rate from the repository
    tax_rate = repository.get_tax_rate(user_location)
    
    final_price = subtotal * (1 + tax_rate)
    return round(final_price, 2)
```

```python
# main.py
# Example usage scenario (using the real database)
db_config = {"user": "root", "database": "ecommerce"}
sql_repo = SQLPricingRepository(db_config)
final_price = calculate_final_price([101, 205], "CA", sql_repo)
print(f"Production Price (from DB): ${final_price}")
```
