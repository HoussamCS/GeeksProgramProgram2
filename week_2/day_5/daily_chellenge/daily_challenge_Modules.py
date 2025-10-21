# --------------------------------------------
#  Daily Challenge: Modules
# --------------------------------------------

"""
Goal:
Using the requests and time modules, create a function that returns
how long it takes for a webpage to load (in seconds).
We'll test it with multiple websites.
"""

import requests
import time

def measure_load_time(url):
    """Return how long it takes for a webpage to fully respond."""
    start = time.time()
    try:
        response = requests.get(url)
        end = time.time()
        load_time = end - start
        print(f"✅ {url} loaded in {load_time:.3f} seconds (Status: {response.status_code})")
        return load_time
    except requests.exceptions.RequestException as e:
        print(f"❌ Error loading {url}: {e}")
        return None


#  Test with multiple sites
if __name__ == "__main__":
    websites = [
        "https://www.google.com",
        "https://www.ynet.co.il",
        "https://www.imdb.com",
        "https://www.wikipedia.org",
        "https://www.python.org"
    ]

    print("🌍 Measuring website load times...\n")
    for site in websites:
        measure_load_time(site)
