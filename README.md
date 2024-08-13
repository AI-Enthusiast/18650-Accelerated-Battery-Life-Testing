# [18650 Battery Accelerated Life Testing Survival Analysis vs Machine Learning](https://github.com/AI-Enthusiast/18650-Accelerated-Battery-Life-Testing/blob/main/slides/Machine%20Learning%20Final%20Presentation%20-%20Aryan%2C%20Avery%2C%20Cormac%2C%20Tyler.pdf)
#### Aryan Bhardwaj, Cormac Dacker, Avery Pike, Tyler Gomez Riddick

## Introduction

In this project, we explore the life cycle of 26 battery packs, each consisting of two 18650 rechargeable lithium-ion
batteries. These batteries are integral to various applications, including electric vehicles, portable electronics, and
renewable energy storage systems. Their reliability and longevity are crucial for manufacturers, energy managers, and
tech developers who depend on these batteries to ensure the optimal performance, safety, and cost-effectiveness of their
products.

Predicting battery life accurately is essential for different stakeholders. For instance, automotive engineers and fleet
managers in the electric vehicle industry need precise battery life forecasts to improve maintenance schedules, vehicle
reliability, and customer satisfaction. Energy storage companies, particularly those involved in renewable energy,
require accurate predictions to optimize energy management, reduce downtime, and enhance sustainability. Similarly,
manufacturers of portable electronics can benefit from better battery life predictions to improve product durability and
customer trust.

This project compares survival analysis techniques with machine learning models to predict battery life, focusing on the
discharge phases that are key to understanding battery degradation. Survival analysis offers a statistically robust
method for modeling time-to-failure data, providing insights into how different factors influence battery longevity.
Meanwhile, machine learning models may have the potential to deliver more accurate predictions, making them valuable for
dynamic and intricate applications. Using a NASA produced dataset this project aims to compare the strengths and
weaknesses of these methods.1

## Methodology

### The Data

The dataset comprises millions of rows, with each row capturing a second-by-second record of one battery pack’s
parameters during charging, rest, and discharging phases. Each CSV in the dataset is an individual battery. Given the
large volume of data, we focused on the discharge phases, as they provide critical insights into battery degradation.

### Data Preprocessing

To streamline the analysis, we first combined the CSV files for regular, second life, and recommissioned batteries into
single datasets for each group. We then extracted key features—average voltage, temperature, and current—for each
discharge phase, reducing the data to one row per discharge cycle.

### Survival Analysis

We performed survival analysis using Weibull regression in R. Weibull regression is well-suited for modeling failure
times and provides insights into how different factors influence battery life.
We used the fitdistrplus and survival packages to fit a Weibull model to the data, focusing on parameters such as
current load, voltage, and temperature. The model provided significant insights, with a high R-squared value indicating
a strong fit.
The equation (below) provided represents a Weibull regression model for predicting the time-to-failure (TTF) of a system
based on various covariances:

**TTF**~**Weibull**(*M* = *b*<sub>0</sub> + *b*<sub>1</sub> Temp<sup>~</sup> + *b*<sub>2</sub>  Volt<sup>~</sup> +
*b*<sub>3</sub>Current + *b*<sub>4</sub>Temp × Volt × Current + Type, *σ* = 1/*B*)

1. Weibull Distribution: Commonly used in reliability analysis, the Weibull distribution is defined by a shape parameter
   k and a scale parameter sigma. Here, sigma = 1/B, meaning B inversely affects the scale of the distribution.
2. Linear Predictor (M):

- M is a linear combination of covariates: Arrhenius temp, log voltage, current, and their interaction (in our actual
  models, our interaction term included only Arrhenius temperature and log voltage)
- b1, b2, b3 are coefficients for Arrhenius temp, log voltage, and current, respectively, while b4 captures the
  interaction between these factors.

3. Covariate Transformations:

- Temperature: Transformed as **Temp**<sup>~</sup> = 11605/(**Temp Celsius** + 273.15) to reflect its inverse
  relationship with failure. This is the Arrhenius equation for temperature degradation.
- Voltage: Log-transformed as **Volt**<sup>~</sup> = *log*(**Voltage**) to linearize its effect on TTF.

This model estimates TTF based on environmental and operational factors. The linear predictor M shifts the TTF
distribution, while sigma influences its spread. The interaction term captures the combined effect of temperature,
voltage, and current, critical in reliability studies. This allows for assessing how different factors contribute to the
system's likelihood of failure.

### Machine Learning

To compare with survival analysis, we implemented three machine learning models: linear regression, random forest, and
neural networks. (Visuals of the models and their respective metrics can be seen in the Jupyter Notebook)

#### Linear Regression

We used linear regression as a baseline model. While it provided decent predictions, the model's simplicity limited its
effectiveness in capturing complex relationships in the data.

#### Random Forest

This model offered a more nuanced approach, capturing interactions between variables that linear regression could not.
Random forest showed excellent performance metrics improving on the linear regression model making it a more robust
choice for this dataset.

#### Neural Network

Finally, we implemented a neural network model using TensorFlow. This model, with its ability to capture non-linear
relationships, provided the best performance among the three, albeit at the cost of increased complexity and
computational resources.

## Hypotheses

Survival analysis will predict the time to full discharge best out of all of the models.

## Evaluation

We compared the models using three key metrics: Mean Squared Error (MSE), Akaike Information Criterion (AIC), and
R-squared (R²). MSE quantifies the average squared difference between observed and predicted values, with a lower MSE
indicating more accurate predictions. AIC balances model fit and complexity, where a lower AIC value suggests a more
efficient model. R-squared measures the proportion of variance explained by the model, with a higher R² indicating a
better fit. These metrics collectively help us assess and compare the performance of different models, guiding us toward
the most accurate and parsimonious choice.

### Results

Our results can be found on our slides, submitted as part of this assignment. Additionally, visualizations can be found
in our [Jupyter notebook](https://github.com/AI-Enthusiast/18650-Accelerated-Battery-Life-Testing/blob/main/ML_WriteUp.ipynb)
and [R-markdown](https://github.com/AI-Enthusiast/18650-Accelerated-Battery-Life-Testing/blob/main/WeibullRegression.rmd)
files. Ultimately, we found that the random forest model was most predictive, and
the Weibull regression and linear regression models were the least predictive.

## Conclusions and Future Research

The comparison between survival analysis and machine learning models highlights the strengths and weaknesses of each
approach. Survival analysis, with its interpretability and established statistical foundation, provides valuable
insights into battery degradation. However, machine learning models, especially neural networks, offer superior
predictive power with the given dataset.

This study demonstrates the utility of combining traditional statistical methods with modern machine learning techniques
to enhance predictive accuracy and deepen our understanding of battery life.

Future research could explore more advanced machine learning models, such as gradient boosting and deep learning, to
further improve predictive performance. Additionally, incorporating more features, such as battery chemistry, cycle
count, and charging patterns, could enhance the models’ accuracy and robustness. Finally, investigating the impact of
battery degradation on energy storage systems and electric vehicles could provide valuable insights for the renewable
energy and automotive industries.

## References

### [Dataset](https://ntrs.nasa.gov/citations/20230014884)
