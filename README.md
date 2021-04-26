*Project Members: Chira Levy, Hussein Faara, Jorge Rodriguez*

## Project Updates: 
Keep up to date with our work through our [Project Updates page](project-updates.md)! 

## Introduction
With the advent of social media, many barriers required to publish information are effectively removed, granting many individuals and organizations the ability to rapidly disseminate information to reach mass audiences. It is no surprise,then,that this enhanced ability can be used to spread true and false information, and has become an important concern, fueling a growing demand for the fact-checking of online content.

In journalism, fact-checking is the task of assessing the validity, or veracity, of a claim. It is a task that is usually performed manually by trained fact-checkers: typically the procedure entails verifying whether a piece of text or a claim is accurate by utilizing relevant information from various trustworthy sources to infer whether a claim is factually supported or not. This procedurecan be very time consuming depending on a couple of parameters: for example, the complexity of the claim and the evidence needed to provide a verdict. With online news outlets on the rise and an increasingly engaged global social media base,  there is a growing need to fact-check and detect potential loci of misinformation (e.g. fake news) found in information providers across the internet in a more  efficient  manner. In fact, in 2020  alone, fake news websites significantly increased their share of engagement on social media platforms making up nearly one fifth (17%) ofall likes, shares, comments – a stark contrast to roughly 8% in 2019. These figures bear significant importance as interactions with fake news and fake claims on social media can potentially exacerbate political polarization, quickly skew opinions, and negatively influence how people perceive crises – for  example, the ongoing SARS-CoV-2 pandemic. This raises the question: what, then, can be done to help journalists and trained fact-checkers address and mitigate the fake news and misinformation problem? Enter fact-checking and classification. 

Fact-Checking can be traced back to 2011, when scholars Cohen et al. suggested it as one of the tasks that should (at the very least) be aided by machines, or automated since the relevant technology begins to suggest the possibility. Later in 2014 the task is not only introduced by Vlachos and Riedel but they also compile a data set and propose an end-to-end algorithm suitablefor completing the task. Subsequent research over the past 6 years has demonstrated the popularityof the task. This rise in popularity is partly due to the progress made in relevant fields like Natural Language Processing, information retrieval, and increased access to robust data sets/bases.

As part of the ongoing discourse in the field, this project will attempt to provide a comprehensive overview of the state of the field, as well as address what is a significant lack of oversight in quality filters of social media companies by taking a more deliberate approach in classifying what is misinformation and what is not. Using a neural network classifier trained on recent datasets, our goal is to flag articles that either intentionally or unintentionally include

```diff
Should we end this sentence with: 
- "untrue statements about COVID or COVID-related topics."
- "misinformation." 
```
We aim for at least 85% accuracy and specifically less than 7.5% of false negatives (news classified as trustworthy when not). If time allows, we hope to use text summarization to create digestible versions of trustworthy sources (END HERE OR INCLUDE: "that include pertinent information regarding COVID, but require specialized knowledge in the field"). A technical challenge we will face is the reliance of the data used to train our classifier. Most, if not all, of the state-of-the-art fake news detection systems rely on data that could easily be converted into a vector and fed to a model.

##What is Fact-Checking? 
From a researcher’s point of view, Vlachos and Riedel (2014) define fact-checking as “the assignment of a truth value to a claim made in a particular context.” Traditionally the task hasbeen commonly performed by trained professionals. In fact, a trained fact-checker must consolidate previous publications or known  facts, combined with reasoning, to reach a verdict on an articlebefore publishing it. Due to the large amount of content produced and shared each second on onlineoutlets and social media nowadays, false information spreads at an unprecedented speed. The time-consuming traditional method of fact-checking is clearly insufficient. Fortunately,rapid progress in the fields of natural language processing, databases, and information retrievalover the past decade have made delegating the task to machines more plausible. Therefore, apartfrom attempting to accurately assess the truthfulness of claims, automated fact-checking attemptsto reduce the human burden of assessing such claims.

Although what an automated fact-checking system should do is intuitive, several scholars haveframed it in different ways.  For example, Vlachos and Riedel highlight that it is not necessarily abinary classification task because many statements are neither completely true nor completely false.As a result, some fact-checking data sets label the claims with varying veracity levels. Accordingto Hassan et al., an ideal automated fact-checking system should not only be able to make accurateassessments, but should also be fully automated, instant, and accountable. This is very challengingtask because it requires solving the often  difficult computational problems of natural language,understanding context, retrieving relevant information, and reasoning. Furthermore, an ability toexplain its decision with supporting evidence from trusted sources is generally expected of any good automated fact-checking system, complicating the task even further.

