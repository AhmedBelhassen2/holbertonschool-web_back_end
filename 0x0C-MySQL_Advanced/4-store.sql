-- Make a trigger to buy item
CREATE TRIGGER DeleteQuantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items 
    SET quantity = quantity - NEW.number
    WHERE NEW.item_name = name
END;