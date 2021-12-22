# metis

This is a public repo for my work on Metis Data Science and Engineering bootcamp.

A list of projects I've completed as part of the bootcamp:
* Developed a song popularity predictor using a linear regression model and Spotify song metadata scraped from Spotify Charts using BeautifulSoup and the Spotify Web API. My model achieved an R^2 of 0.698 and a MAE/RSME of 7.2/9.4 over 100 on test data. [Full project code here](https://github.com/jayktee/metis/tree/master/reg).

* Developed a song genre classifier using several multiclass classification models. In the best performing model (Random Forest model optimized by GridSearchCV), achieved a mean precision score of 40% across 22 classes on test data (lowest precision score of 18.6% for Dance and the highest precision score for Opera at 85.3%). [Full project code here](https://github.com/jayktee/metis/tree/master/classification).

* Calculated changes in foot traffic from a set of pharmacies in lower Manhattan using New York MTA turnstile entry and exit data. Tools used include OpenRouteService isochrones API and geopandas and Folium/Leaflet to visualize the changes in foot traffic within given isochrones. [Full project code here](https://github.com/jayktee/metis/tree/master/eda). 