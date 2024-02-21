import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

state_coordinates = {
    'Alabama': (32.806671, -86.791130),
    'Alaska': (61.370716, -152.404419),
    'Arizona': (34.168219, -111.930907),
    'Arkansas': (34.746613, -92.288986),
    'California': (36.778261, -119.417932),
    'Colorado': (38.997222, -105.547829),
    'Connecticut': (41.518715, -72.757507),
    'Delaware': (39.145301, -75.418541),
    'Florida': (27.994402, -81.760254),
    'Georgia': (32.678125, -83.222977),
    'Hawaii': (20.716179, -158.214676),
    'Idaho': (44.068203, -114.742043),
    'Illinois': (40.041165, -89.196533),
    'Indiana': (39.894219, -86.281601),
    'Iowa': (42.075347, -93.496025),
    'Kansas': (38.498779, -98.320078),
    'Kentucky': (37.822294, -85.768240),
    'Louisiana': (31.173377, -92.529909),
    'Maine': (45.218513, -69.014870),
    'Maryland': (39.045753, -76.641273),
    'Massachusetts': (42.407211, -71.382439),
    'Michigan': (44.182205, -84.506836),
    'Minnesota': (46.392410, -94.636230),
    'Mississippi': (32.741646, -89.678696),
    'Missouri': (38.573936, -92.603760),
    'Montana': (46.965260, -109.533691),
    'Nebraska': (41.125370, -98.268082),
    'Nevada': (38.802610, -116.419389),
    'New Hampshire': (43.193852, -71.572395),
    'New Jersey': (40.058323, -74.405663),
    'New Mexico': (34.407144, -106.112358),
    'New York': (43.205626, -74.8),
    'North Carolina': (35.782169, -80.793457),
    'North Dakota': (47.650589, -100.437012),
    'Ohio': (40.190362, -82.669252),
    'Oklahoma': (35.309765, -98.716049),
    'Oregon': (43.804133, -120.554201),
    'Pennsylvania': (41.203323, -77.194527),
    'Rhode Island': (41.580095, -71.477429),
    'South Carolina': (33.836082, -81.163727),
    'South Dakota': (43.969515, -99.901810),
    'Tennessee': (35.517491, -86.580447),
    'Texas': (31.968599, -99.901810),
    'Utah': (39.320980, -111.093735),
    'Vermont': (44.045876, -72.710686),
    'Virginia': (37.431573, -78.656894),
    'Washington': (47.751076, -120.740135),
    'West Virginia': (38.969645, -80.288437),
    'Wisconsin': (44.786297, -89.826706),
    'Wyoming': (43.075968, -107.290283)
}

def plot_usa_map_with_data(df):
    # Create a new figure
    plt.figure(figsize=(10, 5))

    # Create a new GeoAxes with a Plate Carree projection centered on the USA
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-125, -66.5, 20, 50], crs=ccrs.PlateCarree())  # Extent for the USA

    # Add coastlines, states, and borders
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.STATES)
    ax.add_feature(cfeature.BORDERS, linestyle='--')

    # Plot the scatter data for each state
    for _, row in df.iterrows():
        state = row['state']
        num_people = row['#_of_people']
        
        # Get the coordinates of the state (assuming it's in the provided arrays)
        if state in state_coordinates:
            coord = state_coordinates[state]
        else:
            coord = (0, 0)  # Default coordinates if not found in the arrays

        # Determine color based on the number of people
        red_component = min(1, num_people / 100)  # Ensure the red component is between 0 and 1
        color = (red_component, 0, 1)  # RGB color with red component based on the number of people
        
        # Draw a rectangle background behind the text
        rect = plt.Rectangle((coord[1] - .7, coord[0] - .7), 1.4, 1.4, facecolor=color, edgecolor='none', zorder=1)
        ax.add_patch(rect)

        # Annotate the coordinate with the number of people
        ax.text(coord[1], coord[0], str(num_people), fontsize=9, color='white',
                ha='center', va='center', zorder=2)

    # Show the plot
    plt.show()
