# Air Quality Forecasting in India (Time Series Analysis)

This project aims to forecast daily **PM2.5** levels in a specific city in India using historical air quality data. Using **time series analysis**, **clustering**, **anomaly detection**, and **AutoML** techniques, we analyze and predict air quality trends, helping to identify seasonal patterns and critical pollution events.


## Project Structure

### 1. Library Compatibility Setup
   - Install specific versions of `scipy`, `Auto_ViML`, `pandas-profiling`, and `numba` to ensure compatibility across all analysis and modeling stages.

### 2. Data Loading and Initial Inspection
   - Load the `city_day.csv` dataset from the **Air Quality Data in India** dataset.
   - Display initial information about the dataset, including columns, data types, and a sample of rows.

### 3. Automated EDA with YData Profiling
   - Generate an in-depth profiling report to quickly understand data distributions, correlations, and missing values.

### 4. Manual EDA: PM2.5 Trend Analysis for a Specific City
   - Filter the dataset for a specific city (e.g., Delhi), convert `Date` to datetime format, and visualize PM2.5 levels over time to identify trends and seasonal patterns.

### 5. Data Cleaning and Preprocessing
   - Filter for relevant columns and handle missing values by applying forward filling to maintain time series continuity.

### 6. Feature Engineering
   - **Temporal Features**: Extract year, month, day of the week, and day of the year.
   - **Lagged and Rolling Features**: Create lagged and rolling mean features to incorporate historical data dependencies.

### 7. Clustering with K-Means for Pattern Detection
   - Apply K-Means clustering on pollutant levels to identify distinct patterns in air quality data, helping reveal clusters in PM2.5 trends.

### 8. Anomaly Detection with Isolation Forest
   - Use Isolation Forest to detect anomalies in PM2.5 levels and identify unusual pollutant spikes, visualizing these anomalies to support trend analysis.

### 9. Train-Test Split (Chronological)
   - Perform a chronological split (80% train, 20% test) to maintain temporal integrity for time series forecasting.

### 10. Forecasting Model with AutoML (Auto_ViML)
   - Use Auto_ViML for automated model building, feature selection, and tuning, optimizing the model to forecast PM2.5 levels.


Here is the link for youtube : https://youtu.be/lgjS2mqYLRI

Here is the link for colab : https://colab.research.google.com/drive/17bPjhqJuBbcMympdtQ2hoKL_OrE96ufR?usp=sharing
