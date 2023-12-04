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

1. Clone the repository:
   ```bash
   git clone https://github.com/mbuthi/howtoshopforfree_scraper.git
   ```
2. Navigate to the cloned repository:
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

## Contributing
Contributions to `howtoshopforfree_scraper` are welcome! Feel free to fork the repository, make changes, and submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE file for details.

## Disclaimer
This tool is intended for educational purposes only. Please respect the [How To Shop For Free](https://www.howtoshopforfree.net/) website's terms of use.

## Contact
For any queries or suggestions, feel free to contact [Twitter](https://twitter.com/MungaiMbuthi).
