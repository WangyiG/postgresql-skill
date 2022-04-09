import pandas as pd

df = pd.DataFrame({'id':[1,2],'value':['skls/32c,Msg/sms1,sms2,sms3,SKG/CD,FS','lv32/MDF,ddl/kds,dsf,dsf,bee/lpk,css']})

'''
1.?P<group_name>,命名组
2.+，*接？表示非贪婪模式，尽可能少的匹配
3.(?<=pattern)前向界定
4.(?=pattern)后向界定
5.^首，$尾
'''
df.set_index('id').value.str.extractall('(?P<阿强>\w+?(?=/))/(?P<阿珍>.+?(?=,\w+/|$))')


# 2次split转1次extractall,以逗号结束或结尾的整个看做1个大组,然后组内再去取date起始与结束,没有-的取出起始,结束补空
s = pd.Series(['02.07.2021 - 07.07.2021, 04.08.2021, 19.06.2021 - 21.06.2021','13.02.2021 - 15.02.2021, 03.03.2021'])
s.str.extractall('([\d\.]{10})[\s-]*([\d\.]+)*(?=,|$)')
