# Write your MySQL query statement below
select c.name as customers FROM 
customers c LEFT JOIN orders o
ON c.id=o.customerId
WHERE o.id is null;