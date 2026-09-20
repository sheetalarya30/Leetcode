select round(avg (a.event_date is not null),2) as fraction
from (
    select player_id,min(event_date) as first_date
    from Activity
    group by player_id
) f
left join Activity a
on a.player_id=f.player_id
and datediff(a.event_date,f.first_date)=1;

















 