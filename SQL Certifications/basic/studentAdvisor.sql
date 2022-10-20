SELECT ROLL_NUMBER, NAME
FROM STUDENT_INFORMATION a
JOIN FACULTY_INFORMATION b
ON a.ADVISOR = b.EMPLOYEE_ID
WHERE (GENDER = 'M' AND SALARY > 15000) OR 
(GENDER = 'F' AND SALARY > 20000);