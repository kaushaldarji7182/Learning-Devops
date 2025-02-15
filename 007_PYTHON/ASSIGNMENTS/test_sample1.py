#Mock a function in a unit test to simulate behavior without executing the actual code.
import unittest
from unittest.mock import patch
from sample1 import fetch_data  # Import the function to be tested

class TestFetchData(unittest.TestCase):

    @patch("sample1.requests.get")  # Mock requests.get()
    def test_fetch_data(self, mock_get):
        """Test fetch_data() with mocked API response."""
        
        # Define fake response data
        mock_get.return_value.json.return_value = {"status": "success", "data": "mocked result"}

        # Call the function
        result = fetch_data("http://example.com/api")

        # Verify expected behavior
        self.assertEqual(result, {"status": "success", "data": "mocked result"})
        mock_get.assert_called_once_with("http://example.com/api")  # Ensure it was called correctly

if __name__ == "__main__":
    unittest.main()
