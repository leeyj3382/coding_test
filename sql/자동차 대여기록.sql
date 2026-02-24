select car_id,
case when sum(case when end_date >= '2022-10-16' and start_date <= '2022-10-16' then 1 else 0 end)
> 0 then '대여중'
else '대여 가능' end as availability
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc