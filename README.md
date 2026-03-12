# 🛒 E-Commerce Customer Segmentation Analysis

End-to-end customer segmentation on 1.07M+ UK retail transactions using 
RFM analysis and K-Means clustering to identify high-value and at-risk customers.

## 🚀 Live Dashboard
👉 [View Interactive Dashboard](https://ecommerce-customer-analysis-jqzy8aeurhccjtmttyvzw3.streamlit.app/)

---

## 📌 Key Results

| Segment | % of Customers | Revenue Contribution |
|---|---|---|
| Champions | 14.5% | 60% of £7.1M total |
| Loyal Customers | 33.0% | Strong repeat spend |
| New Customers | 30.9% | Recent acquisitions |
| At Risk | 21.5% | £420K+ recoverable |

**Projected revenue impact from targeted strategy: £420K+ annually (6% growth)**

---

## 🧩 Business Problem

Most e-commerce businesses treat all customers the same — sending identical 
promotions regardless of behavior. This wastes marketing budget and accelerates 
churn among high-value customers.

This project answers:
- Who are our most valuable customers and what do they look like?
- Which customers are about to leave — and how do we win them back?
- How do we move from generic campaigns to targeted segment strategies?

---

## 🔍 Analysis Steps

1. **Data Cleaning** — handled 1.07M+ rows, missing CustomerIDs, 
   negative quantities, duplicate invoices
2. **Exploratory Data Analysis** — revenue trends, top products, 
   country distribution, seasonal patterns
3. **Feature Engineering** — built RFM metrics (Recency, Frequency, 
   Monetary Value) per customer
4. **Modeling** — K-Means clustering with Elbow Method + Silhouette 
   Score to find optimal k=4
5. **Interpretation** — mapped clusters to business segments, 
   quantified revenue impact per segment
6. **Dashboard** — deployed interactive Streamlit app for non-technical stakeholders

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python (Pandas, NumPy) | Data cleaning & feature engineering |
| Scikit-learn | K-Means clustering, scaling |
| Matplotlib, Seaborn | EDA visualizations |
| Streamlit | Interactive dashboard deployment |
| Jupyter Notebook | Analysis environment |
| Git & GitHub | Version control |

---

## 📁 Project Structure
```
ecommerce-customer-analysis/
├── app.py                          # Streamlit dashboard
├── requirements.txt                # Dependencies
├── data/
│   ├── raw/                        # Original dataset
│   └── processed/
│       └── rfm_clustered.csv       # Final clustered data
├── notebooks/                      # Jupyter analysis notebooks
├── images/                         # Visualizations
└── README.md
```

## ▶️ How to Run Locally
```bash
git clone https://github.com/Shraddha964-dev/ecommerce-customer-analysis.git
cd ecommerce-customer-analysis
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Dataset

**Source:** [UCI Machine Learning Repository — Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii)  
**Size:** ~1.07 million transactions · 4,300+ unique customers  
**Period:** December 2009 – December 2011 · UK-based online retailer

---

## 👩‍💻 About

## 👩‍💻 About ME

I am actively seeking entry-level opportunities in Data Analyst and continuously building projects to strengthen my skills.

If you have suggestions or feedback, feel free to share.

If you find this helpful, feel free to star the repository!

If you liked what you saw, want to have a chat with me about the portfolio, work opportunities, or collaboration, shoot an email at ssajane86@gmail.com.

[LinkedIn](https://www.linkedin.com/in/shraddha-sajane) | 
[GitHub](https://github.com/Shraddha964-dev) |
[SQL Portfolio Project](https://github.com/Shraddha964-dev/banking-transaction-sql-analysis)
