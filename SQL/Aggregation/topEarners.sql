SELECT 
    salary * months AS earnings,
    COUNT(employee_id)
FROM employee
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;