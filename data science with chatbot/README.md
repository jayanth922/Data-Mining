# **<center>Water Quality Prediction: A Data Science Project Using CRISP-DM</center>**

---

## **Project Overview**
This project aims to use **ChatGPT** to create a data science project for **water quality prediction** using the **CRISP-DM Methodology**.

---

## **Objective**
The primary goal of this project is to create a predictive model that determines if water is suitable for consumption. This involves analyzing different chemical and physical characteristics of water and using machine learning to classify each sample as **potable (1)** or **not potable (0)**.

---

## **CRISP-DM Methodology**
The project follows the **CRISP-DM (Cross-Industry Standard Process for Data Mining)** methodology, which includes:

1. **Business Understanding**: 
   - Defining the objective of predicting water quality to enhance public health.

2. **Data Understanding**: 
   - Exploring the dataset, including features such as **pH**, **hardness**, **total dissolved solids**, and others.

3. **Data Preparation**: 
   - Handling missing values, anomalies, and standardizing the dataset for model training.

4. **Modeling**: 
   - Building and evaluating different machine learning models, including **RandomForest**, **Logistic Regression**, and **Decision Tree**.

5. **Evaluation**: 
   - Assessing model performance using **accuracy**, **precision**, **recall**, and **F1 score**.

6. **Deployment**: 
   - Preparing the model for real-world use through testing and evaluation.

---

## **Dataset Description**
The dataset contains **3276** water samples, each with a set of features that represent different quality metrics:

- **pH**: Indicates the acidity or basicity of water.
- **Hardness**: Represents the concentration of calcium and magnesium.
- **Total Dissolved Solids (TDS)**: Indicates the amount of dissolved minerals.
- **Chloramines**, **Sulfate**, **Conductivity**, **Organic Carbon**, **Trihalomethanes**, and **Turbidity** are other features that help determine water quality.

The target variable is **Potability**, which indicates whether the water is suitable for drinking.

---

## **Key Phases of the Project**

### 1. **Data Cleaning and Preprocessing**
- **Handled missing values** using the median to ensure data robustness.
- **Standardized features** to ensure consistency across all metrics.

### 2. **Exploratory Data Analysis (EDA)**
- **Visualized feature distributions** and correlations to understand the dataset.
- Determined that **Solids**, **Organic Carbon**, and **Chloramines** were among the most influential features for potability.

### 3. **Modeling**
- Built and compared multiple machine learning models:
  - **RandomForest Classifier** emerged as the best model with an accuracy of **70.12%**.
  - **Logistic Regression** and **Decision Tree** were also tested but did not perform as well.

### 4. **Evaluation and Results**
- The **RandomForest Classifier** was selected as the best-performing model based on its balanced **accuracy**, **precision**, **recall**, and **F1 score**.
- Final evaluation metrics showed the effectiveness of the model in predicting **non-potable water** with potential areas for improving recall for **potable samples**.

### 5. **Sample Prediction**
- The model was used to predict the potability of a randomly selected sample, providing **practical insights** into its use in real-world scenarios.

---

## **Key Findings**
- Features like **Solids**, **Organic Carbon**, and **Chloramines** play a critical role in predicting water quality.
- The **RandomForest Classifier** provided the best balance between accuracy and recall, making it suitable for predicting water potability.

---

## **Links for Reference**
- **ChatGPT Session**: [Link to ChatGPT Session](https://chatgpt.com/share/67031bff-d34c-8002-accb-66a3025ec991)
- **Colab Notebook**: [Link to Colab Notebook](https://colab.research.google.com/drive/1RP86rwng926gFgsRl28fAaqzYahsYkby?usp=sharing)
- **Medium Article**: [Link to Medium Article](https://medium.com/@jayanth.kalyanam/predicting-water-quality-a-data-science-journey-using-crisp-dm-b164c05c2260)

---
