import config

def process_order(order_id):
    # This affects ALL modules using MAX_RETRIES
    config.MAX_RETRIES = 5
    return retry_operation(order_id, config.MAX_RETRIES)
