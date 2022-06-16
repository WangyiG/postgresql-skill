-- 1，类似pd里axis=0
drop FUNCTION myfunc

CREATE OR REPLACE FUNCTION myfunc(in int ) RETURNS int AS  
$BODY$  
DECLARE  
    r int := 0;  
    res int := 0;
BEGIN  
    FOR r IN  
        select m from generate_series(1,$1) as m
    LOOP  
        res = res+r; 
    END LOOP;  
    RETURN res;  
END  
$BODY$  
LANGUAGE plpgsql;


select m,myfunc(m) from generate_series(1,10) as m


-- 2.定义一个接收array参数的mysum存储过程，再把列array_agg转成array，给mysum去调用
CREATE TABLE foo (fooid INT, foosubid INT, fooname TEXT);  
INSERT INTO foo VALUES (1, 2, 'three');  
INSERT INTO foo VALUES (4, 5, 'six'); 


CREATE FUNCTION mysum(int[]) RETURNS int8 AS $$  
DECLARE  
  s int8 := 0;  
  x int;  
BEGIN  
  FOREACH x IN ARRAY $1  
  LOOP  
    s := s + x;  
  END LOOP;  
  RETURN s;  
END;  
$$ LANGUAGE plpgsql;

SELECT mysum(ARRAY_AGG(fooid)) from foo;







