# from .visualizations.scatter_usa import plot_usa_map_with_data
# from .visualizations.scatter_world import plot_world_map_with_data
from .visualizations.bar_graph import get_bar_graph

def display_all_graphs(allYearData, year):    
    # countriesDf = allYearData[0]
    # statesDf = allYearData[1]
    # genderDf = allYearData[2]
    # ageDf = allYearData[3]
    industryDf = allYearData[4]
    # sourceDf = allYearData[5]
    # nameDf = allYearData[6]

    # bar graph for gender
    # get_bar_graph(genderDf, year)

    # bar graph for age
    # get_bar_graph(ageDf, year)


    # bar graph for industry
    get_bar_graph(industryDf, year)

    # bar graph for source
    # get_bar_graph(sourceDf.head(30), year)

    # make bar graphs of the first letter of their name and the first letter of their last name
    # first_name_table = get_first_name_table(nameDf)
    # get_bar_graph(first_name_table, year)
    # last_name_table = get_last_name_table(nameDf)
    # get_bar_graph(last_name_table, year)

    # make display hot locations in the world and usa
    # plot_world_map_with_data(countriesDf)
    # plot_usa_map_with_data(statesDf)

    # showing what areas are the most important
    # ns_table = get_north_south_state_table(statesDf)
    # get_bar_graph(ns_table, year)
    # ew_table = get_east_west_state_table(statesDf)
    # get_bar_graph(ew_table, year)


def parse_data_count_based_on_col(df, col):
    '''
    this will make a new dataframe that counts the occurrence for the column given
    df: dataframe of all data
    col: column to count
    return: dataframe
    '''
    df_source_counts = df.groupby(col).size().reset_index(name='#_of_people').sort_values(by='#_of_people', ascending=False)
    return df_source_counts

def build_table(df, col, new_col, assigment_method):
    df[new_col] = df[col].apply(assigment_method)
    table = df.pivot_table(index=new_col, values='#_of_people', aggfunc='sum')
    table.reset_index(inplace=True)
    return table

def assign_based_on_first_letter_first_name(name):
    return name[0]

def assign_based_on_first_letter_last_name(name):
    n = name.split()
    if len(n)>1:
        return n[1][0]
    else:
        return n[0][0]

def get_first_name_table(df):
    return build_table(df, 'name', 'first_letter_first_name', assign_based_on_first_letter_first_name)

def get_last_name_table(df):
    return build_table(df, 'name', 'first_letter_last_name', assign_based_on_first_letter_last_name)

northern_states = ['Washington', 'Oregon', 'Idaho', 'Montana', 'North Dakota', 'South Dakota', 'Minnesota', 'Wisconsin', 'Michigan', 'Wyoming', 'Nebraska', 'Iowa', 'Illinois', 'Indiana', 'Ohio', 'Pennsylvania', 'New York', 'Vermont', 'New Hampshire', 'Maine', 'Massachusetts', 'Connecticut', 'Rhode Island', 'Alaska']
southern_states = ['California', 'Nevada', 'Utah', 'Colorado', 'Kansas', 'Missouri', 'Kentucky', 'West Virginia', 'Virginia', 'Maryland', 'Delaware', 'New Jersey', 'North Carolina', 'South Carolina', 'Tennessee', 'Arkansas', 'Oklahoma', 'Texas', 'Louisiana', 'Mississippi', 'Alabama', 'Georgia', 'Florida', 'Arizona', 'New Mexico', 'Hawaii']

def get_north_south_state_table(statesDf):
    return build_table(statesDf, 'state', 'vertical_regions', assign_north_south_state_region)

def assign_north_south_state_region(state):
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

def get_east_west_state_table(statesDf):
    return build_table(statesDf, 'state', 'horizontal_regions', assign_east_west_state_region)

def assign_east_west_state_region(state):
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


