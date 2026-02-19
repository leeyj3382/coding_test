select count(id) as count
from ecoli_data
where (genotype &( 1 << 1)) = 0
and (genotype & (1 << 0)
or genotype & (1 << 2))