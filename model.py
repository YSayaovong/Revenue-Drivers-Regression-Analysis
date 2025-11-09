# model.py — train, evaluate, and write predictions to revenue_aggresion.rev.pred_revenue

import pandas as pd
import numpy as np
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from pathlib import Path

# -------------------- 1) DB CONNECTION --------------------
RAW_PASSWORD = "@u$tinM@rwinJ@$min3"
ENC_PWD = quote_plus(RAW_PASSWORD)
DB_URL = f"postgresql+psycopg2://postgres:{ENC_PWD}@127.0.0.1:5432/revenue_aggresion"

engine = create_engine(DB_URL, pool_pre_ping=True)
with engine.connect() as conn:
    db = conn.execute(text("SELECT current_database()")).scalar()
    print("DB OK ->", db)  # should print: revenue_aggresion

# Ensure table exists (idempotent)
DDL = """
CREATE SCHEMA IF NOT EXISTS rev;
CREATE TABLE IF NOT EXISTS rev.pred_revenue (
  store_id   INT,
  channel_id INT,
  y_actual   NUMERIC,
  y_pred     NUMERIC,
  abs_error  NUMERIC,
  model_name TEXT,
  scored_at  TIMESTAMPTZ DEFAULT now()
);
"""
with engine.begin() as conn:
    conn.execute(text(DDL))

# -------------------- 2) LOAD DATA --------------------
csv_path = Path("data") / "revenue_regression_1m_plus.csv"
if not csv_path.exists():
    raise FileNotFoundError(f"Missing dataset at {csv_path.resolve()}")

df = pd.read_csv(csv_path)
print("Loaded rows:", len(df))

# -------------------- 3) FEATURES / TARGET --------------------
features = ["store_id", "channel_id", "website_traffic", "avg_rating", "operating_cost"]
target = "revenue"

X = df[features]
y = df[target]

# -------------------- 4) SPLIT + TRAIN --------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f"Model trained | R2={r2:.4f} | MAE={mae:,.2f}")

# -------------------- 5) PREPARE PREDICTIONS --------------------
pred_df = pd.DataFrame({
    "store_id":   X_test["store_id"].to_numpy(),
    "channel_id": X_test["channel_id"].to_numpy(),
    "y_actual":   y_test.to_numpy(),
    "y_pred":     y_pred
})
pred_df["abs_error"] = (pred_df["y_actual"] - pred_df["y_pred"]).abs()
pred_df["model_name"] = "linear_regression_v1"

print("Pred DF shape:", pred_df.shape)
print("Pred DF sample:\n", pred_df.head(3))

# -------------------- 6) WRITE TO SQL + VERIFY --------------------
with engine.begin() as conn:
    pred_df.to_sql(
        "pred_revenue",
        con=conn,
        schema="rev",
        if_exists="append",
        index=False,
        method="multi",
        chunksize=20000
    )
    cnt = conn.execute(text("SELECT COUNT(*) FROM rev.pred_revenue")).scalar()
    print("Row count in rev.pred_revenue after insert:", cnt)

print("✅ Done.")
