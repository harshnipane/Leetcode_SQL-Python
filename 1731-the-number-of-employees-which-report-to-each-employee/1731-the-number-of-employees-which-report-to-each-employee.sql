# Write your MySQL query statement below
select m.employee_id, m.name, COUNT(e.reports_to) as reports_count,
    ROUND(AVG(e.age * 1.0), 0) as average_age
from Employees e join Employees m ON e.reports_to = m.employee_id
group by m.employee_id,
    m.name
order by m.employee_id