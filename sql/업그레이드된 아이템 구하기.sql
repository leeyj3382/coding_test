select i.item_id, i.item_name, i.rarity
from item_tree t
join item_info p
on p.item_id = t.parent_item_id
join item_info i
on i.item_id = t.item_id
where p.rarity = 'rare'
order by i.item_id desc