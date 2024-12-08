# Gradient Boosting and Ensemble Learning Notebooks

This repository contains a collection of Jupyter Notebooks that implement and demonstrate various machine learning algorithms, focusing on **Gradient Boosting** and **Ensemble Learning** techniques. Each notebook is designed to provide a step-by-step explanation and practical implementation of the respective algorithms.

---

## Table of Content

1. [GBM from Scratch](#gbm-from-scratch)
Youtube Demo : https://youtu.be/9LSNIjAIjrU
Colab Link : https://colab.research.google.com/drive/1leOf9XE0jKwtfqYZrC3fVQNDL6Io8AqF?usp=sharing

2. [Random Forest from Scratch](#random-forest-from-scratch)
Youtube Demo : https://youtu.be/AnNobt6wvQQ
Colab Link : https://colab.research.google.com/drive/18wHlOFpHCADcoJgO-tFRGtqJ_47Nm-Yv?usp=sharing

3. [AdaBoost from Scratch](#adaboost-from-scratch)
Youtube Demo : https://youtu.be/KvTylGBjQSs
Colab Link : https://colab.research.google.com/drive/19UticaGAOQZqmbDf-XRUNCv-k2DGzMzh?usp=sharing

4. [Decision Tree from Scratch](#decision-tree-from-scratch)
Youtube Demo : https://youtu.be/RZe4i0bZ7cE
Colab Link : https://colab.research.google.com/drive/1r-Va20vuA3vad4ooALp8FfigrEds-Mls?usp=sharing

5. [GBM Classifiers Demonstration](#gbm-classifiers-demonstration)
Youtube Demo : https://youtu.be/iS2AZXuxzzk
Colab Link : https://colab.research.google.com/drive/17Et-3qwkyCMC9OxfjXAvEeW79UvRoyE8?usp=sharing


6. [GBM Regression Demonstration](#gbm-regression-demonstration)
Youtube Demo : https://youtu.be/QBBC8jFnEm0
Colab Link : https://colab.research.google.com/drive/1z7Kdbr2_TkXFEuAoJebZMpCFX0obvj1J?usp=sharing

7. [GBM Ranking Demonstration](#gbm-ranking-demonstration)
Youtube Demo : https://youtu.be/FiMZ1jDZmuI
Colab Link : https://colab.research.google.com/drive/1eCJghjEFk83UdNgIj7Z2QAzFPw3m08yz?usp=sharing

---

## 1. GBM from Scratch

This notebook implements the Gradient Boosting Machine (GBM) algorithm from scratch. It builds sequential decision trees, minimizing residual errors iteratively.

- **Dataset**: Synthetic sine wave data.
- **Evaluation**: Mean Squared Error (MSE) and visualization of predictions.
- **Key Features**:
  - Custom GBM class implementation.
  - Training and testing using synthetic data.

---

## 2. Random Forest from Scratch

A custom implementation of the Random Forest algorithm. The notebook combines multiple decision trees trained on bootstrap samples.

- **Dataset**: Iris dataset.
- **Evaluation**: Accuracy score.
- **Key Features**:
  - Custom Decision Tree class.
  - Ensemble learning using bagging.

---

## 3. AdaBoost from Scratch

This notebook demonstrates the AdaBoost algorithm, combining weak learners (decision stumps) to build a strong classifier.

- **Dataset**: Binary-class Iris dataset.
- **Evaluation**: Accuracy score.
- **Key Features**:
  - Dynamic sample weighting.
  - Iterative model improvement.

---

## 4. Decision Tree from Scratch

A Decision Tree classifier built from the ground up, splitting features to minimize impurity.

- **Dataset**: Iris dataset.
- **Evaluation**: Accuracy score.
- **Key Features**:
  - Custom implementation of Gini Index and Entropy.
  - Recursive tree-building.

---

## 5. GBM Classifiers Demonstration

This notebook compares popular classifiers such as XGBoost, CatBoost, LightGBM, Random Forest, AdaBoost, and Decision Tree.

- **Dataset**: Iris dataset.
- **Evaluation**: Accuracy scores for all models.
- **Key Features**:
  - Side-by-side comparison of gradient boosting and ensemble classifiers.

---

## 6. GBM Regression Demonstration

Gradient Boosting Regressors, including XGBoost, CatBoost, and LightGBM, are demonstrated using regression tasks.

- **Dataset**: Diabetes dataset.
- **Evaluation**: Mean Squared Error (MSE).
- **Key Features**:
  - Simple setup for regression tasks.
  - Comparison of three boosting methods.

---

## 7. GBM Ranking Demonstration

This notebook demonstrates ranking algorithms using XGBoost, CatBoost, and LightGBM. Proper group handling is included for ranking tasks.

- **Dataset**: Synthetic dataset with query-based group structures.
- **Evaluation**: Mean Squared Error (MSE).
- **Key Features**:
  - Accurate group handling for ranking tasks.
  - Insights into ranking-specific model behavior.

---
