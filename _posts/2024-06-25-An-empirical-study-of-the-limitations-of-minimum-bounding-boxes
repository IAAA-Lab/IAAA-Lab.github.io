---
title: An empirical study of the limitations of minimum bounding boxes for defining the extent of geospatial resources
subtitle: the use of DGGS and other alternatives for improving the performance of spatial searches
layout: post
image: /images/posts/2024-06-21-oldText.png
categories: [Paper overview]
---

In the domain of geospatial data management, accurately defining the extent of a resource is crucial for effective search and retrieval. Traditionally, Minimum Bounding Boxes (MBB) have been the go-to method for this purpose. However, in this paper we conducted an empirical study to reveal that MBBs often fall short in terms of precision (returning false positive results such as Figure 1), leading to less effective spatial searches.

![Figure 1]({{ site.baseurl }}/images/posts/tgis_a_2361274_f0001_c.jpg)
<center>**Figure 1.** Example of a false positive result, where the bounding box of the resource (green big
rectangle, associated with a dataset describing the Spanish coast lines) intersects with the query
area (blue smaller rectangle) but there are no features (red geometries around the coast) inside
that query area.</center>

To adress these limitations, we compared three methods for defining the extent of geospatial resources: Minimum Bounding Boxes (MBB), Convex Hulls, and Discrete Global Grid Systems (DGGS). The study utilized a rich dataset from major European geospatial data catalogs to evaluate the performance of these methods
The results showed that the MBB method, while easy to implement, suffer a significant gap in precision, with accuracy ranging between 73% and 97%. This variability can lead to a high number of false positives, making spatial searches less reliable.
However, our proposed method, the DGGS (Figure 3) demonstrated a remarkable precision rate between 96% and 99%.

![Figure 3]({{ site.baseurl }}/images/posts/tgis_a_2361274_f0003_c.jpg)
<center>**Figure 3.** Example of rHEALPix DGGS cells that cover a dataset.</center>

The transition to DGGS represents a significant leap forward for geospatial data management. We also propose a pragmatic roadmap for integrating DGGS into existing infrastructures, highlighting the potential for reduced false positives and improved search accuracy.
This study showcases the potential of DGGS to transform geospatial data retrieval. By adopting these advanced techniques, we can enhance the accuracy and reliability of spatial searches, paving the way for better data discovery.

---

[An empirical study of the limitations of minimum bounding boxes for defining the extent of geospatial resources: the use of DGGS and other alternatives for improving the performance of spatial searches](https://doi.org/10.1080/13658816.2024.2361274). S. MARTIN-SEGURA, F. J. LOPEZ-PELLICER, R. BÉJAR, J. NOGUERAS-ISO F. J. ZARAZAGA-SORIA. International Journal of Geographical Information Science, pp. 1–20.
