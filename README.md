# Codtech-Task-1-ETL  
- COMPANY: CODTECH IT SOLUTIONS  
- NAME: BHUKYA JANI  
- INTERN ID: CT04DH2696  
- DOMAIN: DATA SCIENCE  
- DURATION: 4 WEEKS  
- MENTOR: NEELA SANTOSH  

---

### ✅ TASK 1: ETL Pipeline – Iris Dataset

#### 📌 Overview  
This project performs a complete ETL (Extract, Transform, Load) process on the Iris dataset using Python libraries — Pandas and Scikit-learn.  
The cleaned data is exported to a CSV file and can be used for further machine learning tasks.

---

### ⚙️ Technologies Used  
- Python  
- Pandas  
- Scikit-learn  

---

### 🧠 ETL Process

#### 🔹 Extract  
- The Iris dataset is loaded using `sklearn.datasets.load_iris()`  
- It includes features like sepal length, petal length, etc., and a target species label  

#### 🔹 Transform  
- Encoding the categorical label `species` using `LabelEncoder`  
- Scaling the numeric feature columns using `StandardScaler`  
- Output stored in a clean DataFrame with original + transformed data  

#### 🔹 Load  
- The final processed dataset is saved as `iris_cleaned.csv`  
- This file includes scaled features and encoded labels  

---

### 📁 Files Included

| File Name               | Description                           |
|------------------------|---------------------------------------|
| `iris_etl_pipeline.ipynb` | Jupyter Notebook with full ETL pipeline |
| `iris_cleaned.csv`        | Output CSV with cleaned and transformed data |
| `README.md`               | This file with task documentation     |

---
## Tools Used
- Python
- Pandas
- Scikit-learn

## Output
- Processed CSV: `iris_cleaned.csv`
###OUTPUT
<img width="1397" height="682" alt="Image" src="https://github.com/user-attachments/assets/a229dea0-60da-4e96-a7d1-ae9dd04b278f" />
