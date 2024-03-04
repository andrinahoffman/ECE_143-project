"""
Utility functions to read and parse various data.
"""
from pathlib import Path

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

def convert_globwealth_raw(path):
    """
    Converts raw txt data for the "Wealth estimates by country" tables
    from the global-wealth-databook into a useable csv file.

    You'll have to copy and paste from the pdf into a txt file to convert it.
    Some manual correction may be required in the txt.

    Column units can be found in the pdf file.

    Args:
        path (path-like): Path to the raw txt file for wealth estimates.
    
    Returns:
        pd.DataFrame: The parsed data in a dataframe.
    """
    columns = [
        "country",
        "adults",
        "share of adults",
        "total wealth",
        "share of wealth",
        "wealth per adult",
        "financial wealth per adult",
        "non-financial wealth per adult",
        "debt per adult",
        "median wealth per adult",
        "estimation method"
    ]
    path = Path(path)
    dataarr = []
    with open(path, "rt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            lsplit = line.split()
            currdata = []
            currstr = []
            for s in lsplit:
                # Very specific, there are no str columns in the dataset
                # that are adjacent, so after splitting by spaces, we consolidate
                # any adjacent str elements in the list.
                try:
                    num = float(s.replace(",", ""))
                    if len(currstr) > 0:
                        currdata.append(" ".join(currstr))
                        currstr = []
                    currdata.append(num)
                except ValueError:
                    currstr.append(s)
            if len(currstr) > 0:
                currdata.append(" ".join(currstr))
            if len(currdata) == len(columns):
                dataarr.append(currdata)
            else:
                print(f"error with line: {line}")
    df = pd.DataFrame(dataarr, columns=columns)
    return df

def aggregate_globwealth_raw(datadir, startyear, endyear):
    """
    Brings together the raw txt global wealth estimate files into a single dataframe.
    Assumes a specific naming convention for the raw txt files.
        
        wealth-est-{year}-raw.txt

    Adds a new 'year' column to the dataframe.

    Args:
        datadir (path-like): Directory where the raw txt files are located.
        startyear (int): The first year to include.
        endyear (int): The last year to include.
    
    Returns:
        pd.DataFrame: The aggregated dataframe.
    """
    years = range(startyear, endyear + 1)
    alldfs = []
    for y in years:
        rawpath = Path(datadir) / f"wealth-est-{y}-raw.txt"
        df = convert_globwealth_raw(rawpath)
        df["year"] = y
        alldfs.append(df)
    df_agg = pd.concat(alldfs)
    return df_agg
