import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for Indeed job search (example: Data Analyst jobs)
url = "https://www.indeed.com/jobs?q=data+analyst&l="

# Send a GET request to fetch the raw HTML content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize lists to store the job data
job_titles = []
companies = []
locations = []
job_urls = []

# Find all the job postings
for job_card in soup.find_all('div', class_='jobsearch-SerpJobCard'):
    # Extract the job title
    title = job_card.find('h2', class_='title').text.strip()
    job_titles.append(title)
    
    # Extract the company name
    company = job_card.find('span', class_='company').text.strip()
    companies.append(company)
    
    # Extract the location
    location = job_card.find('div', class_='recJobLoc')['data-rc-loc']
    locations.append(location)
    
    # Extract job URL
    job_url = job_card.find('a')['href']
    full_url = "https://www.indeed.com" + job_url
    job_urls.append(full_url)

# Create a DataFrame to store the results
jobs_df = pd.DataFrame({
    'Job Title': job_titles,
    'Company': companies,
    'Location': locations,
    'Job URL': job_urls
})

# Save the DataFrame to a CSV file
jobs_df.to_csv('indeed_jobs.csv', index=False)

print("Scraping completed. Jobs saved to indeed_jobs.csv")
