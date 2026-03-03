select year(o.sales_date) as YEAR, month(o.sales_date) as MONTH, u.GENDER as GENDER,
count(distinct o.user_id) as USERS
from online_sale o
join user_info u
on o.user_id = u.user_id
where u.gender is not null
group by year(o.sales_date), month(o.sales_date), u.gender
order by YEAR asc, MONTH asc, u.gender asc