# Literature Review

1. Augenstein, Isabelle, Christina Lioma, Dongsheng Wang, Lucas Chaves Lima, Casper Hansen, Christian Hansen, Jakob Grue Simonsen . MultiFC: A Real-World Multi-Domain Dataset for Evidence-Based Fact Checking of Claims. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 4677–4691, nov 2019. URL http://arxiv.org/abs/1909.03242.
    This paper presents a large real-world fact-checking dataset, which consists of 34,918 claims from 26 English fact-checking websites. Each set is accompanied by rich metadata and 10 evidence pages retrieved from Google search. Within each claim, entities such as people and places are also detected, disambiguaated, andn linked to their corresponding Wikipedia page. 

2. Ding, Lixuan, Lanting Ding, and Richard O. Sinnott. "Fake News Classification of Social Media Through Sentiment Analysis." International Conference on Big Data. Springer, Cham, 2020.
    In this paper, Sinott et al. test the hypothesis that fake news on social media typically deals with emotive topics and that a neural network equipped with sentiment classification will, therefore, perform well in fake news detection. In doing so, they train their models using Naive Bayes, Decision Tree, and bi-LSTM for sentiment classification and feature selection. News from *FakeNewsNet* and *CredBank* are employed for the algorithm's development. Their final results demonstrate that sentiment analyses can help improve the discrimination of fake news from real news.

3. Kaliyar, Rohit Kumar, et al. "FNDNet–a deep convolutional neural network for fake news detection." Cognitive Systems Research 61 (2020): 32-44.
    In a recent experimental project similar to our own, Kaliyar et al. test the efficacy of a deep convolutional neural network designed to automatically learn the discriminatory features for fake news classification. They benchmark their model using comprehensive datasets and consider various perfomance evaluative parameters such as Wilcoxon, false positive, and true negative to validate their results. Much to our amazement, the research group reports that their model acheived 98.36% accuracy in fake news detection.

4. Schuster, Tal, Darsh J Shah, Yun Jie Serene Yeo, Daniel Filizzola, Enrico Santus, Regina Barzilay. Towards Debiasing Fact Verification Models. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 3410–3416, 2019. ISBN 9781950737901. doi: 10.18653/v1/d19-1341. URL https://arxiv.org/pdf/1908.05267.pdf.
    In this paper, Schuster et al. addresses checking whether a claim is natural or synthetic (modified from its original version) and proposes methodology for debiasing Fact-Verification datasets. Schuster et al. proposes to synthesize each claim into a pair -- one that is supported and the one that is refute dby the evidence -- in order to prevent models from relying on cues from the claims. Another solution offered is  an algorithm that gives more weights to claims containing give-away phrases of the opposite label to balance out their biasing effect. 
    
## Additional Considerations:
1. Oshikawa, Ray, Jing Qian, William Yang Wang. A Survey on Natural Language Processing for Fake News Detection. In Proceedings of the 12th Language Resources and Evaluation Conference, pages 6086–6093, nov 2018. URL http://arxiv.org/abs/1811.00770.

2. Thorne, James and Andreas Vlachos. Automated Fact Checking: Task Formulations, Methods and Future Directions. In Proceedings of the 27th International Conference on Computational Linguistics, pages 3346–3359, jun 2018. URL http://arxiv.org/abs/1806.07687.

![Image](https://ichef.bbci.co.uk/images/ic/400xn/p088bnqx.jpg)
