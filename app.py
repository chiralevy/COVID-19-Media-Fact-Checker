import requests
import numpy as np
import pandas as pd
import streamlit as st 
import tensorflow as tf
import urllib.request, json
from tensorflow import keras
from bs4 import BeautifulSoup
from keras_preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

"""
# Fake News Classifier 
This is a simple classifier. There are two options:
1. General News: With this option, the classifier takes in an article and tells you if the article is fake news or not. It was trained on a data set including articles of real and fake news. 
2. Covid News/Claims: With this option, the classifier takes in either text input about a covid claim or a covid-related news article url. Based on the claim or url, the classifier will tell you if the truthfulness of the claim/article. This classifier was trained on a data set including covid-related articles/claims.  

"""

def predict(url, inference):
    if url != "":
        try:
            news_content = []
            response = requests.get(url)
            # opening the url for reading
            html = urllib.request.urlopen(url)

            # parsing the html file
            htmlParse = BeautifulSoup(html, 'html.parser')

            # Getting the title
            title = htmlParse.find('title').get_text()

            # Reading the content (it is usually divided into paragraphs)
            article = requests.get(url)
            article_content = article.content

            # getting all the paragraphs
            body = htmlParse.find_all("p")

            # Unifying the paragraphs
            list_paragraphs = []
            for p in np.arange (0, len(body)):
                paragraph = body[p].get_text()
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)

            news_content.append(final_article)

            # df_features
            url_data = pd.DataFrame(
                 {'text': news_content 
                })

            # Pad the data similarly to how it was padded with the training data
            sequences = tokenizer.texts_to_sequences(url_data['text'])
            padded = pad_sequences(sequences, maxlen=512, padding='post', truncating='post')

            # Get the model's prediction on url's news article
            pred = inference.predict(padded)

            f"""
            # Article: {title}.
            ## This article **{'is' if pred < 0.5 else 'is not'}** Fake News.
            ### Probability of Real News: {pred.item()*100: .2f}%
            """
        except:
            st.text("Problem reading article from", url)

            
def covid_predict(url, inference):
    if url != "":
        try:
            content = []
            response = requests.get(url)
            # opening the url for reading
            html = urllib.request.urlopen(url)

            # parsing the html file
            htmlParse = BeautifulSoup(html, 'html.parser')
            
            print('reading file')
            # Getting the article title/claim
            title = htmlParse.find('title').get_text()
            
            content.append(title)
            
            df = pd.DataFrame(
                 {'text': content
                })
            
            # Pad the data similarly to how it was padded with the training data
            sequences = tokenizer.texts_to_sequences(df['text'])
            padded = pad_sequences(sequences, maxlen=80, padding='post', truncating='post')

            # Get the model's prediction on url's news article
            pred = inference.predict(padded)

            f"""
            # Article/Claim: {title}.
            ## This article/claim **{'is' if pred < 0.5 else 'is not'}** False.
            ### Probability of Truthfulness: {pred.item()*100: .2f}%
            """
        except:
            st.text("Problem reading article/claim from", url)
            
def covid_claim_pred(claim, inference):
    if claim != "":
        try:
            content = []
            content.append(claim)
            
            # Turning the claim into a data frame
            df = pd.DataFrame(
                             {'text': content
                            })
            
            
            # Pad the data similarly to how it was padded with the training data
            sequences = tokenizer.texts_to_sequences(df['text'])
            padded = pad_sequences(sequences, maxlen=80, padding='post', truncating='post')

            # Get the model's prediction on url's news article
            pred = inference.predict(padded)

            f"""
            # Claim: {claim}.
            ## This claim **{'is' if pred < 0.5 else 'is not'}** False.
            ### Probability of Truthfulness: {pred.item()*100: .2f}%
            """
        except:
            st.text("Problem reading user input from", claim)
            
            
# Application Interface

option = st.radio("", ["General News", "COVID News"])

if option == "General News":
    url = st.text_input("Please input a url.")
    
    # Load the model and tokenizer
    general_news_inference = keras.models.load_model("code-general/rcnn2-model")
    with open('code-general/rcnn2-tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    
    # Predict based on the URL
    predict(url, general_news_inference)

else:
    covid_options = st.radio("", ["URL", "Claim"])
    
    # Load the model and tokenizer
    covid_inference = keras.models.load_model("code-covid/covid-model-1")
    with open('code-covid/covid1-tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    if covid_options == "URL":
        covid_url = st.text_input("Please input a covid-related url.")
   
        # Predict based on the URL
        covid_predict(covid_url, covid_inference)
    else:
        user_input = st.text_input("Please input a covid-related claim.")
        
        # Predict based on the claim
        covid_claim_pred(user_input, covid_inference)

        

    
