-- A SQL script that creates a trigger that decreases the
-- quantity of an item after adding a new order.
-- Quantity in the table items can be negative.
delimiter $$ ;
CREATE TRIGGER trace_orders AFTER INSERT ON orders
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - new.number
WHERE name = new.item_name;
END $$
delimiter ; $$
