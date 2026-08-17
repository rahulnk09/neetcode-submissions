-- Write your query below
-- Select employee_id
-- From employees
-- where employee_id%2=0;

select employee_id,
    CASE
        when employee_id%2!=0 and name not like 'M%' then salary
        else 0
    END AS bonus
from employees
order by employee_id
