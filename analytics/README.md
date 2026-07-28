# Analytics Pipeline

## Overview
This module performs Exploratory Data Analysis (EDA) and Machine Learning on the Titanic dataset.

## Dataset
- Dataset: Titanic Dataset
- Source: Seaborn (`sns.load_dataset("titanic")`)
- Records: 891
- Features: 15

## Tasks Performed

### Exploratory Data Analysis (EDA)
- Data loading and inspection
- Dataset summary
- Missing value analysis and handling
- Histogram
- Boxplot
- IQR outlier detection
- Mean, Median, and Mode
- Survival analysis
- Correlation matrix
- Heatmap
- Feature standardization (Z-score)

### Machine Learning
- Train/Test Split
- Data preprocessing pipeline
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- SMOTE for class balancing
- GridSearchCV for hyperparameter tuning
- Model evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1 Score
  - ROC-AUC
- Linear Regression for Fare Prediction

## Files

- `01_eda.ipynb` – Exploratory Data Analysis
- `02_modeling.ipynb` – Machine Learning models
- `titanic.csv` – Titanic dataset
- `full_pipeline.joblib` – Saved trained machine learning pipeline

## Technologies Used

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn
- Imbalanced-learn
- Joblib

## How to Run

1. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

2. Open the notebooks:
   - `01_eda.ipynb`
   - `02_modeling.ipynb`

3. Run all cells to reproduce the analysis and machine learning results.

## Outcome

The project demonstrates a complete analytics workflow, including data preprocessing, exploratory data analysis, classification, regression, model evaluation, and saving the best-performing machine learning pipeline.