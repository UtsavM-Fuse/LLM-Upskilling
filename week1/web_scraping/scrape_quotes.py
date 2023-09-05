import os
import argparse
import requests
from bs4 import BeautifulSoup
import csv


class QuoteScraper:
    """
    A class for scraping quotes from a website and saving them to a CSV file.

    Attributes:
        url (str): The URL of the website containing quotes.
        output_filename (str): The output directory and filename for the CSV file.
    """

    def __init__(self, url, output_filename):
        """
        Initializes the QuoteScraper object.

        Args:
            url (str): The URL of the website containing quotes.
            output_filename (str): The output directory and filename for the CSV file.
        """
        self.url = url
        self.output_filename = output_filename

    def scrape_quotes(self):
        """
        Scrapes quotes from the website.

        Returns:
            list: A list of lists containing quote data (text, author, tags).
        """
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, "html.parser")
        quotes = soup.find_all("div", class_="quote")
        quote_data = []

        for quote in quotes:
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            tags = [tag.text.strip() for tag in quote.find_all("a", class_="tag")]

            quote_data.append([text, author, tags])

        return quote_data

    def save_to_csv(self, quote_data):
        """
        Saves quote data to a CSV file.

        Args:
            quote_data (list): A list of lists containing quote data.

        Returns:
            None
        """
        file_path = os.path.abspath(self.output_filename)
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote Text", "Author", "Tags"])  # Write header row
            writer.writerows(quote_data)

        print(f"Scraped {len(quote_data)} quotes. Data saved to '{file_path}'")


if __name__ == "__main__":
    """
    Driver function to run the quote scraping script.
    """
    parser = argparse.ArgumentParser(
        description="Scrape quotes from a website and save them to a CSV file."
    )
    parser.add_argument(
        "--url",
        default="https://quotes.toscrape.com",
        help="URL of the website containing quotes",
    )
    parser.add_argument(
        "--output-filename",
        default="./outputs/quotes_scraped.csv",
        help="Output directory and filename for the CSV file",
    )
    args = parser.parse_args()

    scraper = QuoteScraper(args.url, args.output_filename)
    quote_data = scraper.scrape_quotes()
    scraper.save_to_csv(quote_data)
