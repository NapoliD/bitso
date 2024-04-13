-- 1) How many users were active on a given day (they made a deposit or withdrawal)


--"With this query, you can identify the entire historical data, and with the second one,
 --you can pinpoint a specific date by changing the date in the WHERE clause."
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
where DATE(event_date)='2020-01-04' -- day for exmaple
GROUP BY date
ORDER BY date ; 

-- 2)Identify users haven't made a deposit

SELECT user_id
FROM user_id
WHERE user_id NOT IN (
    SELECT DISTINCT user_id FROM deposits where tx_status='complete'
);

--3)Identify on a given day which users have made more than 5 deposits historically

SELECT
     user_id
FROM
    deposits
    where  tx_status='complete'
GROUP BY user_id
HAVING
    COUNT(*) > 5
    order by user_id
