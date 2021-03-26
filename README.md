## Introduction
Fact-checking and fake-news detection are the task of assessing the validity, or veracity, of a claim and/or news article. It is a task that has usually been performed manually by journalists and the like. For any individual performing the task, the process of verifying whether a piece of text or a claim is accurate usually calls for the involvement of pertinent knowledge from various trustworthy sources and utilizing them to infer that something is factually supported or not. The process can be very time consuming depending on a couple of parameters: for example, the complexity of the claim/article and the evidence needed to subsstantiate the claim/article. With online news outlets being the rise, there is a growing need to fact-check and detect potential locuses of misinformation (i.e. fake news) in a more efficient way in internet circulations of information providers. 

In 2020, fake news websites significantly increased their share of engagement on social media platforms making up nearly one fifth (17%) of all likes, shares, comments. This number is in stark contrast to roughly 8% in 2019. These figures bear significant importance as studies have shown that fake news on social media increases political polarization, quickly skews opinions ([rabbit hole effect](https://www.nytimes.com/2019/03/29/technology/youtube-online-extremism.html)), and negatively influences how people perceive the ongoing COVID-19 crisis. This issue has been quite difficult to address in light of censorship concerns from right-leaning groups, and also due to the ineffectual/low effort quality filters of big tech platforms.

As part of the discussion of computational journalism, automated fact-checking is brought up by scholars like Cohen et al. (2011) as one of the tasks that should be at least aided by machines, or automated. The task of fact-checking was (in our findings) first introduced by Vlachos and Riedel in their 2014 article, "Fact Checking: Task Definition and Dataset Construction," while also constructs a datset and proposes an algorithm for completing the task. Since then, research concerning how to tackle fact-checking and fake news detection via different strategies has garnered popularity over the past 6 years. This rise in popularity is partly due to the progress made in relevant fields like Natural Language Processing, information retrieval, and increased access to robust datasets and databases. This paper/project will attempt to provide a comprehensive overview of the state of the field, as well as address what is a significant lack of oversight in quality filters of social media companies by taking a more deliberate approach in classifying what is misinformation and what is not. Using a neural network classifier trained on recent and comprehensive datasets, our goal is to flag articles — specifically those shared on platforms like Facebook and WhatsApp — that either intentionally or unintentionally include untrue statements regarding COVID or COVID-related topics. We aim for at least 85% accuracy and specifically less than 7.5% of false negatives (news classified as trustworthy when not). If time allows, we hope to use text summarization to create digestible versions of trustworthy sources that include pertinent information regarding COVID, but require specialized knowledge in the field. A technical challenge we will face is the reliance of the data used to train our classifier. Most if not all of the state-of-the-art fake news detection systems rely on data that could easily be converted into a vector and fed to a model. This approach leaves systems vulnerable against certain types 
of fake news, such as machine-generated fake news. 

The overall benefits of accurate fact-checking and fake-news detection to society are obvious. For example, providing marginalized groups that have experienced significant hardship precipitated by the pandemic with accurate information to better protect themselves and their communities. However, there are also some practical societal concerns that deserve attention. One of them being the assessment of an article as truthful or not based on the speaker’s identity. For example, the system may learn to associate political elites or reputable social media accounts with high trustworthiness, which could have an unwanted effect of silencing minority voices. Ultimately, this project aims to help resurface and sharpen the line between fact and fiction in journalism and accelerate the progress to a safer and more 
knowledgeable society.

## Our Project:
  There is a tendency to believe for people to conceive whatever they read from news sources and/or social media sites to be completely true -- even if the news source admits to their mistakes retroactively. It is important to identify fake news form the real true news and/or check whether claims made are valid or not -- especially during our protracted times with the SARS-COV-2 virus. The problem can be tackled with  the help of Natural Language Processing tools which will aid in identifying fake or reliable news based on historical data. The following is an outline of how we plan on constructing our classifier and what data sets it will be pulling from for the training process. 
  We plan to construct our classifier from scratch to ensure proper understanding of its function and to ease modifications when deemed necessary. Tentatively, the classifier will take the form of a recurrent convolutional neural network model that consists of several different types of sequential operations and layers:
1. We will utilize a tokenizer to transform each article into a vector of indexed tokens (1 token = 1 word).
2. Word Embedding Layers 
3. 1D convolutional and max-pooling layers.
4. Long Short-Term Memory layers.

After training the classifier on a subset of the data, we hope to create a confusion matrix and classification report to better visualize the performance of the model. Metrics that will be useful in the assessment include precision, recall, and the f-score. 

Once we have developed something sufficient, our hope is to compare the performance of our software against a pre-existing fake news classifier trained on COVID-related news articles using similar metrics and visualizations. 

## Datasets:
The following datasets* will prove useful in our experiments:
1. [COVID-19 Fake News Dataset 1](https://www.kaggle.com/arashnic/covid19-fake-news)
2. [COVID-19 Fake News Dataset 2](https://www.kaggle.com/thesumitbanik/covid-fake-news-dataset)

*Datasets subject to inspection.

## Related Works
For a more comprehensive look at the resources that inform our work, please take a look at our [literature review](literature-review.md).

1. Augenstein, Isabelle, Christina Lioma, Dongsheng Wang, Lucas Chaves Lima, Casper Hansen, Christian Hansen, Jakob Grue Simonsen . MultiFC: A Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 4677–4691, nov 2019. URL http://arxiv.org/abs/1909.03242.
2. Ding, Lixuan, Lanting Ding, and Richard O. Sinnott. "Fake News Classification of Social Media Through Sentiment Analysis." International Conference on Big Data. Springer, Cham, 2020.
3. Hamid, Abdullah, et al. "Fake News Detection in Social Media using Graph Neural Networks and NLP Techniques: A COVID-19 Use-case." arXiv preprint arXiv:2012.07517 (2020).
4. Kaliyar, Rohit Kumar, et al. "FNDNet–a deep convolutional neural network for fake news detection." Cognitive Systems Research 61 (2020): 32-44.
5. Le, Thai, Suhang Wang, and Dongwon Lee. "Malcom: Generating malicious comments to attack neural fake news detection models." arXiv preprint arXiv:2009.01048 (2020). URL: https://arxiv.org/pdf/2009.01048.pdf
6. Oshikawa, Ray, Jing Qian, William Yang Wang. A Survey on Natural Language Processing for Fake News Detection. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 6086–6093, nov 2018. URL http://arxiv.org/abs/1811.00770.
7. Schuster, Tal, Darsh J Shah, Yun Jie Serene Yeo, Daniel Filizzola, Enrico Santus, Regina Barzilay. Towards Debiasing Fact Verification Models. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 3410–3416, 2019. ISBN 9781950737901. doi: 10.18653/v1/d19-1341. URL https://arxiv.org/pdf/1908.05267.pdf.
8. Tan, Reuben, Kate Saenko, and Bryan A. Plummer. "Detecting Cross-Modal Inconsistency to Defend Against Neural Fake News." arXiv preprint arXiv:2009.07698 (2020). URL: https://arxiv.org/pdf/2009.07698.pdf
9. Thorne, James and Andreas Vlachos. Automated Fact Checking: Task Formulations, Methods and Future Directions. In Proceedings of the 27th International Conference on Computational Linguistics, pages 3346–3359, jun 2018. URL http://arxiv.org/abs/1806.07687.
10. Umer, M., Z. Imtiaz, S. Ullah, A. Mehmood, G. S. Choi and B. -W. On, "Fake News Stance Detection Using Deep Learning Architecture (CNN-LSTM)," in IEEE Access, vol. 8, pp. 156695-156706, 2020, doi: 10.1109/ACCESS.2020.3019735.

Project Members: Chira Levy, Jorge Rodriguez, and Hussein Faara

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)

