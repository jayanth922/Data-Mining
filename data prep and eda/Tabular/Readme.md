# Airbnb NYC Tabular Analysis and Prediction

This project focuses on analyzing and predicting Airbnb listing prices in New York City using a tabular dataset. The analysis includes **exploratory data analysis (EDA)**, **feature engineering**, **clustering**, **anomaly detection**, and **automated machine learning (AutoML)** with **Auto_ViML**.


## Project Structure

### 1. **Data Loading and Initial Inspection**
   - Load the Airbnb NYC dataset and inspect columns, data types, and the first few rows to understand the data.

### 2. **Automated EDA with YData Profiling**
   - Generate a profiling report to understand data distributions, correlations, and missing values quickly.

### 3. **Manual EDA: Price Distribution and Room Type Analysis**
   - Plot price distribution to identify outliers.
   - Analyze room type distributions by neighborhood group to detect popular listings by location and room type.

### 4. **Data Cleaning and Preprocessing**
   - Handle missing values by imputing or dropping where necessary.
   - Encode categorical variables like neighborhood and room type.
   - Scale numerical features to prepare for model training.

### 5. **Feature Engineering**
   - Create a `days_since_last_review` feature from the last review date.
   - Drop unnecessary columns to streamline the dataset.

### 6. **Clustering and Anomaly Detection**
   - **K-Means Clustering**: Cluster listings based on latitude and longitude to analyze geographical patterns.
   - **Anomaly Detection**: Use Isolation Forest to identify anomalies in listings based on price, minimum nights, and reviews.

### 7. **Predictive Modeling with AutoML (Auto_ViML)**
   - Use Auto_ViML to automate model building for predicting Airbnb prices, including feature selection and hyperparameter tuning.

Here is the link to youtube : https://youtu.be/NYrwIz87C_k

Here is the link to colab : https://colab.research.google.com/drive/1tAM_0nyQOrrp8LaRqJqDCp7AoM-f_qTi?usp=sharing
