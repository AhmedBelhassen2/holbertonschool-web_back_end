CREATE TRIGGER `MyTrigger` 
    AFTER INSERT ON `products_in_order`
    FOR EACH ROW 
    BEGIN
      UPDATE products
           SET quantity = quantity-New.quantity
           WHERE product_code=New.product_code;
    END;