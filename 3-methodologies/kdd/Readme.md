Wine Quality Prediction using Machine Learning and KDD Methodology
This repository contains a project aimed at predicting wine quality using machine learning techniques, following the Knowledge Discovery in Databases (KDD) methodology. The model is trained on a dataset of red wine samples from the UCI Machine Learning Repository. We explore various models, including Logistic Regression, Random Forest, Support Vector Machines, and more, ultimately optimizing a Random Forest model to predict wine quality.

Project Overview
Wine quality is traditionally evaluated by experts through sensory analysis, which is often subjective. This project leverages machine learning techniques to predict wine quality based on measurable physicochemical properties, providing an efficient and systematic approach to wine quality evaluation.

We utilize the KDD Methodology, which includes:

Data Selection: Selecting the appropriate dataset for analysis.
Data Preprocessing: Cleaning and preparing the data for analysis.
Data Transformation: Engineering new features for better prediction.
Data Mining: Training machine learning models to predict wine quality.
Pattern Evaluation: Evaluating the performance of the models using various metrics.
Knowledge Representation: Interpreting and visualizing results.


Dataset:

The dataset used for this project can be found on the UCI Machine Learning Repository. It contains 1,599 red wine samples with 11 physicochemical properties:

Fixed Acidity
Volatile Acidity
Citric Acid
Residual Sugar
Chlorides
Free Sulfur Dioxide
Total Sulfur Dioxide
Density
pH
Sulphates
Alcohol

The target variable is Wine Quality, which has been transformed into a binary classification problem:

Good Quality (Score $\geq 6$)
Bad Quality (Score $<$ 6)
