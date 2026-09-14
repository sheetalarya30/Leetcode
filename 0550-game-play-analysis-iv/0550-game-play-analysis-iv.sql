
-- select round(avg(datediff(a.event_date,b.event_date)=1),2) as fraction
-- from Activity a
-- join Activity b
-- on a.player_id=b.player_id;



-- select  from
-- (select,
-- lag(event_date) over(order by event_date) as fraction
-- from Activity);




SELECT 
    ROUND(AVG(a.event_date IS NOT NULL), 2) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) f
LEFT JOIN Activity a 
  ON f.player_id = a.player_id 
 AND DATEDIFF(a.event_date, f.first_date) = 1;