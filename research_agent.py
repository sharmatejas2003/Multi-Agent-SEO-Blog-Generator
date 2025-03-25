import requests
from bs4 import BeautifulSoup

def fetch_trending_hr_topics():
    url = "https://www.hrdive.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    topics = [headline.text.strip() for headline in soup.find_all("h3")][:5]  # Extract top 5 topics
    return topics if topics else ["HR Trends in 2025"]  # Fallback topic

if __name__ == "__main__":
    print(fetch_trending_hr_topics())
