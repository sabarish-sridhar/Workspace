# Write your MySQL query statement below




Select sell_date,count( distinct product) as num_sold, group_concat( Distinct product order by product ASC) as products
from activities
group by sell_date;
