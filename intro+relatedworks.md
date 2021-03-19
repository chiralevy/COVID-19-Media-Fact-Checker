## Introduction Outline
In 2020, fake news websites significantly increased their share of engagement on social media platforms making up nearly one fifth (17%) of all likes, shares, 
comments. This number is in stark contrast to roughly 8% in 2019. These figures bear significant importance as studies have shown that fake news on social media 
increases political polarization, quickly skews opinions ([rabbit hole effect](https://www.nytimes.com/2019/03/29/technology/youtube-online-extremism.html)), and 
negatively influences how people perceive the ongoing COVID-19 crisis. This issue has been quite difficult to address in light of censorship concerns from right-
leaning groups, and also due to the ineffectual/low effort quality filters of big tech platforms. 

This paper/project will address what is a significant lack of oversight in quality filters of social media companies by taking a more deliberate approach in 
classifying what is misinformation and what is not. Using a neural network classifier trained on recent and comprehensive datasets, our goal is to flag articles — 
specifically those shared on platforms like Facebook and WhatsApp — that either intentionally or unintentionally include untrue statements regarding COVID or COVID-
related topics. We aim for at least 85% accuracy and specifically less than 7.5% of false negatives (news classified as trustworthy when not). If time allows, we 
hope to use text summarization to create digestible versions of trustworthy sources that include pertinent information regarding COVID, but require specialized 
knowledge in the field. A technical challenge we will face is the reliance of the data used to train our classifier. Most if not all of the state-of-the-art fake 
news detection systems rely on data that could easily be converted into a vector and fed to a model. This approach leaves systems vulnerable against certain types 
of fake news, such as machine-generated fake news. 

The overall benefits to accurate fact-checking to society are obvious. For example, providing marginalized groups that have experienced significant hardship 
precipitated by the pandemic with accurate information to better protect themselves and their communities. However, there are also some practical societal concerns 
that deserve attention. One of them being the assessment of an article as truthful or not based on the speaker’s identity. For example, the system may learn to 
associate political elites or reputable social media accounts with high trustworthiness, which could have an unwanted effect of silencing minority voices. 
Ultimately, this project aims to help resurface and sharpen the line between fact and fiction in journalism and accelerate the progress to a safer and more 
knowledgeable society.

## Related Works
- 

Project Members: Chira Levy, Jorge Rodriguez, and Hussein Faara

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)

