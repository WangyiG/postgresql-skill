-- 字符串连接
1.concat(str,...),忽略Null,返回'1122'
select concat(11,Null,22); 

2.concat_ws(sep,str,...),返回'11-22'
select concat_ws('-',11,Null,22);

3.||连接符,与concat类似,与concat的区别是连接的字符串中存在Null时,返回Null
select 11||Null||22;

-- 字符串长度,大小写与首字母大写
select length('apple');--5
select upper('apple');--'APPLE'
select lower('APPLE');--'apple'
select initcap('apple');--'Apple'

-- 字符串提取
1.substring(str[from m][for n])与substr(str,from m[,for n]),从第m个开始,总计返回n个字符,其中substr的参数位置决定无法省略from
select substring('Apple' for 3);--'App'
select substr('Apple',2,3);--'ppl'

2.left(str,n)与right(str,n),n支持负数,表示截除反向n个字符之后的所有字符
select left('Apple',2);--'Ap'
select left('Apple',-3);--'Ap'

-- 字符串匹配提取
1.substring(str from pattern),匹配提取posix正则表达式的子串(匹配第一个符合的就结束了)
select substring('apple,mday,1day,2day' from '\wday');--'mday'
select substring('apple,mday,1day,2day' from '\dday');--'1day'

2.regexp_match(str,pattern[,flags]),匹配提取posix正则表达式的子串(匹配第一个符合的就结束了),flags用于指定正则的标记修饰符,如i表示忽略大小写
select regexp_match('Mday,mday,1day,2day','m\w+');--'mday'
select regexp_match('Mday,mday,1day,2day','m\w+','i');--'Mday'

3.regexp_matches(str,pattern[,flags]),flags指定g时匹配所有符合的字串,返回形式是一个table形式,不指定g模式时,也是只匹配第一个
select regexp_matches('MDay,mday,1day,2Day','\wday','g');--table形式的'1day' '3day'
select regexp_matches('MDay,mday,1day,2Day','\wday','ig');--table形式的'1day' '2Day' '3day'

-- 返回字串的位置
1.position(substr in str)
select position('le' in 'apple');4

2.strpos(str,substr),注意参数位置与position的区别,子串在后
select strpos('apple','le');--4

-- 字符串替换
1.replace(str,from,to)
select replace('apple','le','');--'app'

2.regexp_replace(str,pattern,replacement[, flags]),正则替换
select regexp_replace('apple plan','p{2}','n');--'anle plan'

3.translate(str,from,to),批量替换,当from长度大于to时,匹配的部分执行替换,多出的部分执行删除
select translate('apple plan','ple','12');--'a112 12an',e没有匹配到,执行删除

4.overlay(str placing substr from [for]),覆盖替换,不必知道被替换的具体是什么,只需知道其位置即可
select overlay('apple plan' placing 'bb' from 2 for 3);--'abbe plan'

-- 截断与填充
1.trim,移除首尾指定字符,默认method为both,默认characters为空格
/*
trim([leading|trailing|both][characters]from str)
trim([leading|trailing|both][from] str [,characters]) -- from可有可无
btrim(str[,characters]),ltrim(str[,characters]),rtrim(str[,characters]) -- 对应method分别为both,leading,trailing
*/
select trim(' apple '),length(trim(' apple '));--'apple' 5
select trim(leading 'xyz' from 'xyappleyz');--'appleyz'
select trim(trailing 'xyappleyz','xyz');--'xyapple'
select rtrim('xyappleyz','xyz');--'xyapple'

2.lpad(str,length[,fill])与rpad(str,length[,fillvalue]),默认以空格填充,当length小于字符长度时会执行截断
select lpad('apple',7,'123');--'12apple',用不上3
select rpad('apple',4,'0');--'appl'而非'pple',注意当长度不够时,都是保留�得okd当ddf


















