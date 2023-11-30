import requests
import json

def send_discord_message(webhook_url, title, image_link, author, author_link, post_link):
    # Prepare the embed
    embed = {
        "title": title,
        "url": post_link,
        "author": {
            "name": author,
            "url": author_link
        },
        "image": {
            "url": image_link
        } if image_link else {}
    }

    # Prepare the payload with embed
    data = {"embeds": [embed]}

    # Set the headers
    headers = {"Content-Type": "application/json"}

    # Post the message
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
    # Check if the request was successful
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}")

# # Webhook URL (replace with your actual webhook URL)
# webhook_url = "https://discord.com/api/webhooks/1179465833764892723/UsIIyuxbOVrAcn2Er25jI4XX8edgI70PPWrYwCRHSRh-pl4H98OCgzEV4ARSCUhij_2w"

# # Sample message details
# title = "76% Off Beats Earbuds HURRY This is HOT!!!"
# image_link = None  # Or provide a valid image URL
# author = "kspencer"
# author_link = "https://www.howtoshopforfree.net/author/kspencer/"
# post_link = "https://www.howtoshopforfree.net/76-off-beats-earbuds-hurry-this-is-hot/"

# # Send the message
# send_discord_message(webhook_url, title, image_link, author, author_link, post_link)
