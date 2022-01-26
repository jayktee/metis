#app.py

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

import gensim
from gensim.corpora.mmcorpus import MmCorpus
from gensim.test.utils import datapath
from gensim.models import LdaSeqModel
import pyLDAvis
import pyLDAvis.gensim_models

#from bertopic import BERTopic

#import pickle
#print("printing", pickle.__doc__)

## load previously saved corpus
#CORPUS_URL = ('/Users/joycetagal/Downloads/untitled folder/data/corpus_moredata_tv.mm')
#MODEL_URL = ('/Users/joycetagal/Downloads/untitled folder/data/models/ldamodel_moredata_tv')

CORPUS_URL = ('./nlp/streamlit/data/corpus_moredata_tv.mm')
MODEL_URL = ('./nlp/streamlit/data/models/ldamodel_moredata_tv')

st.set_page_config(layout="wide")

@st.cache
def load_corpus(path):
    mm = MmCorpus(path)
    for document in mm:
        pass
    return mm

@st.cache
def load_model(path):
    model = LdaSeqModel.load(path)
    return model

data_load_state = st.text('Loading data...')
corpus = load_corpus(CORPUS_URL)
data_load_state.text("Corpus done! (using st.cache)")

model_load_state = st.text('Loading model...')
model = load_model(MODEL_URL)
model_load_state.text("Model done! (using st.cache)")


st.title('Covid-19 vaccine Dynamic Topic Modelling')
st.header("Introduction")
st.write("In this project, the goal was to analyze changes in Covid-19 vaccine sentiment and concerns over time. To achieve this, I conducted dynamic topic modeling and sentiment analysis on a corpus of 100,000 tweets scraped from Twitter over the year 2021. In particular, I wanted to understand the changes in anti-vaccine sentiment over time, and what were some of the leading keywords that would show up in anti-vaccine sentiment.")

st.header("Tools and Methodology")
st.write("To clean and process the data, I used several different text pre-processing tools including NLTK, SKLearn and Demoji. I used VADER to analyze sentiment over time, and for the dynamic topic modeling I used two libraries: gensim's LdaSeqModel and BERTopic. The results from the dynamic topic modeling are displayed below. The full code is available on my [Github repo](https://github.com/jayktee/metis/tree/master/nlp).")

st.header("gensim LDA visualizations")
st.write("I used gensim's LdaSeqModel to develop a dynamic topic model over 2021, with 4 time slices of 3 months each. Using pyLDAvis, we are able to create an interactive intertopic distance map for each specific timeslice. By hovering over each topic bubble or clicking through the previous or next topic buttons, we can see the frequency of global keywords within the selected topic in red.")
st.write("Looking at some of these topics in greater detail, we start to notice some interesting sentiments. For example, Topic 8 in Time 0 shows a lot of anxiety over vaccine reactions, with keywords such as 'heart', 'effect', 'clot' and so on.")

st.subheader("Time = 0 (Jan-Mar 2021)")
doc_topic, topic_term, doc_lengths, term_frequency, vocab = model.dtm_vis(time=0, corpus=corpus)
vis_dtm = pyLDAvis.prepare(topic_term_dists=topic_term, doc_topic_dists=doc_topic, doc_lengths=doc_lengths, vocab=vocab, term_frequency=term_frequency)
py_lda_vis_html = pyLDAvis.prepared_data_to_html(vis_dtm)
components.html(py_lda_vis_html, width=1400, height=800)

st.subheader("Time = 3 (Oct-Dec 2021")
doc_topic2, topic_term2, doc_lengths2, term_frequency2, vocab2 = model.dtm_vis(time=3, corpus=corpus)
vis_dtm2 = pyLDAvis.prepare(topic_term_dists=topic_term2, doc_topic_dists=doc_topic2, doc_lengths=doc_lengths2, vocab=vocab2, term_frequency=term_frequency2)
py_lda_vis_html2 = pyLDAvis.prepared_data_to_html(vis_dtm2)
components.html(py_lda_vis_html2, width=1400, height=800)

st.write("One downside of pyLDAvis is that we cannot view the changes in the topic over time. For example, Topic 8 in Time 3 does not seem to change significantly, and we cannot understand whether or not the anxieties regarding side effects reduced over time.To view changes in topics over time, I instead use the library BERTopic to consider trends in topics over time.")

st.header("BERTopic Dynamic Topic Modeling")
st.subheader("Intertopic distance map")
cola, colb = st.columns([2,6])
with cola:
    st.write("The intertopic distance map here shows the 400 topics created by BERTopic. The size of the circle represents the frequency of topics, and the distance between circles represents the similarity of topics. By hovering over each circle, we can see the top 5 terms represented in the topic.")
    st.write("We can see that the larger circles, such as Topic 0, represent the largest (most mainstream) topics, such as mask-wearing and staying indoors. However, by hovering over some of the smaller circles, such as Topic 271 or Topic 86, we begin to see some anti-vaccine sentiments, with keywords such as 'infertility' and 'ivermectin'.")

with colb:
    HtmlFile = open("./nlp/streamlit/images/intertopic_distance.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=700, width=900)

st.header("BERTopic Topics over time")
st.subheader("Topic word scores")
c1, c2 = st.columns((1, 5))
with c1:
    c1.write("The topic word scores chart here show the top 5 terms in the selected top 7 topics, with the bars representing the frequency of the term within the selected topic. ")
    
with c2:
    HtmlFile = open("./nlp/streamlit/images/topic_word_scores.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=500, width=1100)

st.subheader("Topics over time")

with st.container(): 
    HtmlFile = open("./nlp/streamlit/images/topics_over_time.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, height=500, width=1200)

st.write("Using the BERTopic topics_over_time function, we can view specific topics and their trends over time. Here, we see the top 10 Topics for the year and the top 4 words in the global topic representation. We can also click on specific topics in the legend to toggle the topic trend on and off the chart.")
st.write("We can see here that the top topic (Topic 0) for Covid-19 vaccines involed mask-wearing and safe behavior. This topic peaked around July 2021, which was around the time that a majority of Americans were vaccinated.")
st.write("Similarly, by hovering over Topic 1 in March 2021, we can see some keywords which may have to do with anti-vaccine sentiment, including the hashtag #faucidossier (Google it). We also see that Topic 3, which has to do with vaccines for children and going back to school is rising over the year.")
st.write("Following vaccine hesitancy or anxiety over time, we can see that Topic 9 has keywords that have to do with vaccine side effects and is decreasing over time.Although we cannot conclude conclusively that anti-vaccine sentiment overall decreased over the year, Topic 9 is possibly representative of the general fears of vaccines declining as more people got their shot.")