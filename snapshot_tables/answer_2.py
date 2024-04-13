import pandas as pd
import sqlite3

query="""
SELECT user_id
FROM user_id
WHERE user_id NOT IN (
    SELECT DISTINCT user_id FROM deposits where tx_status='complete'
);

"""
conn = sqlite3.connect('data.db')

results = pd.read_sql_query(query, conn)
results.to_csv("answer_2.csv", index=False)
results
conn.close()