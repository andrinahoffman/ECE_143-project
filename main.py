import pandas as pd
import requests as req
import csv

#https://github.com/open-numbers/ddf--gapminder--billionaires/blob/bb66a61b5a7432e8db2c93301039167bbab2a9b5/etl/notebooks/scraper.ipynb#L4

# Function to fetch and save data for a given year
def fetch_and_save_data(year):
    '''
    go to the given year and download the data from forbes
    year: integer of the year
    return: void
    '''
    url = f"https://www.forbes.com/ajax/list/data?year={year}&uri=billionaires&type=person"
    response = req.get(url)
    data = response.json()
    headers = ['position', 'rank', 'name', 'lastName', 'uri', 'imageUri', 'worth', 'salary', 'managementAssets', 'government', 'title', 'pay', 'headquarters', 'state', 'age', 'source', 'industry', 'gender', 'country', 'timestamp', 'squareImage', 'worthChange', 'realTimeWorth', 'realTimeRank', 'realTimePosition']

    with open(f'raw_data/billionaires_{year}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for billionaire in data:
            writer.writerow(billionaire)
    csvfile.close()
    print(f"Billionaires data for {year} saved successfully.")


def read_csv_data(year):
    '''
    look at a given year csv file previously downloaded
    year: integer of the year
    return: dataframe
    '''
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f'raw_data/billionaires_{year}.csv')
    # col = 'realTimePosition'
    # df_uri_notna = df[(df[col].notna()) & (df[col] != 0.0)] # check out many non empty values are in a given column
    return df

def parse_data_remove_useless_cols(df):
    '''
    removing some columns because they might not be useful or dont contain enough data
    df: dataframe
    return: dataframe
    '''
    columns_to_remove = ['government', 'imageUri', 'managementAssets', 'pay', 'salary', 'squareImage', 'uri']  # Add the names of the columns you want to remove
    df = df.drop(columns=columns_to_remove)
    return df

def parse_data_count_based_on_col(df, col):
    df_source_counts = df.groupby(col).size().reset_index(name='#_of_people').sort_values(by='#_of_people', ascending=False)
    return df_source_counts

def main():
    '''
    main function to download, read, parse, and display data
    return: void
    '''

    all_years = []
    # Iterate over the years you want to analyze
    for year in range(2020, 2023):
        # fetch_and_save_data(year) # if you dont have the data saved yet
        data = parse_data_remove_useless_cols(read_csv_data(year))
        all_years.append(data)
    
    # count the amount for each important col
    important_cols = ['country', 'state', 'gender', 'age', 'industry', 'source']
    for data in all_years:
        print([parse_data_count_based_on_col(data, col) for col in important_cols])

if __name__ == "__main__":
    main()
