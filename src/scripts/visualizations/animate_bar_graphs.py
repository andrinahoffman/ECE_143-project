import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from .bar_graph import animated_bar_graph

def animate_bar_graphs(dataframes, years, column_name, filename='animation.gif'):
    """
    Generate an animated bar graph for a given column across multiple years.

    dataframes: List of DataFrames containing data for each year.
    years: List of years corresponding to the dataframes.
    column_name: Name of the column to visualize.
    filename: Name of the output animation file. Default is 'animation.mp4'.

    return: None
    """
    # Create a new figure and axis
    fig, ax = plt.subplots()
    
    def update(num):
        """
        Update function for each frame of the animation.

        num: Frame number.
        
        return: Bar plot object for the updated frame.
        """
        ax.clear()
        df = dataframes[num]
        year = years[num]
        bars = animated_bar_graph(df, year, fig, ax, column_name)
        return bars

    # Create the animation
    anim = FuncAnimation(fig, update, frames=len(dataframes), repeat=False, blit=True)
    
    # Save the animation as an mp4 file
    frame_speed = 4
    if column_name=="industry" or column_name=="source":
        frame_speed = 2
    anim.save(filename, writer='imagemagick', fps=frame_speed)
    # anim.save(filename, fps=10, extra_args=['-vcodec', 'libx264'])
    
    # Display the animation
    plt.show()
