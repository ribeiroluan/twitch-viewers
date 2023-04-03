SELECT 
    date(request_time) as request_time_d,
    COUNT(DISTINCT game_name) as number_of_titles

FROM public.gaules_silver

WHERE type <> 'offline'

GROUP BY 1