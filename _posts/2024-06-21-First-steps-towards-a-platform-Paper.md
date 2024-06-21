---
title: First steps towards a platform for the analysis of civil law documentary heritage 
subtitle:
layout: post
image: /images/posts/2024-06-21-oldText.png
categories: [Paper overview]
---

Civil law regulates the civil or private relations of persons: it deals with the civil status of persons, their family rights and duties, property and other real rights over things, the regime of obligations and contracts, and successions and inheritances. Although in Europe each country has its own civil law code at the state level, this law dates back to past times and has evolved until present times. In many administrative areas this law has its origin in historical kingdoms that regulated the conditions of settlement of their citizens. The books that publish these historical codes of civil law and the doctrinal works that document their interpretation make up an asset of cultural interest whose study allows us to learn about the political, social, and cultural context of this historical period. Nowadays there are numerous initiatives (e.g. Europeana) that have promoted the digitization of documentary heritage, including that related to civil law. However, simple digitization is not enough. This work is a first step in a research project that aims to promote the study of works of special interest in the field of the history of civil law (specially, civil law authors of XVI, XVII and XVIII centuries) accompanied with the development of the necessary technology to have an online hypertext edition of the works that includes the digital facsimile, a critical edition, a translation and all the complements that are deemed relevant (e.g., legal codes cited and notes or glosses to the text both legal and historical-philological or bibliographical).


![Figure 2. Architecture of our platform ]({{ site.baseurl }}/images/posts/2024-06-21-architecture.jpg){: .center-image width="50%"}
<h4><center><b>Figure 2. Architecture of our platform</b></center></h4>

This paper  presented a first prototype for the development of a web platform to facilitate the analysis of civil law documentary heritage. The design of the platform has been customized to the specific needs of the experts in this domain. First, we have designed a conceptual framework to represent the information required for a deep analysis of civil law contents. In addition, we have integrated open-source tools to assist in tasks such as transcription, translation, and information extraction, which usually require high human resources if performed completely manually. The proposed platform for the analysis of documentary heritage has been implemented using the Django framework for web development. In addition, the components for content management have been implemented in Python integrating different libraries for OCR (Pero-OCR), and named entity recognition (spacy)  and Google Translator API for translation. 

![Figure 5. An example of pages from Miguel del Molino book]({{ site.baseurl }}/images/posts/2024-06-21-oldText.png){: .center-image width="50%"}
<h4><center><b>Figure 5. An example of pages from Miguel del Molino book</b></center></h4>

The feasibility of the implementation has been tested with the processing of a doctrinal civil law book written by Miguel del Molino and printed in 1585: [“Repertorium Fororum et Observantiarum Regni Aragonum: una pluribus cum determinationibus consilii iustitiae Aragonum practicis atquae cautelis eisdem fideliter annexis”](https://derechoaragones.aragon.es/es/consulta/registro.do?id=600036). 



---
[First steps towards a platform for the analysis of civil law documentary heritage.](https://doi.org/10.54886/scire.v30i1.5018). H. NEJI, J. NOGUERAS-ISO, F.J. GARCÍA-MARCO, C. BAYOD LÓPEZ. SCIRE, vol. 30(1) p. 75-83, 2024.


---
