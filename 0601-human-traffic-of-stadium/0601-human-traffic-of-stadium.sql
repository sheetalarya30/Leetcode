WITH X AS (
    SELECT 
        id, 
        visit_date, 
        people, 
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
Y AS (
    SELECT 
        id,
        visit_date,
        people,
        COUNT(*) OVER (PARTITION BY grp) AS cnt
    FROM X
)
SELECT 
    id, 
    visit_date, 
    people
FROM Y
WHERE cnt >= 3
ORDER BY visit_date ASC;