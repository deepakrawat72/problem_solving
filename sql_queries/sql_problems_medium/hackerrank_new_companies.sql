--https://www.hackerrank.com/challenges/the-company/problem
CREATE TABLE company (
company_code varchar(10),
founder varchar(20)
);

CREATE TABLE lead_manager (
lead_manager_code varchar(10),
company_code varchar(10)
);

CREATE TABLE senior_manager (
senior_manager_code varchar(10),
lead_manager_code varchar(10),
company_code varchar(10)
);

CREATE TABLE manager (
manager_code varchar(10),
senior_manager_code varchar(10),
lead_manager_code varchar(10),
company_code varchar(10)
);

CREATE TABLE employee (
employee_code varchar(10),
manager_code varchar(10),
senior_manager_code varchar(10),
lead_manager_code varchar(10),
company_code varchar(10)
);


insert into company(company_code, founder) values('C1', 'Monika');
insert into company(company_code, founder) values('C2', 'Samantha');

insert into lead_manager(company_code, lead_manager_code) values('C1', 'LM1');
insert into lead_manager(company_code, lead_manager_code) values('C2', 'LM2');

insert into senior_manager(company_code, lead_manager_code, senior_manager_code) values('C1', 'LM1', 'SM1');
insert into senior_manager(company_code, lead_manager_code, senior_manager_code) values('C1', 'LM1', 'SM2');
insert into senior_manager(company_code, lead_manager_code, senior_manager_code) values('C2', 'LM2', 'SM3');

insert into manager(company_code, lead_manager_code, senior_manager_code, manager_code) values('C1', 'LM1', 'SM1', 'M1');
insert into manager(company_code, lead_manager_code, senior_manager_code, manager_code) values('C2', 'LM2', 'SM3', 'M2');
insert into manager(company_code, lead_manager_code, senior_manager_code, manager_code) values('C2', 'LM2', 'SM3', 'M3');

insert into employee(company_code, lead_manager_code, senior_manager_code, manager_code, employee_code) values('C1', 'LM1', 'SM1', 'M1', 'E1');
insert into employee(company_code, lead_manager_code, senior_manager_code, manager_code, employee_code) values('C1', 'LM1', 'SM1', 'M1', 'E2');
insert into employee(company_code, lead_manager_code, senior_manager_code, manager_code, employee_code) values('C2', 'LM2', 'SM3', 'M2', 'E3');
insert into employee(company_code, lead_manager_code, senior_manager_code, manager_code, employee_code) values('C2', 'LM2', 'SM3', 'M3', 'E4');

select
    company_code
  , founder
  , COUNT(DISTINCT lead_manager_code) as l_m_count
  , COUNT(DISTINCT senior_manager_code) as l_m_count
  , COUNT(DISTINCT manager_code) as l_m_count
  , COUNT(DISTINCT employee_code) as l_m_count
FROM (
select c.company_code, c.founder, l.lead_manager_code, s.senior_manager_code, m.manager_code, e.employee_code
from company c
join lead_manager l
on c.company_code = l.company_code
join senior_manager s
on c.company_code = s.company_code
join manager m
on c.company_code = m.company_code
join employee e
on c.company_code = e.company_code
) x group by company_code, founder
order by company_code asc