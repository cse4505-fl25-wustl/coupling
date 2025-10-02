# Scenario 1: Configuration

Suppose we have the following configuration variables and settings:

```python
# config.py
DEBUG_MODE = True
MAX_RETRIES = 3
API_TIMEOUT = 30
```

Multiple services use the configuration settings

```python
# user_service.py

import config

def fetch_user(user_id):
    if config.DEBUG_MODE:
        print(f"Fetching user {user_id}")
    # Uses global config directly
    response = api_call(user_id, timeout=config.API_TIMEOUT)
    return response
```

One of the services, adjusts `MAX_RETRIES` configuration setting based on its needs.
```python
# order_service.py

import config

def process_order(order_id):
    # This affects ALL modules using MAX_RETRIES
    config.MAX_RETRIES = 5
    return retry_operation(order_id, config.MAX_RETRIES)
```

**Question:** Does this create high coupling?
