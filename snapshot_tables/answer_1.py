import pandas as pd
import sqlite3

query="""
SELECT
    DATE(event_date) AS date,
    COUNT(DISTINCT user_id) AS active_users
FROM (
    SELECT date(event_timestamp) AS event_date, user_id
    FROM deposits
    UNION ALL
    SELECT date(event_timestamp) AS event_date, user_id
    FROM withdrawal
) AS all_events
where DATE(event_date)=date('2020-01-02')
GROUP BY date
ORDER BY date
;
"""
conn = sqlite3.connect('data.db')

results = pd.read_sql_query(query, conn)
results.to_csv("answer_1.csv", index=False)
# Close connection
conn.close()
results