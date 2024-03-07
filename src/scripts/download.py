import csv
from pathlib import Path

import requests as req

# Function to fetch and save data for a given year
def fetch_and_save_data(year, savedir="src/data"):
    '''
    go to the given year and download the data from forbes
    year: integer of the year
    return: void
    '''
    url = f"https://www.forbes.com/ajax/list/data?year={year}&uri=billionaires&type=person"
    response = req.get(url)
    data = response.json()
    headers = ['position', 'rank', 'name', 'lastName', 'uri', 'imageUri', 'worth', 'salary', 'managementAssets', 'government', 'title', 'pay', 'headquarters', 'state', 'age', 'source', 'industry', 'gender', 'country', 'timestamp', 'squareImage', 'worthChange', 'realTimeWorth', 'realTimeRank', 'realTimePosition']

    with open(Path(savedir) / f"billionaires_{year}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for billionaire in data:
            writer.writerow(billionaire)
    csvfile.close()
    print(f"Billionaires data for {year} saved successfully.")
