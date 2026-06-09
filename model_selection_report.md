# Model Selection Report: Customer Churn Prediction

## 1. Executive Summary

This project aimed to build a supervised classification model to predict customer churn in a telecommunications company. Two algorithms were compared: **Logistic Regression** and **Random Forest**. The Random Forest classifier emerged as the superior model with an ROC-AUC of 0.862 compared to 0.803 for Logistic Regression.

## 2. Methodology

### 2.1 Data Preprocessing
- **Dataset**: 5,000 customer records with 10 features (tenure, monthly charges, service usage, contract type, etc.)
- **Target Variable**: Binary churn (1 = customer churned, 0 = retained)
- **Class Distribution**: 73% non-churn, 27% churn (moderately imbalanced)
- **Preprocessing Steps**:
  - Train-test split (80-20) with stratification to preserve class distribution
  - Feature standardization using StandardScaler
  - 5-fold stratified cross-validation for robust evaluation

### 2.2 Algorithms Compared

| Algorithm | Parameters | Strengths |
|-----------|------------|------------|
| Logistic Regression | balanced class_weight, max_iter=1000 | Interpretable, fast training, good baseline |
| Random Forest | 100 estimators, balanced class_weight | Handles non-linear relationships, feature importance |

### 2.3 Evaluation Metrics

- **Accuracy**: Overall correctness
- **Precision**: Proportion of correct churn predictions
- **Recall**: Proportion of actual churners detected
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Model's ability to distinguish between classes

## 3. Results

### 3.1 Cross-Validation Performance

| Model | 5-Fold CV ROC-AUC (Mean ± Std) |
|-------|-------------------------------|
| Logistic Regression | 0.795 ± 0.023 |
| Random Forest | 0.851 ± 0.018 |

### 3.2 Test Set Performance

| Metric | Logistic Regression | Random Forest | Winner |
|--------|--------------------|---------------|---------|
| Accuracy | 0.8010 | 0.8490 | **Random Forest** |
| Precision | 0.6240 | 0.6960 | **Random Forest** |
| Recall | 0.7180 | 0.7890 | **Random Forest** |
| F1-Score | 0.6670 | 0.7400 | **Random Forest** |
| ROC-AUC | 0.8030 | 0.8620 | **Random Forest** |

### 3.3 Confusion Matrix Analysis (Random Forest)
