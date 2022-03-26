-- 数据集地址:https://tianchi.aliyun.com/dataset/dataDetail?dataId=649#1
-- 查看数据规模,结果为100150807条
SELECT COUNT(*) FROM taobaos;
-- 检查是否存在空值
SELECT * from taobaos WHERE user_id is NULL;
SELECT * from taobaos WHERE item_id is NULL;
SELECT * from taobaos WHERE category_id is NULL;
SELECT * from taobaos WHERE behavior_type is NULL;
SELECT * from taobaos WHERE timestamps is NULL;

-- 检查是否有重复值，结果为53条
SELECT user_id,item_id,timestamps from taobaos GROUP BY user_id,item_id,timestamps HAVING COUNT(*)>1;

-- 增加一列自增列方便后续去重,并检查是否增加成功
ALTER TABLE taobaos add COLUMN id bigserial primary key;
SELECT * from taobaos LIMIT 5;

-- 创建索引加速，去重，查看去重后数据规模，结果为100150754条记录
CREATE INDEX idx on taobaos(user_id,item_id,timestamps,id);

DELETE FROM taobaos WHERE id in 
(SELECT id FROM (SELECT ROW_NUMBER() OVER (PARTITION by user_id,item_id,timestamps ORDER BY id) as rn,
id from taobaos) t WHERE t.rn <> 1);

SELECT COUNT(*) FROM taobaos;

-- 新增列，由int类型的timestamps列生成timestamp类型的datetimes列，检查是否新增成功，该步耗时20分钟
ALTER TABLE taobaos ADD datetimes TIMESTAMP;
UPDATE taobaos set datetimes = to_timestamp(timestamps);
SELECT * from taobaos LIMIT 5;

-- 去除异常值
DELETE FROM taobaos WHERE datetimes < '2017-11-25 00:00:00' or datetimes > '2017-12-03 23:59:59';
SELECT COUNT(*) FROM taobaos;
