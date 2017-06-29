 select
    IF( COUNT( a.Salary ) = 1, a.Salary, NULL ) as SecondHighestSalary
from (select distinct
            Salary
        from Employee
        order by Salary Desc limit 1 offset 1
    ) a
