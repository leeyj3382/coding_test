with recursive H as(
	select 0 as hour
	union all
	select hour + 1
	from H
	where hour < 23
)

select H.hour, count(o.animal_id) as count
from H
left join animal_outs o
on H.hour = hour(o.datetime)
group by H.hour
order by H.hour