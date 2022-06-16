-- 1.条件控制
DO $$
DECLARE
  i integer := 3;
  j integer := 3;
BEGIN 
  IF i > j THEN
    RAISE NOTICE 'i 大于 j';
  ELSIF i < j THEN
    RAISE NOTICE 'i 小于 j';
  ELSE
    RAISE NOTICE 'i 等于 j';
  END IF;
END $$;


DO $$
DECLARE
  i integer := 3;
BEGIN 
  CASE 
    WHEN i BETWEEN 0 AND 10 THEN
      RAISE NOTICE 'value is between zero and ten';
    WHEN i BETWEEN 11 AND 20 THEN
      RAISE NOTICE 'value is between eleven and twenty';
    ELSE
      RAISE NOTICE 'other value';
  END CASE;
END $$;


-- 2.循环语句
/*loop，exit when退出整个循环，continue when 跳出当前循环，继续下次循环*/
DO $$
DECLARE
  i integer := 0;
BEGIN 
  LOOP
    EXIT WHEN i = 5;
    i := i + 1;
    RAISE NOTICE 'Loop: %', i;
  END LOOP;
END $$;


DO $$
DECLARE
  i integer := 0;
BEGIN 
  LOOP
    EXIT WHEN i = 10;
    i := i + 1;
    CONTINUE WHEN mod(i, 2) = 1;
    RAISE NOTICE 'Loop: %', i;
  END LOOP;
END $$;


/*while*/
DO $$
DECLARE
  i integer := 0;
BEGIN 
  WHILE i < 5 LOOP
    i := i + 1;
    RAISE NOTICE 'Loop: %', i;
  END LOOP;
END $$;


/*
for
变量 i 不需要提前定义，可以在 FOR 循环内部使用
FOR target IN query LOOP语法：target 可以是一个 RECORD 变量、行变量或者逗号分隔的标量列表。在循环中，target 代表了每次遍历的行数据
*/
DO $$
BEGIN 
  FOR i IN 1..5 BY 2 LOOP
    RAISE NOTICE 'Loop: %', i;
  END LOOP;
END $$;

CREATE TABLE myta AS select * from (values(1,'test1'),(2,'test2'),(3,'test3')) as t(id, info)

DO $$
DECLARE
  r record;
BEGIN 
  FOR r IN (SELECT * FROM myta) LOOP
    RAISE NOTICE 'Loop: %,%', r.id, r.info;
  END LOOP;
END $$;


/*
FOREACH
FOREACH 循环与 FOR 循环类似，只不过变量的是一个数组
FOREACH target [ SLICE number ] IN ARRAY expression LOOP语法：
如果没有指定 SLICE 或者指定 SLICE 0，FOREACH 将会提取变量数组展开为1维的每个元素
如果指定了一个正整数的 SLICE，FOREACH 将会提取变量数组的子元素；SLICE 不能大于数组的维度
*/
DO $$
DECLARE
  x int;
BEGIN
  FOREACH x IN ARRAY (ARRAY[[1,2],[3,4],[5,6]])
  LOOP
    RAISE NOTICE 'x = %', x;
  END LOOP;
END $$;


DO $$
DECLARE
  -- 注意这里与上面不同
  x int[];
BEGIN
  FOREACH x SLICE 1 IN ARRAY (ARRAY[[1,2],[3,4],[5,6]])
  LOOP
    RAISE NOTICE 'x = %', x;
  END LOOP;
END $$;




















