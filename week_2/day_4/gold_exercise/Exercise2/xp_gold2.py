import requests

API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
query = "hilarious"
rating = "g"
limit = 10

url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={rating}&api_key={API_KEY}&limit={limit}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    gifs = [gif for gif in data["data"] if int(gif["images"]["original"]["height"]) > 100]
    
    print(f"✅ Number of GIFs found: {len(gifs)}\n")
    for gif in gifs[:10]:
        print(f"- {gif['title']}: {gif['url']}")
else:
    print("❌ Failed to fetch GIFs. Status code:", response.status_code)
