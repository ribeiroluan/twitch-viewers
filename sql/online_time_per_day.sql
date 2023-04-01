WITH setup AS (

    SELECT DISTINCT
        date(request_time) as request_time_d,
        MIN(request_time) OVER(PARTITION BY date(request_time)) AS MinTimeStamp,
        MAX(request_time) OVER(PARTITION BY date(request_time)) AS MaxTimeStamp
        
    FROM public.gaules_silver
    
    WHERE type='live'
    
)

SELECT *,
    AGE(MaxTimeStamp, MinTimeStamp) as online_time,
    EXTRACT(epoch FROM AGE(MaxTimeStamp, MinTimeStamp))/3600 as online_time_hours

FROM setup
    
FROM public.gaules_silver as a

LEFT JOIN days as b ON extract(isodow from a.request_time) = b.day_number

GROUP BY 1
ORDER BY day_of_week