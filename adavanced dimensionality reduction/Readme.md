# Dimensionality Reduction Project

## Overview
This project explores and compares various dimensionality reduction techniques on both image and tabular datasets. The implementation was carried out in two environments:
- Google Colab
- Databricks

The goal was to evaluate the methods in terms of visualization, structure preservation, and computational efficiency.

## Techniques Implemented
- **Principal Component Analysis (PCA)**
- **Kernel PCA**
- **Incremental PCA**
- **t-SNE**
- **UMAP**
- **Isomap**
- **Locally Linear Embedding (LLE)**
- **Factor Analysis**
- **Autoencoders**

## Datasets Used
1. **Fashion MNIST (Image Data)**: A subset of grayscale images representing fashion items.
2. **California Housing (Tabular Data)**: A dataset used for Task 2 in Databricks.


# Link for Colab Notebook : https://colab.research.google.com/drive/1Qhm7C6taDGxxbpI7HBtch87EPsgr50Wn?usp=sharing
# Link for Youtube Demo : https://youtu.be/Wfn3ZXeimRo

## Results and Observations
### Task 1 (Colab)
- **Best Techniques**: t-SNE and UMAP excelled in clustering and visualizing non-linear relationships.
- **Other Observations**:
  - PCA and Incremental PCA effectively captured linear variance but failed with non-linear patterns.
  - Autoencoders showed potential but required tuning.

### Task 2 (Databricks)
- **Best Techniques**: Similar to Task 1, t-SNE and UMAP provided the best cluster separations.
- **Other Observations**:
  - Kernel PCA and Autoencoders performed suboptimally without parameter adjustments.

## Key Learnings
- Dimensionality reduction is highly dataset-dependent, and tuning parameters is crucial for non-linear methods.
- UMAP and t-SNE consistently outperform others for non-linear datasets.
- Incremental PCA is ideal for large datasets processed in memory-constrained environments.

## Conclusion
This project highlights the strengths of UMAP and t-SNE for non-linear data and the reliability of PAC for linear structures. By leveraging both Colab and Databricks, we demonstrate the versatility and scalability of these methods.
