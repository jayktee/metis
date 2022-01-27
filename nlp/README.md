#  Analyzing Covid-19 vaccine hesitancy: A Twitter analysis

In this project, the goal was to analyze changes in Covid-19 vaccine sentiment and concerns over time. To achieve this, I conducted dynamic topic modeling and sentiment analysis on a corpus of 100,000 tweets scraped from Twitter over the year 2021. In particular, I wanted to understand the changes in anti-vaccine sentiment over time, and what were some of the leading keywords that would show up in anti-vaccine sentiment. 

### Work completed and tools used

* Used Tweepy to scrape the Twitter API using the keyword "covid+vaccine" with an average of 5000 tweets extracted per month, resulting in over 63,000 tweets.
* Data cleaning: Removed all digits and punctuation and replaced emojis with emoji description using Demoji. 
* For the sentiment analysis, I chose to not lemmatize, stem or remove stopwords to avoid affecting later sentiment analysis. For dynamic topic modeling, I used NLTK's [WordNetLemmatizer](https://www.nltk.org/api/nltk.stem.wordnet.html#nltk.stem.wordnet.WordNetLemmatizer) and [LancasterStemmer](https://www.nltk.org/_modules/nltk/stem/lancaster.html) to stem and lemmatize the corpus of tweets.
* I then ran [VADER](https://github.com/cjhutto/vaderSentiment) on the corpus of tweets, resulting in a positive and negative sentiment score for each row of the dataset. 
* I used two different libraries to conduct dynamic topic modeling: [gensim's LdaSeqModel](https://radimrehurek.com/gensim/models/ldaseqmodel.html) and [BERTopic](https://maartengr.github.io/BERTopic/api/bertopic.html).  
* Using [Streamlit](https://streamlit.io/), I created a simple interactive app linked [here](https://share.streamlit.io/jayktee/metis/nlp/streamlit/app.py) to showcase the results interactively.


### Analysis

I used gensim's LdaSeqModel to develop a dynamic topic model over 2021, with 4 time slices of 3 months each. Using pyLDAvis, we are able to create an interactive intertopic distance map for each specific timeslice. By hovering over each topic bubble or clicking through the previous or next topic buttons, we can see the frequency of global keywords within the selected topic in red. Looking at some of these topics in greater detail, we start to notice some interesting sentiments. For example, Topic 8 in Time 0 shows a lot of anxiety over vaccine reactions, with keywords such as 'heart', 'effect', 'clot' and so on.

One downside of pyLDAvis is that we cannot view the changes in the topic over time. For example, Topic 8 in Time 3 does not seem to change significantly, and we cannot understand whether or not the anxieties regarding side effects reduced over time.To view changes in topics over time, I instead use the library BERTopic to consider trends in topics over time.

Using the BERTopic topics_over_time function, we can view specific topics and their trends over time. Here, we see the top 10 Topics for the year and the top 4 words in the global topic representation. We can also click on specific topics in the legend to toggle the topic trend on and off the chart.

We can see here that the top topic (Topic 0) for Covid-19 vaccines involved mask-wearing and safe behavior. This topic peaked around July 2021, which was around the time that a majority of Americans were vaccinated.

Similarly, by hovering over Topic 1 in March 2021, we can see some keywords which may have to do with anti-vaccine sentiment, including the hashtag #faucidossier (Google it). We also see that Topic 3, which has to do with vaccines for children and going back to school is rising over the year. Following vaccine hesitancy or anxiety over time, we can see that Topic 9 has keywords that have to do with vaccine side effects and is decreasing over time.Although we cannot conclude conclusively that anti-vaccine sentiment overall decreased over the year, Topic 9 is possibly representative of the general fears of vaccines declining as more people got their shot.

### Conclusions

Using dynamic topic modeling libraries such as gensim and BERTopic, we are able to understand in better detail how topics changed over time, including frequency (popularity) and keywords. This methodology could be helpful particularly in public health campaigns to better understand vaccine hesitancy.