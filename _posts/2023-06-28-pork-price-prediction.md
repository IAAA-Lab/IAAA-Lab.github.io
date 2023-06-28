---
title: Effects of data time lag in a decision-making system using machine learning for pork price prediction
subtitle:
layout: post
categories: [Paper overview]
---

The agricultural sector is important in economies worldwide, necessitating robust price control measures to ensure stability and foster growth. However, price volatility in these markets introduces uncertainty, presenting challenges. Thus, accurate price forecasting becomes paramount for producers to effectively manage their products and reduce risks.

In this investigation, we focused on analyzing the effect of data time lag on price predictions for pork meat in the regional markets in Spain. We analyzed the historical behaviour of other European markets to identify suitable data sources for price prediction. Two types of data were considered: public data with a two-week delay, published by the Ministry of Agriculture, and subscription-based data obtained without delay. 

The data showed a high correlation between the markets of Spain and Portugal, but the strongest correlations have been among Spanish local markets. Other correlations have been found among groups of central European countries, indicating that the European pork market does not work as a unity but as a group of independent regional markets.

The algorithms analyzed included Autoregressive Integrated Moving Average (ARIMA), Seasonal Autoregressive Integrated Moving Average Exogenous mode (SARIMAX), Random Forest (RF), Support Vector Machine for regression (SVR), Extremely Randomized Trees (ERT), Light Gradient Boosting Machine (LGBM), Xtreme Gradient Boosting Machine (XGBM), Ridge, Category Boosting (Catboost), Recurrent Neural Networks (RNN), and Long short-term memory Neural Networks (LSTM).

![Table 2: Comparison of model performances using public and subscription data]({{ site.baseurl }}/images/posts/2023-06-28-Table2.jpg){: .center-image width="80%"}

Table 2 shows the results of each model using public information (with two weeks delays) and subscription information (obtained without delays). The results are ordered by the best R2 in the results, and the RMSE metric is also included.

We have developed a decision support system prototype, integrating the most effective prediction algorithm (the public side of this system is available [here](https://www.preciolonja.es)). This prototype aimed to give market agents real-time insights into price evolution and predict prices, empowering them to make informed pricing decisions. The decision support system aims to improve fairness in price negotiation and general decision-making in the pork market by using machine learning and deep learning algorithms. Figure 4 compares the proposals made by the prediction system and the price agreed upon in the "Lonja" process from May 2022 till the middle of October 2022.

![Figure 4: Comparing Lonja’s proposal and the predicted proposal]({{ site.baseurl }}/images/posts/2023-06-28-Fig4.png){: .center-image width="80%"}

The accurate prediction of agricultural prices, such as pork meat, holds immense value in ensuring stability and facilitating informed decision-making for producers in the agricultural market. By evaluating the effect of data acquisition delay and exploring various prediction algorithms, we can enhance price forecasts' accuracy, enabling producers to navigate risks effectively and optimize their product management strategies. As the agricultural sector evolves, leveraging advanced prediction systems becomes increasingly crucial for sustainable growth and success.


---
[Effects of data time lag in a decision-making system using machine learning for pork price prediction.](https://doi.org/10.1007/s00521-023-08730-7) M.E. SUAZA-MEDINA, F.J. ZARAZAGA-SORIA, J. PINILLA-LÓPEZ, F.J. LOPEZ-PELLICER, J. LACASTA. *Neural Computing and Applications*, Available online, 2023.


---
