import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml


# - 1 Shirt Press

AMAZON_URLS = [
    "https://www.amazon.com/Dulytek-DHP7-Hydraulic-Pressing-Touch-Screen/dp/B07PBD1RH2/ref=sr_1_9?keywords=wax%2Bpress"
    "&qid=1652648560&refinements=p_72%3A2638180011&rnid=2638179011&s=arts-crafts&sr=1-9&th=1"
]

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/101.0.4951.67 Safari/537.36"
}

for url in AMAZON_URLS:
    response = requests.get(url=url, headers=headers)
    # response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    pprint(float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1]))