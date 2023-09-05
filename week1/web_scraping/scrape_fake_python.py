import os
import argparse
import requests
from bs4 import BeautifulSoup
import csv


class JobScraper:
    """
    A class for scraping job listings from a website and saving them to a CSV file.

    Attributes:
        url (str): The URL of the website containing job listings.
        output_filename (str): The output directory and filename for the CSV file.
    """

    def __init__(self, url, output_filename):
        """
        Initializes the JobScraper object.

        Args:
            url (str): The URL of the website containing job listings.
            output_filename (str): The output directory and filename for the CSV file.
        """
        self.url = url
        self.output_filename = output_filename

    def scrape_jobs(self):
        """
        Scrapes job listings from the website.

        Returns:
            list: A list of lists containing job data (title, company, location, date posted).
        """
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, "lxml")
        jobs = soup.find_all("div", class_="card-content")
        job_data = []

        for job in jobs:
            title = job.find("h2", class_="title is-5").text.strip()
            company = job.find("h3", class_="subtitle is-6 company").text.strip()
            location = job.find("p", class_="location").text.strip()
            date_posted = job.find("time")["datetime"]

            job_data.append([title, company, location, date_posted])

        return job_data

    def save_to_csv(self, job_data):
        """
        Saves job data to a CSV file.

        Args:
            job_data (list): A list of lists containing job data.

        Returns:
            None
        """
        file_path = os.path.abspath(self.output_filename)
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Title", "Company", "Location", "Date Posted"]
            )  # Write header row
            writer.writerows(job_data)

        print(f"Scraped {len(job_data)} jobs. Data saved to '{file_path}'")


if __name__ == "__main__":
    """
    Main function to run the job scraping script.
    """
    parser = argparse.ArgumentParser(
        description="Scrape job listings from a website and save them to a CSV file."
    )
    parser.add_argument(
        "--url",
        default="https://realpython.github.io/fake-jobs/",
        help="URL of the website containing job listings",
    )
    parser.add_argument(
        "--output-filename",
        default="./outputs/job_data_scraped.csv",
        help="Output directory and filename for the CSV file",
    )
    args = parser.parse_args()

    scraper = JobScraper(args.url, args.output_filename)
    job_data = scraper.scrape_jobs()
    scraper.save_to_csv(job_data)
