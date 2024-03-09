import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('billionaires_2022.csv')

population_data = {
    'United States': 331002651,
    'China': 1439323776,
    'India': 1380004385,
    'Germany': 83783942,
    'Hong Kong': 7496981,
    'Russia': 145934462,
    'Italy': 60461826,
    'Canada': 37742154,
    'Brazil': 212559417,
    'Singapore': 5850342
}

billionaire_counts_per_country = df['country'].value_counts().to_dict()

billionaire_to_population_ratio = {country: billionaire_counts_per_country[country] / population_data[country] for
                                   country in population_data.keys() if country in billionaire_counts_per_country}

ratio_df = pd.DataFrame(list(billionaire_to_population_ratio.items()), columns=['Country', 'Billionaire to Population '
                                                                                           'Ratio'])

sorted_ratio_df = ratio_df.sort_values(by='Billionaire to Population Ratio', ascending=False)

top_2 = sorted_ratio_df.head(2)
bottom_2 = sorted_ratio_df.tail(2)

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(top_2['Country'], top_2['Billionaire to Population Ratio'], color='green', label='Top 2 Ratios')
plt.barh(bottom_2['Country'], bottom_2['Billionaire to Population Ratio'], color='red', label='Bottom 2 Ratios')
plt.xlabel('Billionaire to Population Ratio')
plt.title('Countries with Highest and Lowest Billionaire to Population Ratios')
plt.legend()
plt.show()

top_2, bottom_2
