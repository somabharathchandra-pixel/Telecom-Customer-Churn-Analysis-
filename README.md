# Customer Churn Analysis & Prediction

## Project Overview

This project analyzes telecom customer churn using Python, exploratory data analysis, and machine learning classification models. The analysis focuses on identifying customer and service characteristics associated with churn and evaluating models for churn prediction.

## Dataset

The project uses the Telco Customer Churn dataset. The data contains customer demographics, tenure, services, contract details, payment information, monthly charges, total charges, and churn status.

## Analysis Performed

- Data cleaning and preprocessing
- Handling and converting `TotalCharges`
- Standardization of categorical service fields
- Exploratory analysis of churn patterns
- Analysis by tenure, monthly charges, contract type, payment method, internet service, support, and other customer attributes
- Customer segmentation by tenure and monthly-charge groups
- Churn-rate visualizations

## Machine Learning

The project includes classification models for churn prediction:

- Logistic Regression
- Decision Tree
- Random Forest

The models use an 80/20 train-test split and encoded categorical features. Model evaluation includes accuracy, confusion matrix, precision, recall, and F1-score.

## Key Results

Based on the project analysis:

- Overall churn rate: **26.54%**
- Logistic Regression model accuracy: **82%**
- Precision: **40%**
- Recall: **78%**
- F1-score: **60%**
- Month-to-month customers showed substantially higher churn than customers on one-year or two-year contracts.

## Repository Structure

```text
Customer-Churn-Analysis-Prediction/
│
├── README.md
├── data/
│   ├── raw/
│   │   ├── Telco_Customer_Churn_Dataset.csv
│   │   └── Telco_Customer_Churn_Dataset.xlsx
│   └── processed/
│       ├── cleaned_churn_data.csv
│       └── cleaned_Churn_prediction.csv
│
├── python/
│   ├── Chrun_prediction_Model.py
│   ├── churn_decesion_tree.py
│   ├── Churn_random_forest.py
│   └── churn_predict.py
│
├── powerbi/
│   ├── churn_Analysis_new.pbix
│   └── previous_versions/
│       ├── chur.pbix
│       └── churn_prediction.pbix
│
└── visualizations/
    ├── churn analysis charts
    └── Power BI dashboard image
```

## Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Power BI
- Jupyter/Python analysis workflow

## Disclaimer

This repository is a portfolio project based on the Telco Customer Churn dataset. It is intended for learning and demonstration of data analysis and machine learning skills.