## Methods:
  There is a tendency in people to conceive what they read from news sources and/or social media sites to be completely true -- even if the news source admits to their mistakes retroactively. It is important to identify fake news from the real news and/or check whether claims made are valid or not -- especially during our protracted times with the SARS-COV-2 virus. This problem can be tackled with the help of Natural Language Processing tools which will aid in identifying fake or reliable news based on historical data. The following is an outline of how we plan on constructing our classifier and what data sets it will be pulling from in the training process. 
  
  We constructed our classifier with the help of libraries like Keras and Tensorflow, to ensure proper understanding of its function and to ease modifications when deemed necessary. The classifier is a recurrent convolutional neural network model that consists of several different types of sequential operations and layers:
1. We will utilize a tokenizer to transform each article into a vector of indexed tokens (1 token = 1 word).
2. Word Embedding Layers 
3. 1D convolutional and max-pooling layers.
4. Long Short-Term Memory layers.

### Datasets:
The following datasets will prove useful in our experiments:
1. [Fake News Data](https://www.kaggle.com/c/fake-news/data)
2. [COVID-19 Fake News Dataset 1](https://www.kaggle.com/arashnic/covid19-fake-news)
3. [COVID-19 Fake News Dataset 2](https://www.kaggle.com/thesumitbanik/covid-fake-news-dataset)

Our classifier was trained on a general data set (the first linked data set above) of news articles that fall under two labels: Real or Fake. We will do some preliminary analysis using the LDA module from Scikit-learn and the pyLDAvis library to compare topics and most significant terms in real and fake news articles. Our hope is to create an interactive visualization of the aforementioned details for both real and fake news. Subsequent sections will take a closer look at the results. 

### Results: 
(INSERT RESULTS HERE)




## Discussion Outline: 
The bulk of our project attends to the datasets 1 and 2 enumerated in our "Datasets" section. To better understand our data set, we think it is important to consider the distribution of fake news versus real news, length of articles, and even the topic breakdown of the articles sourced from the data sets we selected for this project. Other metrics that allow us to understand distinguishing features between real and fake news is Perplexity and Coherence. 

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)

While accuracy is a useful metric to assess the performance of a classifier, it fails to tell us how the model is performing relative to each class. In order to have a robust understanding of our classifier's performance, we will be presenting a confusion matrix to understand the distribution of true positives, false positives, false negatives, and true negatives. In addition, we hope to compose a classification report to provide the Precision, Recall, and F-score of our model. With a working understanding of our model's performance, we will reference papers that explore data sets used for classifiers deployed to assess the veracity of articles in order to discuss relevant considerations in our own classifier and data set. Our recurrent convolutional neural network will hopefully fair against other classifiers. If not, then we hope to explore avenues for further work as well as limitations in the task. 

## Ethical Concerns

While the benefits of accurate fact-checking systems are obvious, there are also some practical concerns that deserve attention. Relevant is the question: What are the consequences of deploying automated fact-checking systems?
Important to understanding the possible consequences of deploying these systems is exploring how real-life people interact with such systems. Nguyen et al. explores this through their exam- ination of how users interact with AI fact-checking systems. Their system in the experiment is a transparent and interactive human-AI interface that helps users decide when to trust its decision. They observe that AI can be both helpful and misleading through their user study that asks par- ticipants to use the system to aid their personal assessment of a claim’s truthfulness. Particularly concerning is that the user’s accuracy improve on statements that are correctly classified and falls on statements that are incorrectly classified. What is clear is the following: On the one hand, fact- checking tools could indeed increase an individuals accuracy in deciding whether to trust a claim; on the other hand, it runs the risk of reducing an individual’s exercising of personal judgment should the tool makes systematic mistakes.

Another issue is raised by Oshikawa et al.. While one could argue that meta-data helps the accuracy in fact-checking and fake news detection, it is wise to consider the problematic nature of a fact-checking system’s assessment of a claim’s source – e.g. the person, news network, organization. This is even more clear in the case of determining whether something is truthful based on the claim’s author. For example, a system may learn to attach high trustworthiness to prominent political figures or reputable news sources; consequently, this could lead to the silencing of less prominent but reputable voices. In a similar venue, the question of who is accountable for a system’s errors is brought into the spotlight. Nguyen et al. and Oshikawa et al. address two different yet equally valid points. As is the case with any of machine learning tool, the creators of automated fact-checking systems are responsible for detecting and minimizing bias in their systems. However, users bear some responsibility in using these tools as aids to help (not replace) their ability to judge claims.




## Related Works
For a more comprehensive look at the resources that inform our work, please refer to our [literature review](literature-review.md).

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

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)

