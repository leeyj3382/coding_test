select p.id, count(c.id) as child_count
from ecoli_data p
left join ecoli_data c

on c.parent_id = p.id
group by p.id