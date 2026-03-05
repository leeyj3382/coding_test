select c.car_id,
    c.car_type,
    ROUND(c.daily_fee * 30 * (100 - p.discount_rate) / 100) AS fee
from car_rental_company_car c
join car_rental_company_discount_plan p
on c.car_type = p.car_type
and p.duration_type = '30일 이상'
where c.car_type in ('suv', '세단')
and c.car_id not in(
    select car_id
    from car_rental_company_rental_history
    where start_date <= '2022-11-30'
    and end_date >= '2022-11-01')
and c.daily_fee * 30 *(100 - p.discount_rate) / 100 between 500000 and 2000000

ORDER BY fee DESC, c.car_type ASC, c.car_id DESC;