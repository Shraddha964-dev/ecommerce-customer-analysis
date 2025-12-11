# ecommerce-customer-analysis
An end-to-end data analysis project performing customer segmentation on UK e-commerce data to identify high-value and at-risk customers.

# E-Commerce Customer Segmentation Analysis

## Project Overview
This end-to-end data analysis project performs customer segmentation on a UK-based online retail dataset. The goal is to move from a generic marketing strategy to a targeted one by identifying distinct customer groups based on their purchasing behavior. This allows for strategies to retain high-value customers and win back those at risk of churning.

## Business Problem
The business suffers from inefficient marketing spend by treating all customers the same. The analysis aims to answer:
- Who are our most valuable customers?
- Which customers are at risk of leaving?
- How can we tailor marketing efforts to different segments to increase customer lifetime value (CLV) and reduce churn?

## Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **Environment:** Jupyter Notebook
- **Version Control:** Git & GitHub
- **Visualization:** Tableau Public (Final Dashboard - Link to be added)

## Project Structure
ecommerce-customer-analysis/
├── data/
│ ├── raw/ # Original, immutable data dump
│ └── processed/ # Cleaned data (to be added)
├── notebooks/
│ └── 01_data_cleaning_eda.ipynb # Main analysis notebook
├── scripts/ # Optional helper scripts
├── images/ # Visualizations and graphs
├── README.md # Project documentation (you are here)
└── .gitignore # Specifies files to ignore in version control


## Data Sourcing

**Dataset:** [Online Retail II Data Set](https://archive.ics.uci.edu/dataset/502/online+retail+ii) from the UCI Machine Learning Repository.

**Description:** The dataset contains all transactions occurring between 01/12/2009 and 09/12/2011 for a UK-based online retail store. It includes ~1.07 million transactions across 8 columns, including `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, and `Country`.

**Data Description**
The dataset comprises approximately 1.07 million transactions across 8 columns. The key fields for our analysis are:

**InvoiceNo:** Unique identifier for each transaction.
**StockCode:** Unique identifier for each product.
**Description:** Name of the product.
**Quantity:** Number of units per transaction.
**InvoiceDate:** Date and time of the transaction.
**UnitPrice:** Price of a single unit in British Pounds (£).
**CustomerID:** Unique identifier for each customer.
**Country:** The country where the customer is based.

**Acquisition & Initial Challenge:**
The dataset was manually downloaded from the source as an Excel (`.xlsx`) file on May 22, 2024, and added to the project repository. Upon initial loading within the Jupyter Notebook using `pd.read_excel()`, a **`'Excel file format cannot be determined'`** error was thrown. This indicated a compatibility issue between the file and pandas' default Excel parsing engines.

**Solution & Rationale:**
To resolve this and ensure maximum reproducibility and simplicity, the original `.xlsx` file was opened and exported as a **CSV (Comma-Separated Values)** file. The analysis then proceeds using `pd.read_csv()`.

## Analysis Steps
The project will follow a typical data analysis lifecycle:
1.  **Data Acquisition & Sourcing** ✅ *
2.  **Data Cleaning & Preprocessing** *(Handling missing values, duplicates, outliers)* 
3.  **Exploratory Data Analysis (EDA)** *(Uncovering patterns and trends through visualizations)* ✅ *(Current Stage)*
4.  **Feature Engineering** *(Creating RFM metrics: Recency, Frequency, Monetary Value)*
5.  **Modeling** *(Using K-Means Clustering for customer segmentation)*
6.  **Interpretation & Business Recommendations** *(Translating clusters into actionable strategies)*

## How to Run This Project
1.  Clone this repository:
    ```bash
    git clone https://github.com/Shraddha964-dev/ecommerce-customer-analysis.git
    ```
2.  Navigate to the project directory.
3.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook notebooks/E-Commerce_Customer_Segmentation_project.ipynb
    ```
    
## Key Insights & Recommendations

### Customer Segments Identified:
1. **Champions (14.5%):** High-value VIP customers generating 60% of revenue
2. **Loyal Customers (33.0%):** Regular buyers with strong growth potential  
3. **New Customers (30.9%):** Recent acquisitions needing onboarding
4. **At Risk (21.5%):** Inactive customers requiring reactivation

### Strategic Recommendations:
- **Protect Champions** with exclusive VIP benefits
- **Grow Loyal Customers** through cross-selling
- **Activate New Customers** with educational content
- **Recover At-Risk** with targeted win-back campaigns

### Financial Impact:
- **Current Revenue:** £7.1M annually
- **Potential Increase:** £420K+ (6% growth)
- **Implementation Priority:** Q1 2024

## Dashboard
![Customer Segmentation Dashboard](images/customer_segmentation_dashboard.png)


