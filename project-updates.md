# Project Updates
*formerly 'Project Update 1' page* 

## As of 3/4/2021
  News media has become a channel to disseminate information (instantly) of the happenings around the world. There is a tendency to believe for people to conceive whatever they read from news sources and/or social media sites to be completely true -- even if the news source admits to their mistakes retroactively. It is important to identify fake news form the real true news -- especially during our protracted times with the COVID virus. The problem can be tackled with  the help of Natural Language Processing tools which will aid in identifying fake or reliable news based on historical data. The following is an outline of how we plan on constructing our classifier and what data sets it will be pulling from for the training process. 

## Software Plan
We plan to construct our classifier from scratch to ensure proper understanding of its function and to ease modifications when deemed necessary. Tentatively, the classifier will take the form of a recurrent convolutional neural network model that consists of several different types of sequential operations and layers:
1. We will utilize a tokenizer to transform each article into a vector of indexed tokens (1 token = 1 word).
2. Word Embedding Layers 
3. 1D convolutional and max-pooling layers.
4. Long Short-Term Memory layers.

After training the classifier on a subset of the data, we hope to create a confusion matrix and classification report to better visualize the performance of the model. Metrics that will be useful in the assessment include precision, recall, and the f-score. 

Once we have developed something sufficient, our hope is to compare the performance of our software against a pre-existing fake news classifier trained on COVID-related news articles using similar metrics and visualizations.

## Progress - 3/25/2021
### So far we have: 
- created a timeline/task-list of things to proceed more sure-footed in the project -- also helps divvy up the work!
- cleaned up the repo that will contain our python scripts and project website. 
- familarized ourselves with the datasets we wil use as well as Pytorch's torchtext library. As of tomorrow (Friday, March 26), we will begin preprocessing our data.
### Issues:
- One issue that we've encountered is simply that of our unfamiliarity with torchtext. While we are making progress in grasping this material, the question
  of whether this is the right library to begin with is also of concern.
  
### Desired Grade: 
- We are shooting for an A. We are open to suggestions, advice, etc.
  
## Datasets in Consideration:
The following datasets* will prove useful in our experiments:
1. [COVID-19 Fake News Dataset 1](https://www.kaggle.com/arashnic/covid19-fake-news)
2. [COVID-19 Fake News Dataset 2](https://www.kaggle.com/thesumitbanik/covid-fake-news-dataset)

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)
