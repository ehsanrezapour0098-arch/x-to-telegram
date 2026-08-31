import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

SOURCE = "https://www.sotwe.com/adrirm33"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Testing Sotwe connection...")

r = requests.get(SOURCE, headers=headers, timeout=30)

print("Status code:", r.status_code)

# Stop here if Sotwe blocks GitHub
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text(" ", strip=True)

print("Page downloaded successfully!")
print("Page length:", len(r.text))

message = (
    "✅ Sotwe connection successful!\n\n"
    "GitHub Actions can access AdriRM33.\n\n"
    f"HTTP Status: {r.status_code}\n"
    f"Page size: {len(r.text)} characters\n\n"
    "🔗 https://x.com/AdriRM33"
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

print("Telegram message sent successfully!")
