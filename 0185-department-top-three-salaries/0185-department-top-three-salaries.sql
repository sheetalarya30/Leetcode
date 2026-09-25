with ranksalary as(
    select d.name as Department,
    e.name as Employee,
    e.salary,
    dense_rank() over(partition by e.departmentId order by e.salary desc) as rnk
    from Employee e
    join Department d
    on e.departmentId=d.id
)
select Department,
Employee,
salary
from ranksalary
where rnk<=3;