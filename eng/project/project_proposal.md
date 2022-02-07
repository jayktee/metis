#  Analyzing Covid-19 vaccine hesitancy: A Twitter analysis

### Question/Need:

* What is the question behind your analysis? What is the purpose of the model/system you plan to build?

From December 11, 2020 -- the day that the Food and Drug Agency (FDA) issued the first Emergency Use Authorization for the Pfizer Covid-19 vaccine -- there was widespread excitement that the pandemic may soon be coming to an end. Yet, there was also growing opposition and concerns about the vaccine's safety and possible side effects.

In September 2020, a Pew survey showed that nearly half of American adults surveyed did not intend to take the vaccine, although by February 2021, only 30% of surveyed people said they would not get the vaccine while 19% had already received at least one dose. However, surveys can only go so far to identify public sentiment regarding the vaccine.

Using public Twitter data and natural language processing techniques, we can go further to identify the change in public sentiment towards the Covid vaccine, and study the reasons behind these changes. 


### Data Description:

* What dataset(s) do you plan to use, and how will you obtain the data?

Using the Twitter API and Tweepy, I will ingest and clean over 80,000 tweets related to the key words "vaccine" and "covid-19". To limit the scope of the search, I will search for tweets related to the Covid vaccines within a specific time period, i.e. 1000 tweets per day for 7 days for each month from January to December 2021.

* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

The unit of analysis is a single tweet, which includes the text of the tweet and any linked URLs, the author/user, links to any retweets or replies, interaction counts (e.g. number of retweets or replies), the timestamp, and the geolocation (if enabled) of the user. 

### Tools:

* How do you intend to meet the tools requirement of the project?

I will use topic modeling to identify the most popular or important topics and sentiment analysis libraries such as VADER to code the sentiment of each tweet.

Once the sentiment has been coded, I will use visualization libraries such as Seaborn to chart the percentage composition of positive to neutral to negative tweets regarding the Covid-19 vaccine over the year. 


### MVP Goal:

* What would a minimum viable product (MVP) look like for this project?

For my MVP, I will begin with identifying sentiment analysis using VADER and do a simple visualization of the percentage of sentiment over the year. 