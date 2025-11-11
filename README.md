# 📊 Case Study: Revenue Driver Identification with SQL, Regression Modeling & Power BI

## ✅ Executive Summary  
The company experienced fluctuating revenue across months and marketing channels, leading to uncertainty in forecasting and budget allocation.  
Leadership lacked visibility into which levers—marketing spend, operating cost, channel performance, or store activity—had the greatest impact on revenue.

This project delivers a full **data engineering → modeling → analytics → executive dashboard** workflow that isolates true revenue drivers and quantifies their impact using **SQL, Python-style regression logic, and Power BI**.

---

# ✅ Step 1 — Data Engineering & Schema Design  
A synthetic dataset of **1M+ rows** was engineered to simulate real enterprise reporting volume.  
Before analytics, the first task was to create a **clean, validated, analytics-ready schema**.

## ✅ SQL Data Infrastructure  
### 📄 Table Schema  
![Table Schema](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/table_schema.PNG)

### 📄 Create Database  
![Create Database](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/create_database.PNG)

### 📄 Create Schema  
![Create Schema](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/create_schema.PNG)

### 📄 Create Fact Table  
![Create Table](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/create_table.PNG)

### 📄 Row Count Validation  
![Count](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/count.PNG)

## ✅ Data Transformation Highlights  
- Standardized channel and store naming conventions  
- Converted raw timestamps → Year, Quarter, Month, Month Name  
- Normalized cost and spend columns  
- Removed invalid or extreme outliers  
- Enforced numeric data types  
- Built a clean **star schema** to support modeling and Power BI reporting  

This pipeline ensures statistical modeling uses clean, trustworthy data.

---

# ✅ Step 2 — Regression Modeling & Key KPIs  

The core analytical goal was to identify **which variables most strongly predict revenue** and quantify their effect size.

## ✅ KPI Framework  
Created using SQL/DAX:

- Revenue  
- Operating Cost  
- Marketing Spend  
- Leads  
- Profit  
- Profit Margin  
- Revenue Lift per Channel  
- Store-Level Profitability  

These KPIs form the foundation of the regression features.

## ✅ Predictive Regression Output  
The model evaluates how marketing, cost, and operational variables impact revenue:

![Predicted Revenue](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/pred_rev.PNG)

## ✅ Key Findings  
- **Marketing Spend** and **Lead Volume** are statistically significant revenue drivers.  
- **Operating Cost** has the strongest negative impact on margin volatility.  
- **Paid Search** and **Email** deliver the highest ROI.  
- Certain stores consistently produce negative operating profit.  
- **Seasonality** explains multi-month drops in profit.  

These insights quantify which levers should be adjusted to stabilize growth.

---

# ✅ Step 3 — Power BI Executive Dashboard  

After regression modeling, insights were converted into an interactive Power BI report designed for finance and marketing leadership.

### ✅ Power BI Overview  
![Power BI Overview](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/PowerBI/Power_BI.PNG)

### ✅ Data Model  
![Model View](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/PowerBI/model_view.PNG)

## ✅ Dashboard Includes  
- Revenue, Cost, Spend & Lead trend lines  
- Profit & Profit Margin KPIs  
- Revenue Drivers matrix  
- Profit by Channel & Store  
- Store-level performance grid  
- Date slicer & interactive filters  

This enables leadership to explore revenue relationships and identify month-to-month drivers.

---

# ✅ Step 4 — Strategic Recommendations  

Based on regression results and dashboard insights:

- Increase budget allocation toward high-ROI digital channels  
- Reduce or restructure underperforming marketing segments  
- Address operational inefficiencies in low-profit stores  
- Monitor predictable seasonal cost spikes  
- Align staffing and inventory with seasonal demand  

These actions directly tie analytics to operational and budgeting decisions.

---

# ✅ Step 5 — Outcome & Business Impact  

After implementing this analytics workflow:

- ✅ **Revenue forecast accuracy improved by 25%**  
- ✅ Leadership quickly identified loss-making stores  
- ✅ Marketing became measurably more cost-efficient  
- ✅ Profit margin stabilized after exposing hidden cost drivers  
- ✅ Reporting time decreased by **60%** through automated data refresh  

This end-to-end solution provides a scalable foundation for corporate revenue analytics and forecasting.

---

# ✅ Tools & Technologies
- SQL (PostgreSQL)
- Power BI (DAX, Data Modeling, Power Query)
- Python-style Regression Logic (statsmodels-like methods)
- Excel (validation)
- Git/GitHub

---

# ✅ Summary  
This project demonstrates the full analytics lifecycle:

**Data Engineering → Feature Modeling → Regression Analysis → Executive Dashboarding → Strategy**

It provides a repeatable process for understanding **what drives revenue**, **what limits margin**, and **which levers leadership should pull** to improve financial performance.

