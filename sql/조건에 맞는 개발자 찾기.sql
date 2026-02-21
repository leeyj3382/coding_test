select d.id, d.email, d.first_name, d.last_name
from developers d
where (d.skill_code & (select code from skillcodes where name = 'python')) != 0
or (d.skill_code & (select code from skillcodes where name = 'c#')) != 0
order by d.id asc