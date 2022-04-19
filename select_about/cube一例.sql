select * from abc

select
    coalesce(id, '小计' || date::text, '总计') id,
    coalesce(date::text, '小计' || id, '总计') date,
    COUNT(distinct new)
from 
	(select id,to_date(date,'dd/mm/yyyy') date,unnest(string_to_array(concat_ws('-', "from", "to"), '-')) new from abc) t
group by
    CUBE(id, date)
order BY
    id,date
