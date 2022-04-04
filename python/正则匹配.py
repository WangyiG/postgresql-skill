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
