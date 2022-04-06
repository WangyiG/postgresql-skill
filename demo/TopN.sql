-- 统计点击，加购物车，下单，付款分别最多的5种产品id

/*正常写,为了命中索引，采用了union的写法，耗时6秒*/
-- 创建索引
DROP INDEX i0

CREATE INDEX i0 ON tbao(behavior_type,item_id,user_id)

-- 查看执行情况
EXPLAIN(ANALYZE,TiMING) SELECT behavior_type,item_id,COUNT(*) FROM tbao where behavior_type ='pv' GROUP BY behavior_type,item_id ORDER BY COUNT(*) DESC LIMIT 5;

-- 返回结果
(SELECT behavior_type,item_id,COUNT(*) FROM tbao where behavior_type ='buy' GROUP BY behavior_type,item_id ORDER BY COUNT(*) DESC LIMIT 5)
UNION ALL
(SELECT behavior_type,item_id,COUNT(*) FROM tbao where behavior_type ='cart' GROUP BY behavior_type,item_id ORDER BY COUNT(*) DESC LIMIT 5)
UNION ALL
(SELECT behavior_type,item_id,COUNT(*) FROM tbao where behavior_type ='fav' GROUP BY behavior_type,item_id ORDER BY COUNT(*) DESC LIMIT 5)
UNION ALL
(SELECT behavior_type,item_id,COUNT(*) FROM tbao where behavior_type ='pv' GROUP BY behavior_type,item_id ORDER BY COUNT(*) DESC LIMIT 5);

/*topN插件，耗时20毫秒，注意topn_add_agg(x:test),topn(x,n),topn_union_agg(agg)函数的使用*/


-- 创建一个汇总表test,该表存放的是每个behavior_type对应的item_id:count哈希数组jsonb，得益于postgres对数组的友好支持，该步比创建索引快

DROP TABLE test  

CREATE TABLE test(behavior_type TEXT,agg jsonb);

INSERT INTO test
SELECT behavior_type,topn_add_agg(item_id::text)  
FROM tbao GROUP BY behavior_type;

-- 返回结果
SELECT behavior_type,(topn(topn_union_agg(agg),5)).* FROM test GROUP BY behavior_type ORDER BY behavior_type;



