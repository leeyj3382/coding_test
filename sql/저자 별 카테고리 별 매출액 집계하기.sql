select a.author_id, a.author_name, b.category, sum(s.sales * b.price) as total_sales

from book_sales s
join book b
on s.book_id = b.book_id

join author a
on b.author_id = a.author_id

where month(s.sales_date) = 1
and year(s.sales_date) = 2022

group by a.author_id, b.category

order by a.author_id asc, b.category desc