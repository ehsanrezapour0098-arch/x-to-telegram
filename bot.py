import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

SOURCE = "https://www.twstalker.com/MadridXtra"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Get MadridXtra page
r = requests.get(SOURCE, headers=headers, timeout=30)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

# Extract visible text
text = soup.get_text(" ", strip=True)

# Keep message reasonably short for test
text = text[:2500]

message = (
    "🚨 MadridXtra TEST\n\n"
    + text +
    "\n\n🔗 https://x.com/MadridXtra"
)

telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(
    telegram_url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    },
    timeout=30
)

response.raise_for_status()

print("Sent successfully!")
