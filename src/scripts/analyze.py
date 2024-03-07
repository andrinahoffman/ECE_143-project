# from .visualizations.scatter_usa import plot_usa_map_with_data
# from .visualizations.scatter_world import plot_world_map_with_data
# from .visualizations.bar_graph import get_bar_graph

def display_all_graphs(allYearData, dfs):    
    """
    Display all required graphs based on the data.
    
    allYearData: List of DataFrames containing data for each year.
    dfs: Dictionary to store categorized DataFrames.
    
    return: Dictionary containing categorized DataFrames.
    """
    # countriesDf = allYearData[0]
    # statesDf = allYearData[1]
    # make display hot locations in the world and usa
    # plot_world_map_with_data(countriesDf)
    # plot_usa_map_with_data(statesDf)
    for i in range(len(allYearData)):
        df_dict = determine_df(allYearData[i])
        for key, value in df_dict.items():
            if len(dfs.get(key, [])) > 0: 
                dfs[key].append(value)
            else:
                dfs[key] = [value]
    return dfs

def determine_df(df):
    """
    Determine the category of the DataFrame and return it.
    
    df: DataFrame to categorize.
    
    return: Dictionary containing categorized DataFrame.
    """
    col_name = df.columns[0]
    match col_name:
        case 'gender':
            return {col_name: df}
        case 'age':
            return {col_name: df}
        case 'industry':
            return {col_name: df.head(10)}
        case 'source':
            return {col_name: df.head(10)}
        case 'country':
            return {col_name: df.head(30)}
        case 'state':
            return {
                'states east west': build_table(df, 'state', 'states east west', assign_east_west_state_region),
                'states north south': build_table(df, 'state', 'states north south', assign_north_south_state_region)
            }
        case 'name':
            return {
                "first name first letter": build_table(df, 'name', 'first name first letter', assign_based_on_first_letter_first_name),
                "last name first letter": build_table(df, 'name', 'last name first letter', assign_based_on_first_letter_last_name)
            }
        case _:
            return {col_name: df}

def parse_data_count_based_on_col(df, col):
    '''
    Create a new DataFrame that counts the occurrence for the given column.
    
    df: DataFrame of all data.
    col: Column to count.
    
    return: DataFrame.
    '''
    if col == "industry" or col == "source":
        # Convert specific elements to lowercase
        df[col] = df[col].apply(lambda x: x.lower() if isinstance(x, str) else x)
    df_source_counts = df.groupby(col).size().reset_index(name='#_of_people').sort_values(by='#_of_people', ascending=False)
    return df_source_counts

def build_table(df, col, new_col, assignment_method):
    """
    Build a pivot table from DataFrame based on specific column and assignment method.
    
    df: DataFrame.
    col: Column to assign values from.
    new_col: New column name.
    assignment_method: Method to assign values.
    
    return: DataFrame.
    """
    df[new_col] = df[col].apply(assignment_method)
    table = df.pivot_table(index=new_col, values='#_of_people', aggfunc='sum')
    table.reset_index(inplace=True)
    return table

def assign_based_on_first_letter_first_name(name):
    """
    Assign based on the first letter of the first name.
    
    name: Name string.
    
    return: First letter.
    """
    return name[0]

def assign_based_on_first_letter_last_name(name):
    """
    Assign based on the first letter of the last name.
    
    name: Name string.
    
    return: First letter.
    """
    n = name.split()
    if len(n)>1:
        return n[1][0]
    else:
        return n[0][0]

northern_states = ['Washington', 'Oregon', 'Idaho', 'Montana', 'North Dakota', 'South Dakota', 'Minnesota', 'Wisconsin', 'Michigan', 'Wyoming', 'Nebraska', 'Iowa', 'Illinois', 'Indiana', 'Ohio', 'Pennsylvania', 'New York', 'Vermont', 'New Hampshire', 'Maine', 'Massachusetts', 'Connecticut', 'Rhode Island', 'Alaska']
southern_states = ['California', 'Nevada', 'Utah', 'Colorado', 'Kansas', 'Missouri', 'Kentucky', 'West Virginia', 'Virginia', 'Maryland', 'Delaware', 'New Jersey', 'North Carolina', 'South Carolina', 'Tennessee', 'Arkansas', 'Oklahoma', 'Texas', 'Louisiana', 'Mississippi', 'Alabama', 'Georgia', 'Florida', 'Arizona', 'New Mexico', 'Hawaii']

def assign_north_south_state_region(state):
    """
    Assign states to the north or south region.
    
    state: State name.
    
    return: Region.
    """
    if state in northern_states:
        return 'North'
    elif state in southern_states:
        return 'South'
    else:
        return 'Int'
    
west_states = ['Alaska', 'California', 'Hawaii', 'Oregon', 'Washington', 'Idaho', 'Nevada', 'Utah', 'Arizona', 'Montana', 'Wyoming', 'Colorado', 'New Mexico']
midwest_states = ['North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Minnesota', 'Iowa', 'Missouri', 'Wisconsin', 'Illinois', 'Michigan', 'Indiana', 'Ohio']
mid_east_states = ['Texas', 'Oklahoma', 'Arkansas', 'Louisiana', 'Kentucky', 'Tennessee', 'Mississippi', 'Alabama']
east_states = ['Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'Rhode Island', 'Connecticut', 'New York', 'Pennsylvania', 'New Jersey', 'Delaware', 'Maryland', 'West Virginia', 'Virginia', 'North Carolina', 'South Carolina', 'Georgia', 'Florida']

def assign_east_west_state_region(state):
    """
    Assign states to the east or west region.
    
    state: State name.
    
    return: Region.
    """
    if state in west_states:
        return 'West'
    elif state in midwest_states:
        return 'MW'
    elif state in mid_east_states:
        return 'ME'
    elif state in east_states:
        return 'East'
    else:
        return 'Int'
