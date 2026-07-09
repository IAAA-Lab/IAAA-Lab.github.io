---
title: A framework for the automated thematic annotation of Open Government Data
subtitle:  
layout: post
image: /images/posts/2026-07-05-workflow.png
categories: [Paper overview]
---

Governmental policies for transparency and reuse of public sector information have encouraged the launch of open government data portals around the world. Many of these portals are based on pyramidal structures: national open data portals are aggregators of the contents harvested from open data portals maintained by governments in charge of administrative areas with a narrower scope. Taking into account this hierarchical organization, these open data portals lack consistent and scalable mechanisms for thematic annotation, limiting dataset discoverability. 

Our paper, published in ComSIS journal, proposes a framework for the automated thematic classification of open government data. The framework integrates (i) thematic annotation quality assessment, (ii) supervised machine learning models trained on annotated metadata corpora, and (iii) embedding-based semantic similarity methods for theme assignment in the absence of reliable annotations. 

![Fig. 1. Workflow for the automated thematic annotation of OGD]({{ site.baseurl }}/images/posts/2026-07-05-workflow.png){: .center-image width="80%"}
<h4><center><b>Fig. 1. Workflow for the automated thematic annotation of OGD</b></center></h4>

The framework is evaluated using 29,793 datasets from data.europa.eu, the European open data portal. 

![Fig. 8. Distribution of datasets with respect to the 20 most frequent combinations of themes.]({{ site.baseurl }}/images/posts/2026-07-05-distribution.png){: .center-image width="50%"}
<h4><center><b>Fig. 8. Distribution of datasets with respect to the 20 most frequent combinations of themes.</b></center></h4>

Experimental results show that supervised models achieve high classification performance, with Support Vector Machines reaching an accuracy of 93.65%, while unsupervised embedding-based approaches achieve substantial semantic agreement with portal-assigned themes (74.56%) using transformer-based representations. These results demonstrate that the proposed framework enables scalable, consistent, and interoperable thematic annotation, offering both theoretical contributions to automated metadata enrichment and practical value for integration into large-scale open data portal infrastructures. 


---
[A framework for the automated thematic annotation of Open Government Data.](https://doi.org/10.2298/CSIS251029022A)  A. AZIZ, M. ALI, D.J. HERRERA-MURILLO, M.I. MARATSI, F.J. LOPEZ-PELLICER, J. NOGUERAS-ISO. Computer Science and Information Systems, vol. 23(2), p. 917-946, 2026.

---
