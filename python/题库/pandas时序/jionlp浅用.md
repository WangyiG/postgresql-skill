```py
import arrow
from jionlp import parse_time 

texts = [
    '2001-01-15 12:22:00',
    '2010年4月27日5点28分08秒',
    '20190122134528',
    '2018年7月17日15点03分02秒',
    '2022/03/06 17:42:15'
]

fmts = [
    '%Y-%m-%d %H:%M:%S',
    '%Y年%m月%d日%H点%M分%S秒',
    '%Y%m%d%H%M%S',
    '%Y年%m月%d日%H点%M分%S秒',
    '%Y/%m/%d %H:%M:%S',
]

class Ans:
    def __init__(self,texts):
        self.texts = texts
        self.v = list(map(self.parse,self.texts))

    @staticmethod
    def parse(text):
        try:
            dt = arrow.get(parse_time(text)['time'][0])
        except:
            dt = arrow.get(text,'YYYYMMDDHHmmss')
        return text,dt

    def get_max(self):
        max_str,max_time = max(self.v,key=lambda x:x[1])
        min_str,min_time = min(self.v,key=lambda x:x[1])
        return {'原始时间字符':[max_str,min_str],'时间差(秒)':(max_time-min_time).total_seconds()}

Ans(texts).get_max()
```
