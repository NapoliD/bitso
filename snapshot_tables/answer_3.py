import pandas as pd
import sqlite3

query="""
SELECT
     user_id
FROM
    deposits
    where  tx_status='complete'
GROUP BY user_id
HAVING
    COUNT(*) > 5
    order by user_id

;

"""
conn = sqlite3.connect('data.db')

results = pd.read_sql_query(query, conn)
results.to_csv("answer_3.csv", index=False)

conn.close()
results