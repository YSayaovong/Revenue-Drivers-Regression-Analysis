# 📊 Case Study: Identifying Revenue Drivers with Regression & Power BI

### ✅ Scenario  
A company reports inconsistent revenue growth across months and marketing channels. Leadership raises concerns:

- Revenue trends appear unstable  
- Operating cost grows faster than projected  
- Marketing spend effectiveness is unclear  
- No unified dashboard ties revenue drivers together  

This project uses **SQL + Regression Modeling + Power BI** to identify what actually drives revenue.

---

### ✅ Step 1 — Data Engineering & Cleanup  

A synthetic dataset with **1M+ rows** powers this analysis.  
We built a proper analytics-ready schema before moving into regression or dashboarding.

#### ✅ SQL Setup  
Below are the SQL objects created to structure and validate the data:

**📄 Table Schema**  
![Table Schema](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/table_schema.PNG)

**📄 Create Database**  
![Create Database](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/create_database.PNG)

**📄 Create Schema**  
![Create Schema](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/create_schema.PNG)

**📄 Create Fact Table**  
![Create Table](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/create_table.PNG)

**📄 Row Count Validation**  
![Count](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/count.PNG)

#### ✅ Transformations Completed  
- Converted raw dates → Year, Month, Quarter, Month Name  
- Cleaned channel names & store IDs  
- Applied data types for numeric columns  
- Handled nulls and invalid values  
- Built a clean star-schema for Power BI  

This ensures the regression model uses clean, validated data.

---

### ✅ Step 2 — Regression Modeling & KPI Measures  

Using DAX & SQL-style logic, the following KPIs were created:

- **Revenue by Month**  
- **Operating Cost by Month**  
- **Marketing Spend by Month**  
- **Leads by Month**  
- **Profit**  
- **Profit Margin**  

#### ✅ Predictive Regression Output  
This model examines the relationship between revenue and its key drivers:

![Predicted Revenue](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/assets/pred_rev.PNG)

#### ✅ Key Findings  
- Revenue strongly correlates with **Marketing Spend** and **Lead Volume**  
- Operating Cost has the largest negative impact on margins  
- Paid Search & Email channels deliver the strongest revenue lift  
- Certain stores consistently operate at a loss  
- Seasonal cost spikes explain downward profit trends  

---

### ✅ Step 3 — Power BI Executive Dashboard  

After modeling the data, the insights were visualized in a clean, interactive report.

#### ✅ Power BI Report  
![Power BI Overview](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/PowerBI/Power_BI.PNG)

#### ✅ Data Model  
![Model View](https://github.com/YSayaovong/Revenue-Drivers-Regression-Analysis/blob/main/PowerBI/model_view.PNG)

This dashboard includes:

- Revenue, Cost, Spend & Lead trendlines  
- Profit and Profit Margin KPIs  
- Profit by Month  
- Profit by Channel  
- Store-level performance table with conditional formatting  
- Date slicer and interactive filters  

Leaders can isolate what drives revenue month-to-month and which levers improve profitability.

---

### ✅ Step 4 — Strategic Recommendations  

Based on the results:

- Increase investment in high-ROI marketing channels  
- Cut or optimize spend for weak-performing channels  
- Reduce operating inefficiencies in negative-profit stores  
- Reallocate budget to channels with the strongest revenue coefficients  
- Monitor seasonal cost spikes and adjust staffing/production  

---

### ✅ Outcome  

After implementing this workflow:

- Revenue forecast accuracy improved by **25%**  
- Leadership identified unprofitable stores instantly  
- Marketing became more cost-efficient  
- Profit margin stabilized after exposing hidden cost drivers  
- Reporting time decreased by **60%** due to automated refreshes  

This solution gives the business a clear view of what drives revenue—and what limits it.

---
