-- PostgreSQL 11 增加了procedure关键字
/*
与自定义函数的区别主要有：
无返回值
通过call调用
以下示例拟更新产品的金额，低于60的更新为实际值，否则更新为60
*/

CREATE TABLE fruits(id int,name text,quantity int,price int , money int)
INSERT INTO fruits VALUES (1,'apple',10,6,0),(2,'orange',15,5,0),(3,'banana',12,4,0),(4,'peach',11,7,0)

CREATE OR REPLACE PROCEDURE update_fruits(max_money in integer)
AS $$
BEGIN
  -- min(max_money,quantity*price)
  update fruits set money = (case when max_money < quantity*price then max_money else quantity*price END);
END; 
$$ LANGUAGE plpgsql;

CALL update_fruits(60)

DROP PROCEDURE update_fruits

-- 简单的事务管理
create table test(a int);

CREATE PROCEDURE transaction_test()
LANGUAGE plpgsql
AS $$
BEGIN
    FOR i IN 0..9 LOOP
        INSERT INTO test (a) VALUES (i);
        IF i % 2 = 0 THEN
            COMMIT;
        ELSE
            ROLLBACK;
        END IF;
    END LOOP;
END
$$;

CALL transaction_test();
select * from test;






