import config

def fetch_user(user_id):
    if config.DEBUG_MODE:
        print(f"Fetching user {user_id}")
    # Uses global config directly
    response = api_call(user_id, timeout=config.API_TIMEOUT)
    return response



