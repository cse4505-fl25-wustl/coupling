Scenario 1: Configuration - Solution

**Answer: High Coupling**

**Explanation:** Changes to one module,`order_service.py` impacts the `user_service.py` module through changes in global configuration.

**Solution:** Instead of using global configuration, create a separate configuration object and pass it to each service that needs to be configured separately.

```
# config.py

class Config:
    def __init__(self, debug=False, max_retries=3, api_timeout=30):
        self.debug = debug
        self.max_retries = max_retries
        self.api_timeout = api_timeout
```

```
# user_service.py

class UserService:
    def __init__(self, config):
        self.config = config

    def fetch_user(self, user_id):
        if self.config.debug:
            print(f"Fetching user {user_id}")
        response = api_call(user_id, timeout=self.config.api_timeout)
        return response
```

```
# order_service.py

class OrderService:
    def __init__(self, config):
        self.config = config

    def process_order(self, order_id):
        # Uses its own config instance
        return retry_operation(order_id, self.config.max_retries)
```
