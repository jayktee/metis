# Using MTA data to estimate store traffic in lower Manhattan
By: Joyce Tagal
## Abstract

Besides wreaking havoc on public health systems globally, the COVID-19 pandemic has fundamentally changed city density patterns. To prevent overhead losses from unnecessary rents, retail chains across America have been considering closing a number of retail locations in previously-dense downtown locations.

In this project, I use the MTA turnstile entry and exit data, OpenRouteService API and geopandas to estimate foot traffic at a number of Duane Reade locations in lower Manhattan. This calculation could hopefully be used by company executives in their decisions to potentially close a certain number of stores.

## Design

I use MTA turnstile data to estimate foot traffic for a set of given Duane Reade locations (scraped from Walgreens website) in lower Manhattan. To simplify my project, I manually selected a number of Duane Reade/Walgreens locations and MTA stations below 34th Street in Lower Manhattan using Google Maps. I then filtered the MTA turnstile data for those specific stations based on location names.

Once both datasets are cleaned, I turn both dataframes into geospatial dataframes by geocoding addresses for both the MTA stations and pharmacy locations. Then, using the [OpenRouteService](https://openrouteservice.org/) isochrones API, I call isochrones for a 5-minute walking distance from each MTA station. Then, I use Geopandas spatial join to identify, for each pharmacy location in my Duane Reade dataset, which MTA stations are within a 5-min walking distance from the pharmacy.

After the spatial join is completed, I make several assumptions about foot traffic to sum up estimated foot traffic around that Duane Reade location. I then use Matplotlib to visualize the foot traffic time series trends for each of the 22 DR locations in my dataset.

## Data

- MTA turnstile data from 12-26-2020 to present day
- MTA station coordinates from Open Data NYC
- Duane Reade locations scraped from Walgreens website

## Algorithms

I use several assumptions to estimate foot traffic around the given pharmacy location. For each location:
- Some MTA stations have several exits which are significantly different in geographic coordinates. For ease of calculation, I took the first coordinate point with that station name in the MTA station coordinates  
- I do not take into account the neighborhood baseline population. I assume that this is constant even throughout the pandemic (which may not be a good assumption)
- I calculate 'net traffic' for a given pharmacy location as the (sum entries for all stations within a 5 minute walking distance) minus (the sum of exits from all stations within a 5 minute walking distance)
- I do not account for other pedestrian traffic, including bus lines

## Tools
- Matplotlib for EDA
- Geopandas for GeoDataFrames
- Google Places API for geocoding store addresses
- [OpenRouteService](https://openrouteservice.org/) API to get isochrones
- Folium to map coordinates and isochrones

## Communication

Visualizing my project includes a Folium map available on Github. I also developed slides and this write-up to communicate my project.