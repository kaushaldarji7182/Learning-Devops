import requests

def fetch_data(url):
    """Fetches data from a given URL."""
    response = requests.get(url)
    return response.json()  # Returns JSON response
