SELECT type, 
    avg(viewer_count) 
    
FROM public.gaules_silver

GROUP BY type