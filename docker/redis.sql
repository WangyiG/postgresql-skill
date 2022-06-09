# docker exec -it xxx bash进入redis命令模式
redis-cli
# docker给redic设置的用户是redispw
auth redispw

set test ‘abc’
keys *
