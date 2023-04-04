SELECT date(request_time) as request_time_d,
    avg(a.viewer_count) as avg_viewers,
    max(a.viewer_count) as peak_viewers
    
FROM public.gaules_silver as a

GROUP BY 1
ORDER BY 1