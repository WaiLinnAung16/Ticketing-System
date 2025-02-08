class EmptyInput(Exception):
    """Custom exception for empty input validation."""
    def __init__(self, field_name):
        self.field_name = field_name
        self.message = f"{field_name} cannot be empty!"
        super().__init__(self.message)



class AuthenticationError(Exception):
    """Custom exception for authentication failures."""
    def __init__(self, message):
        super().__init__(message)