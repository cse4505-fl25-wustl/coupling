class UserService:
    def __init__(self, config):
        self.config = config
    
    def fetch_user(self, user_id):
        if self.config.debug:
            print(f"Fetching user {user_id}")
        response = api_call(user_id, timeout=self.config.api_timeout)
        return response
