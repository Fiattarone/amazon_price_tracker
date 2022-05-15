import requests
from bs4 import BeautifulSoup
from pprint import pprint
import lxml
import smtplib

# - 1 Shirt Press
LOWEST_PRICE = 449.00

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
    current_price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
    if LOWEST_PRICE > current_price:
        my_email: str
        my_password: str
        email: str
        with smtplib.SMTP("smtp.gmail.com", port=587) as econnection:
            econnection.starttls()
            econnection.login(user=my_email, password=my_password)
            econnection.sendmail(from_addr=my_email, to_addrs=email,
                                         msg=f"subject: AMAZON DEAL ALERT!\n\nURL: {url} CURRENT PRICE: {current_price} ")
