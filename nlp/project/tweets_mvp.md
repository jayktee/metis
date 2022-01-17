#  Analyzing Covid-19 vaccine hesitancy: A Twitter analysis

I am creating a sentiment analysis of Covid-19 vaccines over the year 2021, using Twitter data. In addition, I am doing dynamic topic modeling to consider changes in the most relevant topics.

### Work completed

I have used Tweepy to scrape the Twitter API using the keyword "covid+vaccine" with an average of 5000 tweets extracted per month, resulting in over 63,000 tweets.
To clean the data, I removed all digits and punctuation and replaced emojis with emoji description. I chose to not lemmatize, stem or remove stopwords to avoid affecting later sentiment analysis.

I then ran VADER on the corpus of tweets, resulting in a positive and negative sentiment score for each row of the dataset. 

### Recent findings

After grouping the sentiments by month and plotting them using Seaborn, I find that the negative sentiment regarding Covid vaccines grew significantly in June-July 2021, which is around the time that the FDA had given emergency authorization use for the general public. However, what is somewhat surprising is that positive sentiment has stayed somewhat constant over time.

!(https://github.com/jayktee/metis/blob/master/nlp/project/images/sentiment_time.png)

### Moving forward

I will move on next to Dynamic Topic Modeling (DTM) using gensim's Ldaseqmodel function. If I have time, I would like to build an app to showcase my results using Streamlit/Herokuapp.