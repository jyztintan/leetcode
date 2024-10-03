SELECT name
FROM employee e1,
    (
    SELECT managerId, COUNT(managerId) as reports
    FROM employee e2
    GROUP BY managerId
    ) sub
WHERE e1.id = sub.managerid
AND sub.reports >= 5