import requests

API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"

def fetch_gifs(search_term):
    url = f"https://api.giphy.com/v1/gifs/search?q={search_term}&api_key={API_KEY}&limit=10"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["data"]:
            print(f"✅ Found {len(data['data'])} GIFs for '{search_term}':\n")
            for gif in data["data"]:
                print(f"- {gif['title']}: {gif['url']}")
        else:
            print(f"⚠️ No results found for '{search_term}'. Showing trending GIFs instead.\n")
            show_trending()
    else:
        print("❌ Error fetching data from Giphy.")

def show_trending():
    url = f"https://api.giphy.com/v1/gifs/trending?api_key={API_KEY}&limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("🔥 Trending GIFs:")
        for gif in data["data"]:
            print(f"- {gif['title']}: {gif['url']}")
    else:
        print("❌ Failed to fetch trending GIFs.")

def main():
    search_term = input("Enter a search term: ").strip()
    if not search_term:
        print("⚠️ No input provided. Showing trending GIFs instead.\n")
        show_trending()
    else:
        fetch_gifs(search_term)

if __name__ == "__main__":
    main()
