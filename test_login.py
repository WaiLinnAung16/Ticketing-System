import unittest
from app import authenticate  # Import your function from the correct module

class test_authentication(unittest.TestCase):
    def test_valid_credentials(self):
        """Test login with correct credentials."""
        self.assertTrue(authenticate("admin", "admin123"))
    def test_invalid_username(self):
        """Test login with incorrect username."""
        self.assertFalse(authenticate("wrongUser", "admin123"))
    def test_invalid_password(self):
        """Test login with incorrect password."""
        self.assertFalse(authenticate("admin", "wrongPass"))
    def test_empty_username(self):
        """Test login with empty username."""
        self.assertFalse(authenticate("", "admin123"))
    def test_empty_password(self):
        """Test login with empty password."""
        self.assertFalse(authenticate("admin", ""))
    def test_empty_credentials(self):
        """Test login with both username and password empty."""
        self.assertFalse(authenticate("", ""))
if __name__ == '__main__':
    unittest.main()
