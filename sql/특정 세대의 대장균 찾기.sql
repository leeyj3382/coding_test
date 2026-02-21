select c.id
from ecoli_data c
join ecoli_data p
on c.parent_id = p.id
join ecoli_data gp
on p.parent_id = gp.id

where gp.parent_id is null
order by id asc