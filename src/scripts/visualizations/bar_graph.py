import matplotlib.pyplot as plt
import numpy as np

def get_bar_graph(df, year):
    """
    Generate a bar graph based on DataFrame data for a given year.
    
    df: DataFrame containing data to plot.
    year: Year for which data is being plotted.
    
    return: Plot object.
    """
    plot = df.plot(x=df.columns[0], y='#_of_people', kind='bar')
    plt.title(f'{year}')  # Set title as the year
    plt.xlabel(df.columns[0])  # Set x-axis label as the first column name
    plt.ylabel('#_of_people')  # Set y-axis label as '#_of_people'
    return plot

def animated_bar_graph(df, year, fig, ax, column_name):
    """
    Generate an animated horizontal bar graph based on DataFrame data for a given year and column.
    
    df: DataFrame containing data to plot.
    year: Year for which data is being plotted.
    ax: Axis object to plot on.
    column_name: Name of the column for which data is being plotted.
    
    return: Bar plot object.
    """
    # Check if the column names are as expected
    # print(df.columns)

    if column_name=="country":
        fig_width = len(df) * 0.5  # Adjust the multiplier according to your preference
        fig.set_size_inches(fig_width, 6)  # Set the figure size
    elif column_name=="industry" or column_name=="source":
        fig_width = len(df) * 2 # Adjust the multiplier according to your preference
        fig.set_size_inches(fig_width, 6)  # Set the figure size
    # Generate horizontal bar graph
    bars = ax.barh(df[column_name], df['#_of_people'])
    
    # Set title, labels, and ticks for the plot
    ax.set_title(f'{year} {column_name}')  # Set title with year and column name
    ax.set_xlabel('# of People')  # Set x-axis label as '# of People'

    ax.set_ylabel(column_name)  # Set y-axis label as the column name

    # Generalize x-axis ticks to avoid overlap
    max_value = df['#_of_people'].max()
    ax.set_xticks(np.arange(0, max_value + 1, max_value // 10))  # Adjust the divisor to control the number of ticks
    
    return bars
