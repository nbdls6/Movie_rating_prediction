# 🎬 **Movie Critic Rating Prediction**  

## 🌟 **Overview**  
Welcome to the **Movie Critic Rating Prediction Project**! This project showcases the full machine learning workflow to predict movie critic ratings. From raw data extraction to building predictive models, this project highlights the power of data-driven insights in the movie industry.  

Whether you're a film buff or a machine learning enthusiast, this project has something exciting to offer! 🍿  

---

## 📂 **Repository Contents**  

### **1. Code**  
- **`data_cleaning_and_eda.ipynb`**: A comprehensive notebook that performs data cleaning, exploratory analysis, and visualizations.  
- **`feature_engineering_and_modeling.ipynb`**: The powerhouse notebook for feature engineering, predictive modeling, and evaluation.  

### **2. Data**  
- **`movies_data.csv`**: The original dataset used for analysis.  
- Processed `.pkl` files created during feature engineering for reuse in modeling.  

### **3. Environment Details**  
- **`requirements.txt`**: A list of all Python libraries and versions used in the project.  

### **4. Documentation**  
- **`README.md`**: You're reading it now! 🎉  
- Detailed markdown cells in the notebooks to guide you through the analysis.  

### **5. Utilities**  
- **`.gitignore`**: Ensures unnecessary files.
- **`.env`**: Stores personal keys.

---

## 🛠️ **Project Workflow**  

### **🔍 1. Scope and Data Gathering**  
The goal is to build a model that predicts **movie critic ratings**.  
- Connected to the `everything2024` database in the `mlds422` schema using `psycopg2`.  
- Extracted rich movie data for analysis and modeling.  

---

### **📊 2. Data Cleaning & Exploratory Data Analysis (EDA)**  
The fun begins with exploring the movie dataset:  
- **Highlights**:
  - 🎥 Visuals that bring insights to life!  
  - 📈 Insights into trends, preferences, and popular genres pre-2010.  

---

### **🚀 3. Feature Engineering**  
Created meaningful features to enhance model performance:  
- **`kid_friendly`**: Binary feature for family-friendly movies.  
- **Genre Dummies**: One-hot encoding for genres.  
- Custom engineered features designed to capture complex patterns in the data.  

---

### **🤖 4. Modeling**  
- Split the data:  
  - **Training**:
  - **Test**:  
- Built **6 Linear Regression Models**, starting simple and progressively incorporating engineered features.  
- Evaluated models using:  
  - 📊 **R²**: Coefficient of determination.  
  - 📉 **MAE**: Mean Absolute Error.  
  - 🔧 **RMSE**: Root Mean Squared Error.  

---

## ✨ **Project Insights**  
- **Best Model**: Identified the top-performing model and the features driving its success.  
- **Key Takeaways**:
  - 
  - 

---

## 🛠️ **How to Run the Project**  

### **1. Clone the Repository**  
```bash
git clone <your-private-repo-url>
cd <repository-name>
```

### **2. Set Up the Environment**  
- **Using pip**:  
  ```bash
  pip install -r requirements.txt
  ```  

### **3. Run the Code**  

### **4. Database Credentials**  
- Replace placeholders in the database connection code with your credentials.  
- **Important**: Remove credentials before pushing to GitHub.  

---

## 🌟 **Future Work**  
- Experiment with **ensemble models** like Random Forest and Gradient Boosting.  
- Incorporate external data for richer features.  
- Perform **hyperparameter tuning** to optimize model performance.  

---

## 💡 **Key Learnings**  
This project demonstrates:  
- The importance of **data cleaning and EDA** in uncovering hidden insights.  
- How thoughtful **feature engineering** improves model accuracy.  
- The iterative nature of **machine learning modeling** to refine predictions.  

---

Feel free to reach out for any feedback or questions! 🚀