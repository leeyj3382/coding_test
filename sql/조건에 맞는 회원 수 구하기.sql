select count(user_id) as users
from user_info
where year(joined) = 2021
and age >= 20
and 29 >= age