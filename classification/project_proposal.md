#  Predicting Spotify song genres using Classification model

### Question/Need:

* What is the question behind your analysis? What is the purpose of the model/system you plan to build?

Spotify wants to build a predictor to identify the genre of a song, so that they can more easily develop playlists based on certain genres, e.g. "Emo Effect", "Classical Calling", or "Punk Paradise". With a large amount of data available on their track metadata, they have decided to try several different classification models and decide what is the best model to launch on their platform.

Spotify would like to first build a predictor for the United States market and, if the predictor has a high degree of accuracy,
to build the same for other countries.

* Who benefits from exploring this question or building this model/system?

By using a predictor, we can more easily develop playlists that are suited for each listener, based on their listening history. Given a sample of songs that the user has recently listened to, Spotify can "target" playlists to the user with similar songs based on their listening history.

### Data Description:

* What dataset(s) do you plan to use, and how will you obtain the data?

I will be using a dataset downloaded from Kaggle with 228,000+ rows, originally downloaded from the Spotify Web API. The features of the dataset are outlined below.

* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

A row of analysis in this project is a song/track with several features that can be used to identify the genre of the track (the
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
- genre - the genre of the track. This feature has now been deprecated from a track metadata and associated with artists.

* If modeling, what will you predict as your target?

The targets are the genre of a track. 


### Tools:

* How do you intend to meet the tools requirement of the project?

I will use the following tools in the project:
- sklearn and other modelling tools to develop the models
- Matplotlib and Seaborn to visualize the data

If I have enough time, I may consider using fun visualization tools or presentation tools to develop a recommender site. 


### MVP Goal:

* What would a minimum viable product (MVP) look like for this project?

For my MVP, I will begin with a subset of data including 3-4 genres and once I improve the metrics for my initial models, I will include more genres. 
