# Write your MySQL query statement below
with comb1 as
(
    select requester_id as id , count(accepter_id) as numb from RequestAccepted
    group by requester_id 

    union all

    select accepter_id , count(requester_id) from RequestAccepted
    group by accepter_id 
)

select id , sum(numb) as num from comb1
group by id
order by num desc
limit 1