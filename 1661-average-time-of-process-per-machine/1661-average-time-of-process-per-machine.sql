# Write your MySQL query statement below
SELECT
    machine_id,
    ROUND(
        SUM(if(activity_type = 'start',-timestamp,timestamp)
        ) / COUNT(DISTINCT process_id)    
    , 3) as processing_time
FROM Activity
GROUP BY machine_id