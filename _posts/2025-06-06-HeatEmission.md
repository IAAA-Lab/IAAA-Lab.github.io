---
title: Detection of changes in the heat emissions signature of buildings related to indoor activity using publicly available satellite data
subtitle:
layout: post
categories: [Paper overview]
---

The detection of human activity in isolated structures is crucial for improving surveillance and resource management in remote rural areas, where communication infrastructure and sensor networks are often nonexistent. This study investigates the possibility of using publicly available satellite data to infer thermal emissions associated with the presence of people or livestock in pig farms located in the Ebro Valley (the municipalities of Albalate, Ballobar, Granén, and Tamarite). Although the typical range for detecting human heat (8,000–14,000 nm) does not match the bands available on Sentinel-2, band 12 (SWIR, around 2,200 nm) provides spectral information that can be indirectly correlated with thermal variations inside buildings. To overcome the limitations of the spatial and radiometric resolution, machine learning techniques were applied to learn patterns of thermal emission from the spectral response of this band and meteorological data, particularly daily temperature collected between 2021 and 2023.

![Figure 1: Methodology Workflow]({{ site.baseurl }}/images/posts/2025-06-06-Fig1.png){: .center-image width="50%"}
<h4><center><b>Figure 1: Methodology Workflow</b></center></h4>

A total of 281 Sentinel-2 band 12 images covering the four farms in 2021 were collected, of which 206 corresponded to occupied periods (when animals were housed) and 75 to periods without livestock presence. Each image was clipped using vector files created in QGIS to extract only the pixels corresponding to the buildings, ensuring that each installation of at least 15 × 15 m was represented by at least one 20 m × 20 m pixel. At the same time, daily temperature data (minimum, maximum, and mean) from the nearest meteorological stations were obtained via the AEMET portal and integrated as additional channels or pixels in the images.

![Figure 3: Creation of farm shapefiles]({{ site.baseurl }}/images/posts/2025-06-06-Fig3.png){: .center-image width="50%"}
<h4><center><b>Figure 3: Creation of farm shapefiles</b></center></h4>

To increase training diversity and mitigate class imbalance, 3866 samples were generated through random rotation, horizontal/vertical shifts, and zoom to balance the dataset.
The final dataset was split into 70 % for training, 15 % for validation, and 15 % for testing. Four models were evaluated: Dense Neural Networks (DNN), Convolutional Neural Networks (CNN), XGBoost, and LightGBM, with hyperparameters optimised using Optuna, and performance measured by accuracy, AUC, precision, recall, and F1-score.

![Figure 4: Pixels selection]({{ site.baseurl }}/images/posts/2025-06-06-Fig4.png){: .center-image width="50%"}
<h4><center><b>Figure 4: Pixels selection</b></center></h4>

The results show that incorporating temperature data significantly improves the performance of all models. XGBoost achieved the best classification on the test set, reaching 96% accuracy and an AUC of 0.94 when combining band 12 images and temperature, outperforming CNN (accuracy 88%, AUC 0.86) and DNN (accuracy 83%, AUC 0.81) after applying data augmentation techniques. LightGBM remained relatively consistent (accuracy ≈ 81 %, AUC ≈ 0.80) across all scenarios. When performing the “leave-one-farm-out” experiment excluding one farm from training XGBoost’s accuracy dropped to 92 % (AUC 0.90).
In this work, we demonstrate that Sentinel-2 band 12, combined with meteorological data, can be used to indirectly infer the occupancy of remote buildings, achieving robust classification with XGBoost. The methodology offers an affordable alternative to high-resolution thermal sensors, helpful in detecting activity, optimising the management of agricultural facilities, and supporting decision-making in isolated areas.



---
[Detection of changes in the heat emissions signature of buildings related to indoor activity using publicly available satellite data.](https://doi.org/10.1007/s12145-025-01926-6) M.E. SUAZA-MEDINA, J. LACASTA, F.J. LOPEZ-PELLICER, R. BÉJAR, F.J. ZARAZAGA-SORIA. Earth Science Informatics, Volume 18, article number 420, (2025), 2025.


---
