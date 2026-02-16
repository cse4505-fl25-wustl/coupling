# Scenario 3: Chained Function Call

Consider a customer loyalty module within an e-commerce platform. When a user reaches a certain milestone, an administrative script updates their specific discount settings.

We navigate through the internal relationships of the objects to reach the specific property we want to change.

```python
def upgrade_user_tier(order):
    # The manager reaches through the Order to the Customer, 
    # then to the LoyaltyProgram, then to TierSettings to assign a value.
    order.get_customer().get_loyalty_program().get_tier_settings().set_min_spend(500)
    print("User tier spend requirement updated.")

def reset_loyalty(order):
    # This also depends on the internal structure of 4 different classes
    order.get_customer().get_loyalty_program().get_tier_settings().set_points_multiplier(1.0)

```

The system relies on the exact path between these four distinct classes remaining identical across the entire application.

**Question:** Does this create high coupling?
