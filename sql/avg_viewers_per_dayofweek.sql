WITH days AS (
    SELECT 1 as day_number, '1. Monday' day_of_week
    UNION ALL SELECT 2, '2. Tuesday'
    UNION ALL SELECT 3, '3. Wednesday'
    UNION ALL SELECT 4, '4. Thursday'
    UNION ALL SELECT 5, '5. Friday'
    UNION ALL SELECT 6, '6. Saturday'
    UNION ALL SELECT 7, '7. Sunday'
    
)

SELECT b.day_of_week, 
    avg(a.viewer_count) 
    
FROM public.gaules_silver as a

LEFT JOIN days as b ON extract(isodow from a.request_time) = b.day_number

GROUP BY 1
ORDER BY day_of_week