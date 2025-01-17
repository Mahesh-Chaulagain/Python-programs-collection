# step 1: Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv

# step 2: Define the base URL and CSV headers
def scrape_uci_datasets():
    base_url = "https://archive.ics.uci.edu/datasets"

    headers = [
        "Dataset Name", "Donated Date", "Description",
        "Dataset Characteristics", "Subject Area", "Associated Tasks",
        "Feature Type", "Instances", "Features"
    ]
    
    data = []

# step 3: Create a function to scrape dataset details that takes the URL of an individual dataset page, retrieve the HTML
# content, parse it using BeautifulSoup and extracts relevant information
    def scrape_dataset_details(dataset_url):
        response = requests.get(dataset_url)
        soup = BeautifulSoup(response.text, "html.parser")

        dataset_name = soup.find('h1', class_="text-3xl font-semibold text-primary-content")
        dataset_name = dataset_name.text.strip() if dataset_name else "N/A"

        donated_date = soup.find('h2', class_="text-sm text-primary-content")
        donated_date = donated_date.text.strip().replace("Donated on", "") if donated_date else "N/A"

        description = soup.find('p', class_='svelte-17wf9gp')
        description = description.text.strip() if description else "N/A"

        details = soup.find_all('div', class_="col-span-4")

        dataset_characteristics = details[0].find('p').text.strip() if len(details) > 0 else "N/A"
        subject_area = details[1].find('p').text.strip() if len(details) > 1 else "N/A"
        associated_tasks = details[2].find('p').text.strip() if len(details) > 2 else "N/A"
        features_type = details[3].find('p').text.strip() if len(details) > 3 else "N/A"
        instances = details[4].find('p').text.strip() if len(details) > 4 else "N/A"
        features = details[5].find('p').text.strip() if len(details) > 5 else "N/A"

        return [
            dataset_name, donated_date, description, dataset_characteristics, subject_area, associated_tasks, features_type,
            instances, features
        ]    

    # Step 4: Create a function to scrape dataset listings
    def scrape_dataset(page_url):
        response = requests.get(page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        dataset_list = soup.find_all('a', class_="link-hover link text-xl font-semibold")

        if not dataset_list:
            print("No dataset links found")
            return
        
        for dataset in dataset_list:
            dataset_link = "https://archive.ics.uci.edu" + dataset['href']
            print(f"scrapping details for {dataset.text.strip()}...")
            dataset_details = scrape_dataset_details(dataset_link)
            data.append(dataset_details)

    # Step 5: Loop through pages using pagination parameters
    skip = 0
    take = 10
    while True:
        page_url = f"https://archive.ics.uci.edu/datasets?skip={skip}&take={take}&sort=desc&orderBy=NumHits&search="
        print(f'scrapping page:{page_url}')
        initial_data_count = len(data)
        scrape_dataset(page_url)
        if len(data) == initial_data_count:
            break
        skip += take

# Step 6: Save the scrapped data to a CSV file
    with open('uci_dataset.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Step 7: Run the scrapping function
scrape_uci_datasets()