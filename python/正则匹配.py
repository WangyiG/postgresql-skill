import pandas as pd

'''
1.?P<group_name>,命名组
2.+，*接？表示非贪婪模式，尽可能少的匹配
3.(?<=pattern)前向界定,前向否定(?<!pattern)，注意前向中不可使用\d等正则表达式
4.(?=pattern)后向界定,后向否定(?！pattern)
5.^首，$尾
6.无捕获组(?:pattern),无捕获组的使用偏向把确定能匹配的放前面,不确定的放无捕获组内,如题3对比
7.有编号组n的使用,首先匹配应该是组的形式,然后才能r'\n'调用,这里r不能省
'''

# /前面的为1组开头,后面直至另一组开头为1组
df = pd.DataFrame({'id':[1,2],'value':['skls/32c,Msg/sms1,sms2,sms3,SKG/CD,FS','lv32/MDF,ddl/kds,dsf,dsf,bee/lpk,css']})
df.set_index('id').value.str.extractall('(?P<阿强>\w+?(?=/))/(?P<阿珍>.+?(?=,\w+/|$))')


# 2次split转1次extractall,以逗号结束或结尾的整个看做1个大组,然后组内再去取date起始与结束,没有-的取出起始,结束补空
s = pd.Series(['02.07.2021 - 07.07.2021, 04.08.2021, 19.06.2021 - 21.06.2021','13.02.2021 - 15.02.2021, 03.03.2021'])
s.str.extractall('([\d\.]{10})[\s-]*([\d\.]+)*(?=,|$)')


# 有2个匹配的切分出来,不足部分再单独切分出来
s = pd.Series(['add tss czz qty', 'fss esc mdk', 'ssl .str.extractall('(\w+\s\w+|\w+$)').droplevel(1)mny tc fkl dek', 'mq'])
s.str.extractall('(\w+(?:\s\w+)?)').droplevel(1)
s.str.extractall('(\w+\s\w+|\w+$)').droplevel(1)


# 注意这里replace使用了组的形式,然后才能被r'\1'调用
pd.Series(['ab-cd','ab-ab']).str.extract(r'(\w+)-\1')
S = pd.Series(['ab,cd','efg-h'],name='A')
S.str.replace('(\w+)',S.name+r'\1',regex=True)



