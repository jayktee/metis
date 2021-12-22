# Using Spotify track metadata to predict song popularity
By: Joyce Tagal
## Abstract

* What is the question behind your analysis? What is the purpose of the model/system you plan to build?

Spotify wants to develop a model to identify the genre of a song, to auto-generate playlists based on certain genres, e.g. "Emo Effect", "Classical Calling", or "Punk Paradise". With a large amount of data available on their track metadata, they have decided to try several different classification models and decide what is the best model to launch on their platform.

* Who benefits from exploring this question or building this model/system?

By using a predictor, we can more easily develop playlists that are suited for each listener, based on their listening history. Given a sample of songs that the user has recently listened to, Spotify can "target" playlists to the user with similar songs based on their listening history.

## Design

Spotify has made billions of rows of metadata available on all the songs in its catalog, available on its Web API. The features included in metadata range from musicality features such as `tempo`, `mode` and `time-signature` to more descriptive measures such as `liveness` and `valence`, that measures the happiness level of the track. We will use the features available to see if we can predict genre based on the track's metadata. One important thing to note is that some of the features are based on the song's musical features, while some may not be, such as `popularity`.

Our target is the `genre`, i.e. the type of genre for the track. There are 22 genres in the dataset, and the targets are generally balanced. We start with a baseline accuracy of 4.5% i.e. the accuracy if a naive model predicted "Opera" for every single instance. Any model we choose will have to be better than the baseline accuracy. 

I select mean precision and precision by target as my chosen metrics to compare across models.

## Data

My data includes 200,100 rows taken from 3 various data sources: 

- 1,277 rows were scraped from the Spotify Top 200 weekly charts for the year between 09-01-2021 and 09-01-2020
- 4,099 rows were scraped from Spotify's API using random search terms
- 10,000 rows were randomly sampled from a dataset of 228,159 rows downloaded from Kaggle

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
- popularity - the current popularity of a song, a metric developed by Spotify based on number of recent listens

## Algorithms

I went through 7 different models, and chose a Random Forest model optimized by GridSearchCV for the final model. The model had a precision score of 40% on holdout data and a decent distribution of precision across targets, with the lowest precision score of 18.6% for Dance and the highest precision score for Opera at 85.3%. 

The other models I selected were as follows: 

- Naive KNN
- KNN optimized with GridSearchCV
- DecisionTree Baseline
- DecisionTree optimized with GridSearchCV
- RandomForest Baseline
- RandomForest optimized with GridsearchCV (final selected model)
- ExtraTrees Baseline


## Tools
- pandas to summarize and clean the data
- seaborn for visualizing the data and metrics
- sklearn for training the model (KNN, DecisionTree, RandomForest, ExtraTrees)
- sklearn.metrics for evaluating the models (precision, recall, accuracy, F1, confusion_matrix)

## Communication

Ultimately I was able to achieve a mean precision score of 40% on holdout data. I developed slides to communicate my model development process and predictive outcomes, and have developed notebooks to explain the process which I have posted to my GitHub account.
