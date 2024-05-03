# Write your MySQL query statement below

 #   select w1.id
#from Weather w1, Weather w2
#where (w1.Temperature > w2.Temperature and 
#	datediff(w1.recordDate, w2.recordDate) = 1)

select id 
from 
(select id, 
case 
when datediff(recordDate,lag(recordDate) over(order by recordDate)) = 1 and lag(temperature) over(order by recordDate) < temperature then 'yes'
else 'no'
end as temp
from Weather) e
where e.temp = 'yes'
    





