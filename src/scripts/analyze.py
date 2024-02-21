def parse_data_count_based_on_col(df, col):
    '''
    this will make a new dataframe that counts the occurrence for the column given
    df: dataframe of all data
    col: column to count
    return: dataframe
    '''
    df_source_counts = df.groupby(col).size().reset_index(name='#_of_people').sort_values(by='#_of_people', ascending=False)
    return df_source_counts

northern_states = ['Washington', 'Oregon', 'Idaho', 'Montana', 'North Dakota', 'South Dakota', 'Minnesota', 'Wisconsin', 'Michigan', 'Wyoming', 'Nebraska', 'Iowa', 'Illinois', 'Indiana', 'Ohio', 'Pennsylvania', 'New York', 'Vermont', 'New Hampshire', 'Maine', 'Massachusetts', 'Connecticut', 'Rhode Island', 'Alaska']
southern_states = ['California', 'Nevada', 'Utah', 'Colorado', 'Kansas', 'Missouri', 'Kentucky', 'West Virginia', 'Virginia', 'Maryland', 'Delaware', 'New Jersey', 'North Carolina', 'South Carolina', 'Tennessee', 'Arkansas', 'Oklahoma', 'Texas', 'Louisiana', 'Mississippi', 'Alabama', 'Georgia', 'Florida', 'Arizona', 'New Mexico', 'Hawaii']

def get_vertical_table(statesDf):
    statesDf['vertical_regions'] = statesDf['state'].apply(assign_vertical_region)
    vertical_table = statesDf.pivot_table(index='vertical_regions', values='#_of_people', aggfunc='sum')
    vertical_table.reset_index(inplace=True)
    return vertical_table

def assign_vertical_region(state):
    if state in northern_states:
        return 'North'
    elif state in southern_states:
        return 'South'
    else:
        return 'International'
    
west_states = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington', 'Idaho', 'Nevada', 'Utah', 'Arizona', 'Montana', 'Wyoming', 'Colorado', 'New Mexico']
midwest_states = ['North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Minnesota', 'Iowa', 'Missouri', 'Wisconsin', 'Illinois', 'Michigan', 'Indiana', 'Ohio']
mid_east_states = ['Texas', 'Oklahoma', 'Arkansas', 'Louisiana', 'Kentucky', 'Tennessee', 'Mississippi', 'Alabama']
east_states = ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'Pennsylvania', 'New Jersey', 'Delaware', 'Maryland', 'West Virginia', 'Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida']

def get_horizontal_table(statesDf):
    statesDf['horizontal_regions'] = statesDf['state'].apply(assign_horizontal_region)
    horizontal_table = statesDf.pivot_table(index='horizontal_regions', values='#_of_people', aggfunc='sum')
    horizontal_table.reset_index(inplace=True)
    return horizontal_table

def assign_horizontal_region(state):
    if state in west_states:
        return 'West'
    elif state in midwest_states:
        return 'Midwest'
    elif state in mid_east_states:
        return 'Mid-East'
    elif state in east_states:
        return 'East'
    else:
        return 'International'
