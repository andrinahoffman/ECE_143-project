import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('billionaires_2022.csv')

country_industry_counts = df.groupby(['country', 'industry']).size().reset_index(name='counts')


country_counts = df['country'].value_counts()

countries_more_than_one_billionaire = country_counts[country_counts > 1].index

filtered_country_industry_counts = country_industry_counts[country_industry_counts['country'].isin(countries_more_than_one_billionaire)]

top_industry_in_countries = filtered_country_industry_counts.sort_values('counts', ascending=False).groupby('country').head(1)

selected_countries_for_visualization = top_industry_in_countries.sort_values('counts', ascending=False).head(5)['country'].tolist()

fig, axes = plt.subplots(len(selected_countries_for_visualization), 1, figsize=(10, 8 * len(selected_countries_for_visualization)))

if len(selected_countries_for_visualization) == 1:
    axes = [axes]

for ax, country in zip(axes, selected_countries_for_visualization):
    industry_distribution = df[df['country'] == country]['industry'].value_counts()
    ax.pie(industry_distribution, labels=industry_distribution.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(f'Industry Distribution among Billionaires in {country} (2022)')
    ax.axis('equal')

plt.tight_layout()
plt.show()
