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
