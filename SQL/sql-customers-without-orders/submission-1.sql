-- Write your query below
Select name
from customers
LEFT Join orders
    on customers.id=orders.customer_id
where orders.customer_id IS NULL
