# 📊 Revenue Drivers Regression Analysis  
*Power BI + Regression Modeling + Marketing & Cost Drivers*

![Power BI Dashboard](./Power_BI.PNG)

---

## 📌 Overview
This project analyzes **what drives revenue**, using:

- Power BI  
- Regression modeling  
- Exploratory data analysis  
- Marketing, cost, and revenue KPIs  

The goal is to help leadership understand which metrics influence revenue the most and how performance changes across **months, stores, and marketing channels**.

---

## 📂 Project Structure
```
Revenue-Drivers-Regression-Analysis/
│── data/
│     └── revenue_regression_1m_plus.csv
│
│── pbix/
│     └── revenue_drivers_regression_analysis.pbix
│
│── screenshots/
│     ├── Power_BI.PNG
│     └── model_view.PNG
│
└── README.md
```

---

## ✅ Main Features

### 📈 1. Monthly Performance Trends
- Revenue  
- Operating Cost  
- Marketing Spend  
- Leads  
- Profit  
- Profit Margin  

---

### 📊 2. Profitability Insights
- Profit by Month  
- Store-level profitability  
- Channel-level profit comparison  
- Conditional formatting  

---

### 📣 3. Channel Performance Breakdown
Marketing channels analyzed:
- Affiliate  
- Direct  
- Email  
- Organic  
- Paid Search  

---

### 🏬 4. Store-Level Financial Table
Includes:
- Revenue  
- Operating Cost  
- Profit  
- Profit Margin  

---

## 🧮 DAX Measures Used
```
Revenue by Month = SUM('rev_fact_daily'[revenue])

Operating Cost by Month = SUM('rev_fact_daily'[operating_cost])

Marketing Spend by Month = SUM('rev_fact_daily'[marketing_spend])

Leads by Month = SUM('rev_fact_daily'[num_leads])

Profit = [Revenue by Month] - [Operating Cost by Month] - [Marketing Spend by Month]

Profit Margin = DIVIDE([Profit], [Revenue by Month], 0)
```

---

## 🛠 Tools Used
- Power BI Desktop  
- DAX  
- CSV dataset (~1M rows)  
- Power Query  

---

## ✅ Purpose of Project
This project demonstrates core **mid‑level data analyst** skills:

- Data modeling  
- KPI creation  
- Trend analysis  
- Financial reporting  
- Dashboard design  
- Business storytelling  

---

## 📬 Contact
**Yengkong Sayaovong**  
GitHub: https://github.com/YSayaovong  
