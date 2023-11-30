import requests
from bs4 import BeautifulSoup
import random
from discord_bot.bot import send_discord_message

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
    "Mozilla/5.0 (iPad; CPU OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 8.0; SM-N960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36"
]


def send_request(link: str) -> str:
    # Randomly select a user agent
    user_agent = random.choice(USER_AGENTS)
    
    # Set up headers with the selected user agent
    headers = {'User-Agent': user_agent}

    # Send the request with the headers
    res = requests.get(link, headers=headers, verify=False)
    return res.text

def scrape_deals(link: dict):
    response = send_request(link["link"])
    soup = BeautifulSoup(response, "html.parser")
    page_scraper(soup=soup, webhook=link["webhook"])
    
    next_page_link = find_next_page(soup=soup)
    
    while next_page_link:
    
        response = send_request(next_page_link)
        soup = BeautifulSoup(response, "html.parser")
        page_scraper(soup=soup, webhook=link["webhook"])
        next_page_link = find_next_page(soup=soup)
    
        
def find_next_page(soup: BeautifulSoup):
    # Find next page link
    next_page_div = soup.find('div', class_='pagination-next alignright')
    next_page_link_tag = next_page_div.find("a") if next_page_div else None
    next_page_link = next_page_link_tag["href"] if next_page_link_tag else None
    return next_page_link
    
def page_scraper(soup: BeautifulSoup, webhook: str):
    # Find all instances of the specified element
    entries = soup.find_all('header', class_='entry-header')

    # Extract the required information
    for entry in entries:
        # Get the title
        title = entry.find('h2', class_='entry-title').get_text(strip=True)
        
        # Get the image link
        image_tag = entry.find('img', class_='post-image entry-image')
        
        image_link = "https:" +image_tag['data-lazy-src'] if image_tag else None

        # Get the author and the author link
        author_tag = entry.find('span', class_='entry-author-name')
        author = author_tag.get_text(strip=True) if author_tag else None
        author_link_tag = entry.find('a', class_='entry-author-link')
        author_link = author_link_tag['href'] if author_link_tag else None
        
        # Get the "View Post" link
        view_post_link_tag = entry.find('a', class_='entry-title-link')
        view_post_link = view_post_link_tag['href'] if view_post_link_tag else None
        send_discord_message(webhook_url=webhook, title=title, image_link=image_link,
                             author=author, author_link=author_link, post_link=view_post_link)
        # print(f"Title: {title}\nImage Link: {image_link}\nAuthor: {author}\nAuthor Link: {author_link}\nPost Link: {view_post_link}\n\n")
    