import pandas as pd

def read_csv_data(year):
    '''
    look at a given year csv file previously downloaded
    year: integer of the year
    return: dataframe
    '''
    # Read the CSV file into a DataFrame
    df = pd.read_csv(f'src/data/billionaires_{year}.csv')
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
