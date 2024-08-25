# Write your MySQL query statement below
with comb as
(
    select mr.movie_id, title, mr.user_id, name, rating, created_at from Movies m join MovieRating mr on m.movie_id = mr.movie_id join Users u on mr.user_id = u.user_id
)

select name as results from(
select name, count(rating) as rate from comb 
group by user_id 
order by rate desc, name
limit 1) a

UNION ALL

select title from 
(select title , avg(rating) as high
from comb
where date_format(created_at, '%Y-%m') = '2020-02'
group by title
order by high desc, title
limit 1
) b
