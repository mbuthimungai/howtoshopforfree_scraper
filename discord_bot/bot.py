import requests
import json
import time

def send_discord_message(webhook_url, title, image_link, author, author_link, post_link, description=None, destination_link=None):
    # Prepare the embed
    embed = {
        "title": title,
        "url": post_link,
        "description": description,
        "author": {
            "name": author,
            "url": author_link
        },
        "fields": [
            {
                "name": "Destination Link",
                "value": destination_link or "No link provided"
            }
        ] if destination_link else [],
        "image": {
            "url": image_link
        } if image_link else {}
    }

    # Prepare the payload with embed
    data = {"embeds": [embed]}

    # Set the headers
    headers = {"Content-Type": "application/json"}

    # Function to post the message with retry logic
    def post_message():
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        return response

    # Attempt to send the message with retries
    max_retries = 5
    retry_delay = 10  # seconds
    for attempt in range(max_retries):
        response = post_message()
        if response.status_code == 204:
            print("Message sent successfully")
            break
        elif response.status_code == 429:
            print(f"Rate limit hit, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print(f"Failed to send message: {response.status_code}")
            break

# Example usage with description and destination_link
# description_text = "On your mark get set RUNN!!!\n\nRight now on Amazon you can get a case of 8 bottles of Seventh Generation Stain remover for $4.99\n\nRegular price is $59.99\n\nThat’s an insane price and most likely a glitch so go scoop it up now while you can and be stain free for life!!\n\nGet this deal on Amazon HERE"
# send_discord_message(webhook_url, title, image_link, author, author_link, post_link, description=description_text, destination_link="https://example.com")
