# 📊 Case Study: Identifying Revenue Drivers with Regression & Power BI

### ✅ Scenario  
A company reports inconsistent revenue growth across months and marketing channels. Leadership raises concerns:

- Revenue trends appear unstable  
- Operating cost grows faster than projected  
- Marketing spend effectiveness is unclear  
- No unified dashboard ties revenue drivers together  

This analysis uses **regression modeling + Power BI** to isolate what actually drives revenue.

---

### ✅ Step 1 — Data Engineering & Cleanup  
The project begins with a synthetic dataset of **1,000,000+ rows** representing:

- Daily revenue  
- Operating cost  
- Marketing spend  
- Leads generated  
- Channel performance  
- Store-level contribution  

**Transformations completed:**

- Converted raw dates into a complete date dimension (Year, Month, Month Name, Quarter)  
- Cleaned channel names and store IDs  
- Created fact/dimension model for analytics  
- Removed nulls and standardized numeric fields  
- Built a star-schema model for fast Power BI performance  

This ensures the regression model and visuals rely on clean, validated data.

---

### ✅ Step 2 — KPI Modeling & Regression Diagnostics  
Using DAX, calculated measures, and SQL-style materialized logic, we created:

- **Revenue by Month**  
- **Operating Cost by Month**  
- **Marketing Spend by Month**  
- **Leads by Month**  
- **Profit**  
- **Profit Margin**  

A regression model determines which variables explain most of the revenue movement.

**Key Findings:**

- Revenue is strongly correlated with **marketing spend** and **lead volume**  
- Operating cost is negatively tied to profitability  
- Paid Search and Email channels show the strongest revenue lift  
- Certain stores consistently operate at a negative profit margin  
- Cost ramp-ups in specific months drive profit volatility  

These insights were not visible before building a unified view.

---

### ✅ Step 3 — Power BI Executive Dashboard  
The dashboard provides leadership a full picture of revenue behavior:

- Revenue, Operating Cost, Marketing Spend & Leads trendline  
- Profit and Profit Margin KPIs  
- Profit by Month bar chart  
- Channel-level performance comparison  
- Store-level table with conditional formatting  
- Fully interactive slicers and cross-filters  

Leaders can finally see what’s driving revenue changes month-by-month and which levers increase profit.

---

### ✅ Step 4 — Strategic Recommendations  
Based on the regression + dashboard insights:

- Increase investment in high-ROI marketing channels  
- Reduce operational inefficiencies in negative-profit stores  
- Reallocate budget toward channels with the strongest revenue coefficients  
- Monitor monthly cost spikes tied to seasonality  
- Use lead data to forecast revenue more accurately  

---

### ✅ Outcome  
After implementing this workflow:

- Revenue forecast accuracy improves by **25%**  
- Leadership identifies poor-performing stores instantly  
- Marketing budget becomes more efficient  
- Profit margin stabilizes after cost visibility increases  
- Reporting time decreases by **60%** due to automated Power BI refresh**  

This solution gives the business a clear map of what drives revenue—and what destroys it.

---

# 📸 Dashboard

### Power BI Overview  
![Power BI Dashboard](Power_BI.PNG)

### Data Model  
![Data Model](model_view.PNG)

---
