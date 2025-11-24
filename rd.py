import requests
import json

def fetch_redgifs(subreddit, limit=100):
    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=all&limit={limit}"

    headers = {
        "User-Agent": "Mozilla/5.0 (RedgifsFetcher)"
    }

    res = requests.get(url, headers=headers)
    data = res.json()

    redgifs_links = []

    for post in data.get("data", {}).get("children", []):
        post_url = post["data"].get("url", "").lower()
        if "redgifs.com" in post_url:
            redgifs_links.append(post["data"]["url"])

    return redgifs_links


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ").strip()
    number_of_links = int(input("Enter number of posts to fetch: ").strip())

    links = fetch_redgifs(subreddit, limit=number_of_links)

    print(f"Found {len(links)} redgifs links")

    # Save to JSON file
    filename = "input.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(links, f, indent=2)

    print(f"Saved to {filename}")
