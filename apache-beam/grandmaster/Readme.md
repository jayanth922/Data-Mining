# Wine Quality Analysis with Interactive D3.js Visualizations

This repository contains a comprehensive exploratory data analysis (EDA) of the **Wine Quality** dataset using advanced interactive visualizations created with **D3.js**. The project aims to uncover factors that influence wine quality.


## Introduction

Wine quality is a complex attribute influenced by various physicochemical properties. Understanding these factors can help in wine production, quality control, and consumer preference analysis. This project performs an in-depth EDA of the Wine Quality dataset, employing interactive D3.js visualizations to enhance data exploration and insights.

## Dataset

The Wine Quality dataset consists of red and white variants of the Portuguese "Vinho Verde" wine. It includes 11 physicochemical properties and a quality score between 0 and 10. The dataset is publicly available at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/wine+quality).

## Project Overview

The project involves the following key steps:

1. **Data Loading and Preprocessing**
   - Loaded red and white wine datasets.
   - Combined datasets and added a `type` column to distinguish wine types.
   - Checked for missing values and ensured proper data types.
   - Renamed columns for clarity.

2. **Exploratory Data Analysis**
   - Generated descriptive statistics.
   - Analyzed distributions of wine quality and alcohol content.
   - Explored relationships between features and wine quality.

3. **Correlation Analysis**
   - Computed the correlation matrix excluding non-numeric columns.
   - Identified features with strong positive or negative correlations to quality.

4. **Advanced Visualizations with D3.js**
   - Created interactive histograms, scatter plots, and heatmaps.
   - Visualizations allow dynamic data exploration within Google Colab.

5. **Feature Engineering**
   - Categorized wine quality into 'Low', 'Medium', and 'High' labels.

6. **Clustering Analysis**
   - Standardized features and applied KMeans clustering.
   - Determined the optimal number of clusters using the silhouette score.
   - Visualized clusters using PCA and interactive scatter plots.

7. **Conclusions**
   - Summarized key findings regarding factors affecting wine quality.
  

Here is the link for colab notebook : https://colab.research.google.com/drive/18t7aN9cwEKAmjZdTVb2E3UH6rNo1Ugvv?usp=sharing

Link for youtube video : https://youtu.be/KYaQOkJpJDw
