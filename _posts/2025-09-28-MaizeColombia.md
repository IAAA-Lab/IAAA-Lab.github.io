---
title: Multivariate integration of time series with ML for corn price forecasting in Colombia
subtitle:
layout: post
image: /images/posts/2025-09-28-Fig1.jpg
categories: [Paper overview]
---


The volatility of corn prices poses a significant challenge for both producers and policymakers. This study proposes a hybrid model that combines Extreme Gradient Boosting (XGBoost) and Light Gradient Boosting Machine (LightGBM), optimized through Particle Swarm Optimization with Cuckoo Search (PSO-CS), for accurate corn price forecasting. 

![Figure 1: Proposed methodological framework for corn price forecasting The process is divided into three phases: (1) prediction based on a univariate time series, (2) multivariate data integration, and (3) model validation]({{ site.baseurl }}/images/posts/2025-09-28-Fig1.jpg){: .center-image width="60%"}
<h4><center><b>Figure 1: Proposed methodological framework for corn price forecasting The process is divided into three phases: (1) prediction based on a univariate time series, (2) multivariate data integration, and (3) model validation</b></center></h4>

The approach integrates multivariate time series data, including local prices from the Atlántico market and international futures prices from the Chicago Board of Trade (CBOT). Empirical Mode Decomposition (EMD) is applied to enhance signal clarity and improve model performance.

![Figure 2: Architecture for forecasting corn prices in Colombia using multivariate time series and ensemble learning models. The figure illustrates the three-phase methodology: (1) univariate prediction using EMD and ML models, (2) integration of CBOT corn futures data to create a multivariate model, and (3) Ensemble predictions are optimized through a PSO-CS metaheuristic to enhance accuracy and robustness]({{ site.baseurl }}/images/posts/2025-09-28-Fig2.jpg){: .center-image width="60%"}
<h4><center><b>Figure 2: Architecture for forecasting corn prices in Colombia using multivariate time series and ensemble learning models. The figure illustrates the three-phase methodology: (1) univariate prediction using EMD and ML models, (2) integration of CBOT corn futures data to create a multivariate model, and (3) Ensemble predictions are optimized through a PSO-CS metaheuristic to enhance accuracy and robustness</b></center></h4>

Model performance is assessed through sensitivity analysis and statistical comparison using the Diebold-Mariano (DM) test. The results demonstrate that the proposed ensemble outperforms both individual models and neural network combinations, achieving a Mean Absolute Percentage Error (MAPE) of 2.06

This work includes the results of [Adelaida Ojeda’s internship at the IAAA.](https://iaaa.es/2024/10/03/Adelaida-internship/)


---
[Multivariate integration of time series with ML for corn price forecasting in Colombia.](https://doi.org/10.1016/j.eswa.2025.129822)  A. OJEDA-BELTRAN, M.E. SUAZA-MEDINA, F.J. ZARAZAGA-SORIA, E. DE-LA-HOZ-FRANCO, J. ESCORCIA-GUTIERREZ. Expert Systems with Applications, Available online 27 September 2025, 129822, 2025. 


---
