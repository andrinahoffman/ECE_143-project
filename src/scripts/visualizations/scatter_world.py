import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

country_coordinates = {
    'United States': (37.0902, -95.7129),
    'China': (35.8617, 104.1954),
    'India': (20.5937, 78.9629),
    'Germany': (51.1657, 10.4515),
    'Russia': (61.5240, 105.3188),
    'Hong Kong': (22.3193, 114.1694),
    'Canada': (56.1304, -106.3468),
    'Brazil': (-14.2350, -51.9253),
    'Italy': (41.8719, 12.5674),
    'United Kingdom': (55.3781, -3.4360),
    'Taiwan': (23.6978, 120.9605),
    'Australia': (-25.2744, 133.7751),
    'Japan': (36.2048, 138.2529),
    'France': (46.6034, 1.8883),
    'South Korea': (35.9078, 127.7669),
    'Sweden': (60.1282, 18.6435),
    'Switzerland': (46.8182, 8.2275),
    'Indonesia': (-0.7893, 113.9213),
    'Singapore': (1.3521, 103.8198),
    'Israel': (31.0461, 34.8516),
    'Thailand': (15.8700, 100.9925),
    'Spain': (40.4637, -3.7492),
    'Turkey': (38.9637, 35.2433),
    'Malaysia': (4.2105, 101.9758),
    'Philippines': (12.8797, 121.7740),
    'Mexico': (23.6345, -102.5528),
    'Netherlands': (52.1326, 5.2913),
    'Austria': (47.5162, 14.5501),
    'Norway': (60.4720, 8.4689),
    'Czech Republic': (49.8175, 15.4729),
    'Ireland': (53.4129, -8.2439),
    'Cyprus': (35.1264, 33.4299),
    'Denmark': (56.2639, 9.5018),
    'Poland': (51.9194, 19.1451),
    'Finland': (61.9241, 25.7482),
    'Chile': (-35.6751, -71.5429),
    'Vietnam': (14.0583, 108.2772),
    'Ukraine': (48.3794, 31.1656),
    'Egypt': (26.8206, 30.8025),
    'Romania': (45.9432, 24.9668),
    'South Africa': (-30.5595, 22.9375),
    'Argentina': (-38.4161, -63.6167),
    'Lebanon': (33.8547, 35.8623),
    'Kazakhstan': (48.0196, 66.9237),
    'Greece': (39.0742, 21.8243),
    'Peru': (-9.1900, -75.0152),
    'Belgium': (50.5039, 4.4699),
    'Monaco': (43.7384, 7.4246),
    'Nigeria': (9.0820, 8.6753),
    'Colombia': (4.5709, -74.2973),
    'United Arab Emirates': (23.4241, 53.8478),
    'New Zealand': (-40.9006, 174.8860),
    'Hungary': (47.1625, 19.5033),
    'Uruguay': (-32.5228, -55.7658),
    'Slovakia': (48.6690, 19.6990),
    'Bulgaria': (42.7339, 25.4858),
    'Iceland': (64.9631, -19.0208),
    'Qatar': (25.3548, 51.1839),
    'Oman': (21.4735, 55.9754),
    'Morocco': (31.7917, -7.0926),
    'Estonia': (58.5953, 25.0136),
    'Georgia': (42.3154, 43.3569),
    'Tanzania': (-6.3690, 34.8888),
    'Venezuela': (6.4238, -66.5897),
    'Algeria': (28.0339, 1.6596),
    'Macau': (22.1987, 113.5439),
    'St. Kitts and Nevis': (17.3578, -62.782998),
    'Portugal': (39.3999, -8.2245),
    'Panama': (8.5370, -80.7821),
    'Nepal': (28.3949, 84.1240),
    'Liechtenstein': (47.1660, 9.5554),
    'Guernsey': (49.4657, -2.5853),
    'Eswatini (Swaziland)': (-26.5225, 31.4659),
    'Belize': (17.1899, -88.4976),
    'Barbados': (13.1939, -59.5432),
    'Bangladesh': (23.6850, 90.3563),
    'Armenia': (40.0691, 45.0382),
    'Zimbabwe': (-19.0154, 29.1549)
}

def plot_world_map_with_data(df):
    # Create a new figure
    plt.figure(figsize=(15, 10))

    # Create a new GeoAxes with a Plate Carree projection centered on the world
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_global()

    # Add coastlines, countries, and borders
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle='--')

    # Plot the scatter data for each country
    for _, row in df.iterrows():
        country = row['country']
        num_people = row['#_of_people']
        
        # Get the coordinates of the country (assuming it's in the provided dictionary)
        if country in country_coordinates:
            coord = country_coordinates[country]
        else:
            coord = (0, 0)  # Default coordinates if not found in the dictionary

        # Determine color based on the number of people
        red_component = min(1, num_people / 100)  # Ensure the red component is between 0 and 1
        color = (red_component, 0, 1)  # RGB color with red component based on the number of people
        
        # Draw a rectangle background behind the text
        x = 4.5
        y = 7.5 if num_people >= 100 else 5

        rect = plt.Rectangle((coord[1] - y/2, coord[0] - x/2), y, x, facecolor=color, edgecolor='none', zorder=1)
        ax.add_patch(rect)

        # Annotate the coordinate with the number of people
        ax.text(coord[1], coord[0], str(num_people), fontsize=9, color='white',
                ha='center', va='center', zorder=2)

    # Show the plot
    plt.show()
