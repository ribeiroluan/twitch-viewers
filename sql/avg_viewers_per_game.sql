SELECT CASE WHEN game_name = 'Counter-Strike: Global Offensive' THEN 'CS-GO' ELSE game_name END AS game_name, 
    type,
    avg(viewer_count) 
    
FROM public.gaules_silver

WHERE game_name <> 'None'

GROUP BY game_name, type