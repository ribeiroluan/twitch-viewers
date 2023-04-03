SELECT 
    COUNT(DISTINCT game_name) as number_of_titles

FROM public.gaules_silver

WHERE type <> 'offline'