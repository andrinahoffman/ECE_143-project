from src.scripts.download import fetch_and_save_data
from src.scripts.read_parse import read_csv_data, parse_data_remove_useless_cols
from src.scripts.analyze import parse_data_count_based_on_col, get_horizontal_table, get_vertical_table
from src.scripts.visualizations.scatter_usa import plot_usa_map_with_data
from src.scripts.visualizations.scatter_world import plot_world_map_with_data
from src.scripts.visualizations.bar_graph import get_bar_graph

#https://github.com/open-numbers/ddf--gapminder--billionaires/blob/bb66a61b5a7432e8db2c93301039167bbab2a9b5/etl/notebooks/scraper.ipynb#L4

def main():
    '''
    main function to download, read, parse, and display data
    return: void
    '''

    important_cols = ['country', 'state', 'gender', 'age', 'industry', 'source']
    # Iterate over the years you want to analyze
    for year in range(2022, 2023):
        # fetch_and_save_data(year) # if you dont have the data saved yet
        data = parse_data_remove_useless_cols(read_csv_data(year))
        allYearData = [parse_data_count_based_on_col(data, col) for col in important_cols]
        
        # countriesDf = allYearData[0]
        statesDf = allYearData[1]

        # plot_world_map_with_data(countriesDf)
        # plot_usa_map_with_data(statesDf)

        horizontal_table = get_horizontal_table(statesDf)
        vertical_table = get_vertical_table(statesDf)
        get_bar_graph(horizontal_table, year)
        get_bar_graph(vertical_table, year)
    

if __name__ == "__main__":
    main()
