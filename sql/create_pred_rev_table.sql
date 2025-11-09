CREATE TABLE IF NOT EXISTS rev.pred_revenue (
  store_id   INT,
  channel_id INT,
  y_actual   NUMERIC,
  y_pred     NUMERIC,
  abs_error  NUMERIC,
  model_name TEXT,
  scored_at  TIMESTAMPTZ DEFAULT now()