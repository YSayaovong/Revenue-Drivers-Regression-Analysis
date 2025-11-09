CREATE TABLE IF NOT EXISTS rev.fact_daily (
  date             date,
  store_id         int,
  channel_id       smallint,
  channel_name     text,
  marketing_spend  numeric(12,2),
  website_traffic  int,
  num_leads        int,
  sales_calls      int,
  avg_rating       numeric(3,2),
  operating_cost   numeric(12,2),
  revenue          numeric(12,2)
);