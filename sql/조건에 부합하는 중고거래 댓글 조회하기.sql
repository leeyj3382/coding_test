select a.TITLE,
a.BOARD_ID,
b.REPLY_ID,
b.WRITER_ID,
b.CONTENTS,
date_format(b.created_date, '%Y-%m-%d') as CREATED_DATE
from used_goods_board a
join used_goods_reply b
on a.board_id = b.board_id
where  year(a.created_date) = 2022
and month(a.created_date) = 10
order by b.created_date asc, a.title asc