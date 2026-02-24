select food_type, rest_id , rest_name, favorites
from(
    select *,
            rank() over(partition by food_type order by favorites desc) as rnk
    from rest_info
) t
where rnk = 1
order by food_type desc