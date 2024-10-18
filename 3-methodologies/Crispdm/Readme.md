# Airbnb Price Prediction Using CRISP-DM

This project uses the **CRISP-DM** (Cross Industry Standard Process for Data Mining) methodology to predict Airbnb rental prices in New York City. By leveraging machine learning techniques such as XGBoost, Random Forest, and Linear Regression, we build a predictive model and deploy it using a Flask API.

## Table of Contents
- [Project Overview](#project-overview)
- [CRISP-DM Methodology](#crisp-dm-methodology)
- [Dataset](#dataset)
- [Technologies and Libraries Used](#technologies-and-libraries-used)
- [Project Structure](#project-structure)
- [Running the Project](#running-the-project)
- [Model Deployment](#model-deployment)
- [Results](#results)
- [References](#references)

## Project Overview

The goal of this project is to accurately predict the price of Airbnb listings based on various features such as location, number of reviews, room type, and more. The project follows the CRISP-DM methodology, which consists of six major phases: business understanding, data understanding, data preparation, modeling, evaluation, and deployment.

The **XGBoost model** was the best-performing model, and the final model was deployed via a Flask API that allows for real-time predictions.

## CRISP-DM Methodology

This project follows the CRISP-DM methodology:

1. **Business Understanding**: Understand the problem of predicting Airbnb prices to help hosts optimize their listings.
2. **Data Understanding**: Exploratory data analysis (EDA) was performed to understand the key factors influencing rental prices.
3. **Data Preparation**: Missing values were handled, features were log-transformed, and categorical variables were one-hot encoded.
4. **Modeling**: Several machine learning models were used, including XGBoost, Random Forest, Gradient Boosting, and Linear Regression.
5. **Evaluation**: Models were evaluated based on Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²).
6. **Deployment**: The final model was deployed via a Flask API for real-time price prediction.

## Dataset

- **Source**: [New York City Airbnb Open Data](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data)
- The dataset contains over 48,000 listings with features such as:
  - `latitude`, `longitude`: Geolocation of the listing.
  - `minimum_nights`: Minimum nights required for booking.
  - `price`: Price of the listing (target variable).
  - `number_of_reviews`: Number of reviews for the listing.
  - `neighbourhood_group`, `room_type`: Categorical features indicating location and type of accommodation.

## Technologies and Libraries Used

- **Python 3.8+**
- **Flask** for deployment
- **Pandas** for data manipulation
- **Seaborn** and **Matplotlib** for data visualization
- **Scikit-learn** for model training
- **XGBoost** for model optimization
- **Joblib** for model serialization
- **Jupyter Notebook** / **Colab** for exploratory analysis

## Project Structure

