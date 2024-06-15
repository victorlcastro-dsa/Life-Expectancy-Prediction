# 🧬 Data Analysis and AI Model Project for Life Expectancy 
**`Under development`**

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

- Export the file in `.csv` for use in: [Model Training Notebook](https://github.com/victorlcastro-dsa/LifeExpectancy/blob/1892efa8069ea78b1a3a1be18794d23961437945/notebook/MODEL%20TRAINING.ipynb)

### 🛠️ Tools Used

- Python

Libraries:
1. Pandas
2. Matplotlib
3. Seaborn
4. Scikit-Learn
5. Scipy
6. Statsmodels
7. Requests
8. Functools
9. Concurrent.Futures
10. OS

## Part 2: Project Extension - [AI Model](https://github.com/victorlcastro-dsa/LifeExpectancy/blob/1892efa8069ea78b1a3a1be18794d23961437945/notebook/)

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

## Part 3: Web Implementation

### 🎯 Objective

Integrate the predictive model into a web application where users can input data and obtain life expectancy predictions.

`More information will be added throughout the development of the project`
