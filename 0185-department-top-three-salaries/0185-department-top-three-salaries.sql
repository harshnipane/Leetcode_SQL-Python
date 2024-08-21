# Write your MySQL query statement below
with Emp_dept as
(
    select e.id , e.name, e.salary, e.departmentId , d.name as dept_name from Employee e join Department d on e.departmentId = d.id
)

select dept_name as Department, name as Employee, salary as Salary from
(
    select *, dense_rank() over( partition by departmentId order by salary desc) as dr from Emp_dept
) e

where e.dr < 4