# Write your MySQL query statement below
select p.firstname,p.lastname,a.city,a.state
FROM person p LEFT JOIN address a
ON p.personId = a.personId;