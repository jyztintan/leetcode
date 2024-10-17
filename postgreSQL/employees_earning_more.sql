SELECT e.name AS Employee
FROM employee e, employee e1
WHERE e.managerId = e1.id
AND e.salary > e1.salary
