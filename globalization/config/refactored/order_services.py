class OrderService:
    def __init__(self, config):
        self.config = config
    
    def process_order(self, order_id):
        # Uses its own config instance
        return retry_operation(order_id, self.config.max_retries)
