import requests
import time
import random
from datetime import datetime

url = "thread_link" # change to your thread but add '/add-reply' after your thread link like mines

cookies = {
    "cf_clearance": "",
    "xf_csrf": "",
    "xf_siropu_chat_room_id": "1",
    "xf_push_notice_dismiss": "1",
    "xf_siropu_chat_conv_id": "",
    "xf_siropu_chat_channel": "room",
    "xf_tfa_trust": "",
    "xf_user": "",
    "xf_session": "",
    "xf_emoji_usage": "cookie",
}

# copy ur cookies, u can ask AI to format them if ur lazy xd



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36", # ua; you can change this to your own useragent if u want
    "Referer": "", # thread to postmaxx in
    "Origin": "https://incels.is",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/javascript, */*; q=0.01",
}

message = "postmaxxing"   # postmaxxing msg

data = {
    "_xfToken": "", # get from inspect element
    "message_html": message,
    "attachment_hash": "",
    "_xfRequestUri": "", # change to your thread to postmaxx in
    "_xfWithData": "1",
    "_xfResponseType": "json",
}

print("Press Ctrl+C to stop\n")

count = 0

try:
    while True:
        count += 1
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        response = requests.post(url, headers=headers, cookies=cookies, data=data)
        
        if response.status_code == 200:
            print(f"✅ [{timestamp}] Post #{count} sent successfully!")
        else:
            print(f"❌ [{timestamp}] Error (Status {response.status_code})")
            print(response.text[:300])
        
        # random delay to maybe not be detected xD
        delay = random.uniform(10.0, 13.0)
        print(f"   Waiting {delay:.2f} seconds...\n")
        time.sleep(delay)

except KeyboardInterrupt:
    print(f"\n🛑 Total posts sent: {count}")
except Exception as e:
    print(f"\nError: {e}")
