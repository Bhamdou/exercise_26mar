import requests
from bs4 import BeautifulSoup

def get_job_postings(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    job_posts = soup.find_all('div', class_='job-post')

    return job_posts

def print_job_postings(job_posts):
    for job in job_posts:
        title = job.find('h2', class_='job-title').text
        company = job.find('h3', class_='company-name').text
        location = job.find('span', class_='job-location').text
        print(f"Job Title: {title}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print('-' * 40)

def main():
    job_listing_url = "https://www.example.com/job-listings"  # Replace with a real job listing URL
    try:
        job_postings = get_job_postings(job_listing_url)
        print_job_postings(job_postings)
    except Exception as e:
        print("Error fetching job postings:", e)

if __name__ == "__main__":
    main()
