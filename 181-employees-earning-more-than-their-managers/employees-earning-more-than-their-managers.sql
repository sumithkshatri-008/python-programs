# Write your MySQL query statement below
select e.name as employee from
employee e
join 
employee m
on m.id=e.managerId
WHERE e.salary>m.salary; 