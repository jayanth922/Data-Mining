# Predicting Customer Churn Using SEMMA Methodology

This repository contains the project code for predicting customer churn using the **SEMMA methodology** (Sample, Explore, Modify, Model, and Assess). The project leverages machine learning algorithms such as Logistic Regression, Random Forest, SVM, and XGBoost to build predictive models and compare their performance. The dataset used for this project is the **Telco Customer Churn** dataset from Kaggle.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Visualizations](#visualizations)
- [References](#references)

## Overview
Customer churn prediction is an essential task for subscription-based businesses. By predicting whether a customer is likely to leave, companies can take proactive steps to retain them. In this project, we apply the SEMMA methodology to systematically analyze and build models that can accurately predict customer churn.


## Dataset
We use the **Telco Customer Churn** dataset available on Kaggle, which contains customer data from a telecom company. The dataset includes demographic information, services used by customers, and whether they have churned.

- **Source**: [Kaggle: Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
- **Target Variable**: `Churn` (whether the customer has churned or not)

## Methodology
This project follows the **SEMMA methodology**, which is broken down into the following phases:

1. **Sample**: We randomly sampled 50% of the dataset to manage computational resources.
2. **Explore**: We conducted exploratory data analysis (EDA) to visualize the target variable distribution, correlations between features, and to check for missing values.
3. **Modify**: We handled missing data, encoded categorical variables using one-hot encoding, and scaled numerical features.
4. **Model**: Several machine learning models were trained and evaluated, including Logistic Regression, Random Forest, SVM, and XGBoost.
5. **Assess**: We evaluated models using accuracy, cross-validation scores, and confusion matrices to identify the best-performing model.
