#  Analyzing Covid-19 vaccine hesitancy: A Twitter analysis

In this project, the goal was to analyze changes in Covid-19 vaccine sentiment and concerns over time. To achieve this, I conducted dynamic topic modeling and sentiment analysis on a corpus of 100,000 tweets scraped from Twitter over the year 2021. 

### Work completed and tools

* Used Tweepy to scrape the Twitter API using the keyword "covid+vaccine" with an average of 5000 tweets extracted per month, resulting in over 63,000 tweets.
* Data cleaning: Removed all digits and punctuation and replaced emojis with emoji description using Demoji. 
* For the sentiment analysis, I chose to not lemmatize, stem or remove stopwords to avoid affecting later sentiment analysis. For dynamic topic modeling, I used NLTK's [WordNetLemmatizer](https://www.nltk.org/api/nltk.stem.wordnet.html#nltk.stem.wordnet.WordNetLemmatizer) and [LancasterStemmer](https://www.nltk.org/_modules/nltk/stem/lancaster.html) to stem and lemmatize the corpus of tweets.
* I then ran [VADER](https://github.com/cjhutto/vaderSentiment) on the corpus of tweets, resulting in a positive and negative sentiment score for each row of the dataset. 
* I used two different libraries to conduct dynamic topic modeling: [gensim's LdaSeqModel](https://radimrehurek.com/gensim/models/ldaseqmodel.html) and [BERTopic](https://maartengr.github.io/BERTopic/api/bertopic.html).  
* Using [Streamlit](https://streamlit.io/), I created a simple interactive app  


### Analysis

After grouping the sentiments by month and plotting them using Seaborn, I find that the negative sentiment regarding Covid vaccines grew significantly in June-July 2021, which is around the time that the FDA had given emergency authorization use for the general public. However, what is somewhat surprising is that positive sentiment has stayed somewhat constant over time.

![Sentiment over time](/nlp/project/images/sentiment_time.png)

### Moving forward

I will move on next to Dynamic Topic Modeling (DTM) using gensim's Ldaseqmodel function. If I have time, I would like to build an app to showcase my results using Streamlit/Herokuapp.