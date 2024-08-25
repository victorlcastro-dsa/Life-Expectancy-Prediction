# 🧬 Data Analysis and AI Model Project for Life Expectancy 
**`Completed`**

## Part 1: Data Analysis ([EDA](https://github.com/victorlcastro-dsa/LifeExpectancy/blob/main/notebook/EDA.ipynb))

### 🎯 Objectives

The objective of this project is to answer five valuable business questions related to life expectancy. Subsequently, the project will be extended to create an AI model that can predict life expectancy based on the provided data.

### 📊 Business Questions

1. What are the main factors that influence life expectancy in different countries?
2. How has life expectancy changed over time in countries with different socioeconomic statuses?
3. What is the relationship between healthcare expenditure and life expectancy?
4. Is there a correlation between immunization coverage (Hepatitis B, Polio, Diphtheria) and life expectancy?
5. How does alcohol consumption affect life expectancy in different regions?

### 🔍 Data Analysis Steps

#### 1. Data Import and Preprocessing

- Import data from CSV.
- Clean data (handling missing values, duplicate data, etc.).

#### 2. Exploratory Data Analysis (EDA)

- Descriptive statistics.
- Data visualization to identify patterns and trends.
- Correlation analysis between variables.

#### 3. Specific Analysis to Answer Questions

- Use Python techniques to identify factors influencing life expectancy.
- Perform temporal analysis to observe changes in life expectancy over the years.
- Conduct correlation analysis to investigate the relationship between healthcare expenditure and life expectancy.
- Analyze the correlation between immunizations and life expectancy.
- Perform regional analysis on the impact of alcohol consumption on life expectancy.

#### 4. Exporting the updated dataset

- Export the file in `.csv` for use in: [Model Training Notebook](https://github.com/victorlcastro-dsa/LifeExpectancy/blob/main/notebook/MODEL%20TRAINING.ipynb)

### 🛠️ Tools Used

- Python

Libraries:
1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn
5. Scipy
6. Statsmodels
7. Scikit-learn
8. Requests
9. Xgboost
10. Shap
11. Graphviz
12. Joblib

## Part 2: Project Extension - [AI Model](https://github.com/victorlcastro-dsa/LifeExpectancy/blob/main/notebook/MODEL%20TRAINING.ipynb)

### 🎯 Objective

Develop a predictive model to estimate life expectancy based on the provided data.

### 🧠 AI Model Development Steps

#### 1. Data Preparation

- Select relevant features.
- Normalize and transform data.
- Split data into training and testing sets.

#### 2. Model Construction

- Test various algorithms (Linear Regression, Random Forest, Gradient Boosting, etc.).
- Evaluate model performance using appropriate metrics (MAE, RMSE, R²).
- Select the best performing model.

#### 3. Model Validation and Tuning

- Cross-validation.
- Hyperparameter tuning using GridSearchCV or RandomizedSearchCV.

#### 4. Model Implementation

- Train the final model with the best parameters.
- Save the trained model for future use.

### 🛠️ Tools Used

- Python
- Libraries: Pandas, NumPy, Scikit-learn, XGBoost, Joblib

The foundational structure and initial version of the model are complete, providing a solid base for the project. Future updates will focus on **refining** and **optimizing** the code to align with industry standards and enhance overall performance.
