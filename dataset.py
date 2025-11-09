# dataset.py
# Generate a 1.1M+ row synthetic business dataset (realistic signals + noise)
# Outputs: data/revenue_regression_1m_plus.csv (+ Parquet if pyarrow/fastparquet installed)

import numpy as np
import pandas as pd
from pathlib import Path

# -------- Settings --------
START_DATE = "2023-01-01"
END_DATE   = "2024-12-31"   # ~730 days
N_STORES   = 300            # 300 stores
CHANNELS   = ["Paid Search", "Organic", "Email", "Affiliate", "Direct"]
OUT_DIR    = Path("data")

# -------- Setup --------
OUT_DIR.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(42)

# Build base grids
dates = pd.date_range(START_DATE, END_DATE, freq="D")        # ~730 days
n_days = len(dates)
store_ids   = np.arange(1, N_STORES + 1, dtype=np.int32)
channel_ids = np.arange(1, len(CHANNELS) + 1, dtype=np.int16)

# Cartesian product: day × store × channel ≈ 730 * 300 * 5 = 1,095,000+
date_col    = np.repeat(dates.values, N_STORES * len(CHANNELS))
store_col   = np.tile(np.repeat(store_ids, len(CHANNELS)), n_days)
channel_col = np.tile(channel_ids, n_days * N_STORES)

# Seasonality by month
month = pd.DatetimeIndex(date_col).month
season_mult = 0.85 + (month - 1) * (0.35 / 11)

# Store “size” effect
store_base = 0.70 + (store_col % 10) * 0.05

# Channel cost & efficiency
chan_cost = np.array([1.25, 0.65, 0.80, 0.75, 0.55])
chan_eff  = np.array([0.95, 1.10, 1.00, 0.90, 0.80])
chan_cost_col = chan_cost[channel_col - 1]
chan_eff_col  = chan_eff[channel_col - 1]

# Marketing spend ($)
base_spend = 28_000
marketing_spend = (
    base_spend * season_mult * store_base * chan_cost_col
    + rng.normal(0, 6_000, size=len(date_col))
)
marketing_spend = np.clip(marketing_spend, 3_000, 120_000)

# Website traffic
website_traffic = (
    marketing_spend
    * rng.uniform(6.5, 12.0, size=len(marketing_spend))
    * chan_eff_col
    + rng.normal(0, 4_000, size=len(marketing_spend))
)
website_traffic = np.clip(website_traffic, 5_000, 1_500_000).astype(np.int32)

# Leads & sales calls
num_leads = (
    website_traffic
    * rng.uniform(0.010, 0.030, size=len(website_traffic))
    * chan_eff_col
).astype(np.int32)
num_leads = np.clip(num_leads, 0, None)

sales_calls = (
    num_leads * rng.uniform(0.10, 0.24, size=len(num_leads))
).astype(np.int32)
sales_calls = np.clip(sales_calls, 0, None)

# Ratings
avg_rating = (
    rng.normal(4.25, 0.22, size=len(marketing_spend))
    + (store_col % 7) * 0.01
    + (channel_col % 5) * 0.005
)
avg_rating = np.clip(avg_rating, 3.5, 5.0).round(2)

# Operating cost
day_index = (pd.to_datetime(date_col) - pd.Timestamp(START_DATE)).days
operating_cost = (
    85_000 + day_index * 18 + (store_col % 12) * 1_200 + rng.normal(0, 5_000, size=len(day_index))
)
operating_cost = np.clip(operating_cost, 40_000, 250_000).round(2)

# Revenue (latent regression + noise)
revenue = (
    (marketing_spend * 1.65)
    + (num_leads * 11.5)
    + (sales_calls * 24.0)
    + (avg_rating * 7_500.0)
    - (operating_cost * 0.58)
    + rng.normal(0, 7_000, size=len(marketing_spend))
).round(2)

revenue = np.clip(revenue, -20_000, None)

# Assemble DataFrame
df = pd.DataFrame({
    "date": pd.to_datetime(date_col),
    "store_id": store_col.astype(np.int32),
    "channel_id": channel_col.astype(np.int16),
    "channel_name": [CHANNELS[i - 1] for i in channel_col],
    "marketing_spend": marketing_spend.round(2),
    "website_traffic": website_traffic,
    "num_leads": num_leads,
    "sales_calls": sales_calls,
    "avg_rating": avg_rating,
    "operating_cost": operating_cost,
    "revenue": revenue
})

# Save files
csv_path = OUT_DIR / "revenue_regression_1m_plus.csv"
parq_path = OUT_DIR / "revenue_regression_1m_plus.parquet"

df.to_csv(csv_path, index=False)

saved_parquet = False
try:
    df.to_parquet(parq_path, index=False)
    saved_parquet = True
except Exception as e:
    print("Parquet skipped (install pyarrow or fastparquet):", e)

# Summary
print("Rows:", len(df))
print("Unique stores:", df['store_id'].nunique(), 
      "| Channels:", df['channel_id'].nunique(), 
      "| Days:", df['date'].nunique())
print("Saved CSV ->", csv_path)
print("Saved Parquet ->", parq_path if saved_parquet else "(skipped)")
