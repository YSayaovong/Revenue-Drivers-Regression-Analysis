CREATE MATERIALIZED VIEW IF NOT EXISTS rev.mv_daily_agg AS
SELECT
  date, store_id, channel_id, channel_name,
  SUM(revenue) AS revenue,
  SUM(marketing_spend) AS marketing_spend,
  SUM(website_traffic) AS website_traffic,
  SUM(num_leads) AS num_leads,
  SUM(sales_calls) AS sales_calls,
  AVG(avg_rating) AS avg_rating,
  SUM(operating_cost) AS operating_cost
FROM rev.fact_daily
GROUP BY 1,2,3,4;
