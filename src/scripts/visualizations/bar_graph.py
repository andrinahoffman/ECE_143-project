import matplotlib.pyplot as plt

def get_bar_graph(df, year):
    df.plot(x=df.columns[0], y='#_of_people', kind='bar')
    plt.title(f'{year} Location')
    plt.xlabel(df.columns[0])
    plt.ylabel('#_of_people')
    plt.show()
