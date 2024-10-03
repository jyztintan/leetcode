-- Write your PostgreSQL query statement below
SELECT u.unique_id, e.name
FROM employees e LEFT JOIN employeeUNI u ON u.id = e.id