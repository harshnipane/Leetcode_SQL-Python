# Write your MySQL query statement below
select 
ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
from(
   select d.*, 
row_number() over(partition by customer_id order by order_date ) rn
from Delivery d) x
where rn = 1;
