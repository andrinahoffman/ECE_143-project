def parse_data_count_based_on_col(df, col):
    '''
    this will make a new dataframe that counts the occurrence for the column given
    df: dataframe of all data
    col: column to count
    return: dataframe
    '''
    df_source_counts = df.groupby(col).size().reset_index(name='#_of_people').sort_values(by='#_of_people', ascending=False)
    return df_source_counts
