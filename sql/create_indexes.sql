CREATE INDEX IF NOT EXISTS idx_fact_date    ON rev.fact_daily(date);
CREATE INDEX IF NOT EXISTS idx_fact_store   ON rev.fact_daily(store_id);
CREATE INDEX IF NOT EXISTS idx_fact_channel ON rev.fact_daily(channel_id);
CREATE INDEX IF NOT EXISTS idx_fact_dc      ON rev.fact_daily(date, channel_id, store_id);
