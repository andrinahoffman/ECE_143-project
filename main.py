from src.scripts.download import fetch_and_save_data
from src.scripts.read_parse import read_csv_data, parse_data_remove_useless_cols
from src.scripts.analyze import parse_data_count_based_on_col

#https://github.com/open-numbers/ddf--gapminder--billionaires/blob/bb66a61b5a7432e8db2c93301039167bbab2a9b5/etl/notebooks/scraper.ipynb#L4

def main():
    '''
    main function to download, read, parse, and display data
    return: void
    '''
    all_years = []
    # Iterate over the years you want to analyze
    for year in range(2020, 2023):
        fetch_and_save_data(year) # if you dont have the data saved yet
        data = parse_data_remove_useless_cols(read_csv_data(year))
        all_years.append(data)
    
    important_cols = ['country', 'state', 'gender', 'age', 'industry', 'source']
    for data in all_years:
        print([parse_data_count_based_on_col(data, col) for col in important_cols])

if __name__ == "__main__":
    main()
