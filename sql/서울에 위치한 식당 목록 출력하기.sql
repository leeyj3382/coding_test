select a.rest_id,
a. rest_name, 
a.food_type,
a.favorites,
a.address,
round(avg(review_score), 2) as score
from rest_info a
join rest_review b
on a.rest_id = b.rest_id
where address like '서울%'
group by a.rest_id, rest_name, favorites, address
order by score desc, favorites desc