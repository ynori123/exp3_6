import datetime

 
def stringToTime(s) :
    #print(s.split('/'))
    x = [int(s) for s in (s.split(':'))]
    time = datetime.datetime(year=2000,month=1,day=1,hour=x[0],minute=x[1])
    return time


tm1 = stringToTime(input('開始時間(hh:mm):'))
tm2 = stringToTime(input('終了時間(hh:mm):'))

rslt = str(tm2 - tm1)
list = rslt.split(':')
print("経過時間：{0}時間{1}分".format(list[0],list[1]))