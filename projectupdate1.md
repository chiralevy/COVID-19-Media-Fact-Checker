# Project Update 1
  News media has become a channel to disseminate information (instantly) of the happenings around the world. There is a tendency to believe for people to conceive whatever they read from news sources and/or social media sites to be completely true -- even if the news source admits to their mistakes retroactively. It is important to identify fake news form the real true news -- especially during our protracted times with the COVID virus. The problem can be tackled with  the help of Natural Language Processing tools which will aid in identifying fake or reliable news based on historical data. The following is an outline of how we plan on constructing our classifier and what data sets it will be pulling from for the training process. 

## Software Plan:
We plan to construct our classifier from scratch to ensure proper understanding of its function and to ease modifications when deemed necessary. Tentatively, the classifier will take the form of a recurrent convolutional neural network model that consists of several different types of sequential operations and layers:
1. We will utilize a tokenizer to transform each article into a vector of indexed tokens (1 token = 1 word).
2. Word Embedding Layers 
3. 1D convolutional and max-pooling layers.
4. Long Short-Term Memory layers.

After training the classifier on a subset of the data, we hope to create a confusion matrix and classification report to better visualize the performance of the model. Metrics that will be useful in the assessment include precision, recall, and the f-score. 

Once we have developed something sufficient, our hope is to compare the performance of our software against a pre-existing fake news classifier trained on COVID-related news articles using similar metrics and visualizations. 

## Datasets in Consideration:
The following datasets* will prove useful in our experiments:
1. [COVID-19 Fake News Dataset 1](https://www.kaggle.com/arashnic/covid19-fake-news)
2. [COVID-19 Fake News Dataset 2](https://www.kaggle.com/thesumitbanik/covid-fake-news-dataset)

*Datasets subject to inspection.

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)
