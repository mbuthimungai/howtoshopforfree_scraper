# howtoshopforfree_scraper

## Description
`howtoshopforfree_scraper` is a web scraping tool designed to extract deals from the [How To Shop For Free](https://www.howtoshopforfree.net/) website. It automates the process of gathering deal information and sends this data to a specified Discord channel for easy access and real-time updates.

## Features
- Automatically scrapes the latest deals from How To Shop For Free.
- Parses deal information including titles, images, and links.
- Sends structured deal information to a designated Discord channel.
- Offers real-time deal updates to keep users informed about new opportunities.

## Installation

To use `howtoshopforfree_scraper`, you need to have Python installed on your system. Follow these steps to set it up:

2. Navigate to the extracted repository:
   ```bash
   cd howtoshopforfree_scraper
   ```
3. Install `virtualenv` if you haven't already:
   ```bash
   pip install virtualenv
   ```
4. Create a virtual environment:
   ```bash
   virtualenv venv
   ```
5. Activate the virtual environment:

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
6. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the scraper, execute the following command:

```bash
python main.py
```

Make sure to configure your Discord webhook URL in the script to receive the deal alerts.

## Configuration

1. **Discord Webhook**: Set up a Discord webhook in your desired channel and add the webhook URL to the script.

2. **Customization**: You can customize the frequency of scrapes and specific deal categories in the script as per your requirements.
