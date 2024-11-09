# Bike Sharing Prediction Pipeline with Apache Beam

This project demonstrates an **Apache Beam** pipeline that predicts daily bike rentals based on weather-related features using a **Linear Regression** model. The pipeline processes the UCI Bike Sharing dataset, trains a predictive model, and then performs batch inference on the data. The predictions are finally uploaded to **Amazon S3**.

## Project Overview

The project consists of the following key steps:

1. **Dataset Loading and Cleaning**: 
   - Download the **UCI Bike Sharing dataset** and clean it by selecting relevant columns.
   - The cleaned data is saved as `cleaned_bike_data.csv`.

2. **Model Training**:
   - A **Linear Regression model** is trained using `scikit-learn` to predict the total number of bike rentals (`cnt`) based on features such as temperature, humidity, and windspeed.
   - The trained model is saved as `bike_model.pkl` for use in the Apache Beam pipeline.

3. **Apache Beam Pipeline**:
   - The pipeline reads the cleaned dataset, preprocesses it, performs batch inference using the saved model, and uploads the predictions to an Amazon S3 bucket.

## Project Structure

- **Dataset**: The UCI Bike Sharing dataset (`day.csv`), which contains daily bike rental information with weather attributes.
- **Model Training**: A Linear Regression model trained on the dataset, saved as `bike_model.pkl`.
- **Apache Beam Pipeline**:
  - **Data Preprocessing**: Encapsulated in a composite transform, converts CSV rows into NumPy arrays for model inference.
  - **Run Inference**: Uses BeamML’s `RunInference` to apply the saved model for predictions.
  - **Upload to S3**: Final predictions are saved and uploaded to an Amazon S3 bucket.
 

Here is the link for colab notebook : https://colab.research.google.com/drive/1xgTzhqnPhSmjVfc_CRRd7NXKzlhlHp23?usp=sharing

Here is the link for youtube video : https://youtu.be/6LNMtRUOb6I

