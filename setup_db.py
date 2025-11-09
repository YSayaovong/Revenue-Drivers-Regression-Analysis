from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

# --- your actual password ---
RAW_PASSWORD = "@u$tinM@rwinJ@$min3"
ENC = quote_plus(RAW_PASSWORD)

# ✅ FIX: use the correct database everywhere
DB_URL = f"postgresql+psycopg2://postgres:{ENC}@127.0.0.1:5432/revenue_aggresion"

engine = create_engine(DB_URL, pool_pre_ping=True)

ddl = """
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
    # ✅ Confirm which DB you are truly in
    dbname = conn.execute(text("SELECT current_database()")).scalar()
    print("✅ Connected to database:", dbname)

    # ✅ Create schema + table
    conn.execute(text(ddl))
    print("✅ Schema + table ensured.")

    # ✅ Insert a smoketest row
    conn.execute(text("""
        INSERT INTO rev.pred_revenue (store_id, channel_id, y_actual, y_pred, abs_error, model_name)
        VALUES (9999, 9, 100.0, 95.0, 5.0, 'python-smoketest');
    """))

    # ✅ Count rows AFTER the insert
    cnt = conn.execute(text("SELECT COUNT(*) FROM rev.pred_revenue")).scalar()
    print("✅ Row count after smoketest insert:", cnt)
