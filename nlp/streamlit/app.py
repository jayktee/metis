#app.py

import streamlit as st
import pandas as pd
import numpy as np
import gensim
from gensim.corpora.mmcorpus import MmCorpus
from gensim.test.utils import datapath
from gensim.models import LdaSeqModel
import pyLDAvis
import pyLDAvis.gensim_models
import streamlit.components.v1 as components

## load previously saved corpus
CORPUS_URL = ('./nlp/streamlit/data/corpus_moredata_tv.mm')
MODEL_URL = ('./nlp/streamlit/data/models/ldamodel_moredata_tv')

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

st.title('Uber pickups')

for topic_id in range(model.num_topics):
    topk = model.print_topic(topic_id)
    topk_words = [w for w, _ in topk ]
    
    st.write('{}: {}'.format(topic_id, ' '.join(topk_words)))

#id2word = dict((v, k) for k, v in corpus.vocabulary_.items())

""" #if hasattr(st.session_state.model, 'inference'):  # gensim Nmf has no 'inference' attribute so pyLDAvis fails
    if st.button('Generate pyLDAvis'):
        #st.session_state.id2word = id2word
        st.session_state.corpus = corpus
        st.session_state.model = model

        with st.spinner('Creating pyLDAvis Visualization ...'):
            #doc_topic, topic_term, doc_lengths, term_frequency, vocab = model.dtm_vis(time=0, corpus=corpus)
            py_lda_vis_data = pyLDAvis.gensim_models.prepare(st.session_state.model, st.session_state.corpus)
            py_lda_vis_html = pyLDAvis.prepared_data_to_html(py_lda_vis_data)
        with st.expander('pyLDAvis', expanded=True):
            st.markdown('pyLDAvis is designed to help users interpret the topics in a topic model that has been '
                        'fit to a corpus of text data. The package extracts information from a fitted LDA topic '
                        'model to inform an interactive web-based visualization.')
            st.markdown('https://github.com/bmabey/pyLDAvis')
            components.html(py_lda_vis_html, width=1300, height=800) """

doc_topic, topic_term, doc_lengths, term_frequency, vocab = model.dtm_vis(time=0, corpus=corpus)
vis_dtm = pyLDAvis.prepare(topic_term_dists=topic_term, doc_topic_dists=doc_topic, doc_lengths=doc_lengths, vocab=vocab, term_frequency=term_frequency)
py_lda_vis_html = pyLDAvis.prepared_data_to_html(vis_dtm)
components.html(py_lda_vis_html, width=1300, height=800)

doc_topic2, topic_term2, doc_lengths2, term_frequency2, vocab2 = model.dtm_vis(time=3, corpus=corpus)
vis_dtm2 = pyLDAvis.prepare(topic_term_dists=topic_term2, doc_topic_dists=doc_topic2, doc_lengths=doc_lengths2, vocab=vocab2, term_frequency=term_frequency2)
py_lda_vis_html2 = pyLDAvis.prepared_data_to_html(vis_dtm2)
components.html(py_lda_vis_html2, width=1300, height=800)


