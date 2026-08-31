import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

SOURCE = "https://www.sotwe.com/adrirm33"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("Downloading AdriRM33...")

r = requests.get(SOURCE, headers=headers, timeout=30)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")

# Find page text
text = soup.get_text("\n", strip=True)

# Find AdriRM33 content in the page
lines = [line.strip() for line in text.splitlines() if line.strip()]

# Remove obvious page/menu junk
bad_words = [
    "Twitter Profile",
    "Followers",
    "Following",
    "Joined",
    "Who to follow",
    "Pinned Tweet"
]

clean_lines = []

for line in lines:
    if not any(word.lower() in line.lower() for word in bad_words):
        clean_lines.append(line)

# Take a chunk from the beginning for this test
post_text = "\n".join(clean_lines[:25])

if not post_text:
    raise RuntimeError("Could not extract post text from Sotwe")

message = (
    "🚨 AdriRM33 TEST\n\n"
    + post_text[:3000]
    + "\n\n🔗 https://x.com/AdriRM33"
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

print("Latest content sent to Telegram!")
