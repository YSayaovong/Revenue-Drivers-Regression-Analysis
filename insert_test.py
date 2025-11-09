from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

RAW_PASSWORD = "@u$tinM@rwinJ@$min3"
ENC = quote_plus(RAW_PASSWORD)
DB_URL = f"postgresql+psycopg2://postgres:{ENC}@127.0.0.1:5432/analytics"
engine = create_engine(DB_URL, pool_pre_ping=True)

with engine.begin() as conn:
    conn.execute(text("""
        INSERT INTO rev.pred_revenue (store_id, channel_id, y_actual, y_pred, abs_error, model_name)
        VALUES (9999, 9, 100.0, 95.0, 5.0, 'smoketest');
    """))
    cnt = conn.execute(text("SELECT COUNT(*) FROM rev.pred_revenue")).scalar()
    print("Row count after smoketest insert:", cnt)
