class Config:
    def __init__(self, debug=False, max_retries=3, api_timeout=30):
        self.debug = debug
        self.max_retries = max_retries
        self.api_timeout = api_timeout
