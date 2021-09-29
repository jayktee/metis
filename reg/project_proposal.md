#  Predicting Spotify song popularity using Linear Regression model

### Question/Need:

* What is the question behind your analysis? What is the purpose of the model/system you plan to build?
Sony Music wants to build a predictor to identify the possible popularity of a song, so that they can identify hit songs
ahead of time and market them accordingly. This task is becoming more difficult given that music tastes have become more
global, thanks to the internet and streaming platforms like Spotify and Pandora. Now, label executives have to identify 
possible hits from a wide variety of genres and artists. Enter machine learning! Perhaps Sony can build a predictor that
will help identify the popularity of a recorded track based on several traits. With a large amount of data available on
platforms such as Spotify, data scientists can build predictors relatively easily from open source data.

Sony would like to first build a predictor for the United States market and, if the predictor has a high degree of accuracy,
to build the same for other countries.

* Who benefits from exploring this question or building this model/system?
Currently, record labels have executives that listen to songs to identify potential hits. By using a predictor, we could first
predict the popularity score of a certain track before human executives listen to it. This will reduce the number of tracks for 
execs to listen to, making it easier overall to find the next hit song.

### Data Description:

* What dataset(s) do you plan to use, and how will you obtain the data?
I will be using two datasets, obtained as following:
- Spotify US top 200 songs by week for the year 2020, scraped from [spotifycharts.com](https://spotifycharts.com/regional/us/daily/2020-09-01) using BeautifulSoup and Selenium
- Spotify track features for all the songs in the first dataset, obtained from the [Spotify Developer Tracks API](https://developer.spotify.com/documentation/web-api/reference/#category-tracks)

The second dataset will provide me with the features for all the songs in the first dataset, which will allow me to train my predictor
model. 

* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

A row of analysis in this project is a song/track with several features to predict popularity (the
target).

Per the Spotify Tracks API documentation, API contains the following features for each track: 
- danceability (0-1) - how suitable a track is for dancing
- energy (0-1) - measure of intensity and activity
- key (0-11) - using standard Pitch Class notation where 0=C
- loudness (-60-0)
- mode (0 or 1) - major (1) or minor (0) key
- speechiness (0-1) - the presence of spoken words on a track
- accousticness (0-1) - whether the track is accoustic
- instrumentalness - whether a track has no vocals
- liveness (0-1) - detects the presence of an audience in the recording
- valence (0-1) - the musical "positiveness" of a track, i.e. happiness 
- tempo (float) - estimated tempo in beats per minute
- time-signature - estimated time signature of a track

I will begin with all these features in my first model, and refine by removing collinear and 
non-significant features as I go along.

* If modeling, what will you predict as your target?
The target is the popularity of a track, calculated by a Spotify algorithm based on total number
of plays the track has had and how recent those plays are. 

I will use linear regression, training my model on 60% of the dataset and using the remaining 20-20
for further refinement and evaluation. 

Note: The popularity of a track is a numerical value (integer) between 0-100 that is assigned to a track. This value is not updated in real time so the value may lag actual popularity by a few days. 
Given that we are using a list of top songs from 2020 (last year), this may not be an issue given that the popularity value for those songs should have stabilized over time.


### Tools:

* How do you intend to meet the tools requirement of the project?
I will use the following tools in the project:
- BeautifulSoup and Selenium for scraping spotifycharts.com
- pandas to summarize and clean the data
- seaborn for visualizing the data
- statsmodel for doing some baseline stats score with R^2
- sklearn for training the model and model evaluation


### MVP Goal:

* What would a minimum viable product (MVP) look like for this project?
I will work on an MVP using 10 weeks of data from SpotifyCharts to train the model, with the predictors described above. With more time, I will be able to refine my model by removing low correlation variables and reducing collinearity. 
