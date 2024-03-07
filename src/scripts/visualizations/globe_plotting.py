"""
Utilities for plotting scalar data on a globe by country.
"""
import cartopy
from cartopy.io import shapereader
import cartopy.crs as ccrs
import geopandas
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


# ripped straight from https://stackoverflow.com/questions/61460814/color-cartopy-map-countries-according-to-given-values
# get global country data from natural earth data (http://www.naturalearthdata.com/)

# get country borders
resolution = "10m"
category = "cultural"
name = "admin_0_countries"
shpfilename = shapereader.natural_earth(resolution, category, name)

# read the shapefile using geopandas
df = geopandas.read_file(shpfilename)


def plot_global_data(countries, data, figsize=(8, 6), title="", cbar_label="", cmap="viridis", gridlines=False, country_name_map={}):
    """
    Plots scalar data on a global map by country. Color indicates scalar value.

    Args:
        countries (iterable): List of country names. If they don"t match natural earth data names,
            it can be corrected using the country_name_map argument.
        data (iterable): List of scalar values for each country. Same order as countries.
        figsize (tuple): Figure size.
        title (str): Title of the whole plot.
        cbar_label (str): Label for the colorbar.
        cmap (str): Name of the colormap to use.
        gridlines (bool): True to plot gridlines, False otherwise.
        country_name_map (dict): Dictionary mapping country names to what they are called in the
            natural earth data, in order to correct any mismatches.
    
    Returns:
        fig, ax
    """
    assert len(countries) == len(data)
    fig = plt.figure(figsize=figsize)
    central_lon = 0
    # exclude Antarctica lol
    extent = [-180, 180, -70, 90]
    ax = plt.axes(projection=cartopy.crs.PlateCarree(central_lon))
    ax.set_extent(extent)
    if gridlines:
        ax.gridlines()

    # Add natural earth features and borders
    ax.add_feature(cartopy.feature.BORDERS, linestyle=":", alpha=1)
    ax.add_feature(cartopy.feature.OCEAN, facecolor=("lightblue"))
    ax.add_feature(cartopy.feature.LAND)
    ax.coastlines(resolution="110m")

    # Normalise data so colors show up properly in the colormap
    data_norm = (data - np.nanmin(data)) / (np.nanmax(data) - np.nanmin(data))

    cmap = matplotlib.colormaps.get_cmap(cmap)

    for country, d_norm in zip(countries, data_norm):
        # read the borders of the country in this loop
        if country in country_name_map:
            country = country_name_map[country]
        poly = df.loc[df["ADMIN"] == country]["geometry"].values[0]
        # get the color for this country
        rgba = cmap(d_norm)
        # plot the country on a map
        ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor=rgba, edgecolor="none", zorder=1)

    # hacky way to generate scale of colorbar, invisible scatter plot
    dummy_scat = ax.scatter(data, data, c=data, cmap=cmap, zorder=0, s=0)
    fig.colorbar(mappable=dummy_scat, label=cbar_label, orientation="horizontal", shrink=0.8)
    fig.suptitle(title)
    fig.tight_layout()
    return fig, ax
