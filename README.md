✨ Heart Disease Prediction - AI Project ✨

An end-to-end AI project that predicts the likelihood of heart disease using real-world medical data. It combines data preprocessing, machine learning, evaluation, visualization, and a polished Streamlit UI.

---

🚀 Project Overview

This project aims to classify patients as having heart disease or not, based on features such as age, cholesterol levels, chest pain type, and other clinical parameters. It includes:

* 🔎 Exploratory Data Analysis (EDA) with Seaborn & Matplotlib
* 🧼 Data cleaning: handling missing values, encoding categorical variables, outlier removal
* ⚖️ Feature scaling using StandardScaler
* 🧠 Model training using:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine (SVM)
  
* 🧪 Feature selection using:

  * Feature importance
  * Recursive Feature Elimination (RFE)
  * Chi-Square Test
* 📊 Evaluation metrics: Accuracy, Precision, Recall, F1 Score
* 📈 ROC Curve and AUC Score visualization
* 🧩 Unsupervised Learning: K-Means & Hierarchical Clustering
* 🎯 Selection of best-performing model
* 💻 Streamlit GUI for user interaction


---

🧩 Technologies Used

* Python (pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost)
* Streamlit (for interactive web-based GUI)
* Jupyter Notebook (for development & analysis)

---

📦 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/Yomna-Mahsoob/Heart-Disease-Prediction
cd Heart-Disease-Prediction
```

2. **Set up a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app locally**

```bash
streamlit run ui/app.py
```


---

📁 Project Structure

```
📂 Heart-Disease-Prediction
├── data/                         # Dataset
├── models/                       # Saved trained model (best_rf.pkl)
├── notebooks/                    # Jupyter notebooks for training & analysis
├── results/                      # Evaluation metrics, plots
│   └── evaluation_metrics.txt
├── ui/
│   └── app.py                    # Streamlit GUI app
├── requirements.txt              # Project dependencies
├── README.md                     # Project overview
```

---

💡 Inspiration

This project showcases how to transform a machine learning pipeline into a deployable and user-friendly product using Streamlit. It is an ideal example for students and professionals learning how to bridge the gap between modeling and deployment.

---

🎀 The GUI

The app provides a beautiful and responsive interface using Streamlit, with:

* Consistent blue-themed design 🎨
* Clean and intuitive input fields for patient data
* One-click prediction based on the trained model
* Real-time feedback (low or high risk)


---


