from src.scripts.download import fetch_and_save_data
from src.scripts.read_parse import read_csv_data, parse_data_remove_useless_cols
from src.scripts.analyze import parse_data_count_based_on_col, display_all_graphs
from src.scripts.visualizations.animate_bar_graphs import animate_bar_graphs

#https://github.com/open-numbers/ddf--gapminder--billionaires/blob/bb66a61b5a7432e8db2c93301039167bbab2a9b5/etl/notebooks/scraper.ipynb#L4

def main():
    '''
    Main function to manage data processing and visualization.
    
    This function orchestrates the process of downloading, reading, parsing, and displaying data.
    '''
    # Define the columns that are important for analysis
    important_cols = ['country', 'state', 'gender', 'age', 'industry', 'source', 'name']
    # Define the years for analysis
    years = [year for year in range(2003, 2023)]
    # Initialize an empty dictionary to store categorized DataFrames
    dfs = {}
    # Iterate over the years to analyze data
    for year in years:
        # fetch_and_save_data(year) # if you dont have the data available
        # Read and parse the data for the current year
        data = parse_data_remove_useless_cols(read_csv_data(year))
        # Parse and count data based on important columns
        allYearData = [parse_data_count_based_on_col(data, col) for col in important_cols]
        # Display all graphs based on the parsed data
        dfs = display_all_graphs(allYearData, dfs)

    for key in dfs:
        # Reverse the order of data frames so it starts with earlier years
        dfs[key].reverse()
        # Generate and save animation for each data frame
        animate_bar_graphs(dfs[key], years, key, f"{key}.gif")

if __name__ == "__main__":
    main()
