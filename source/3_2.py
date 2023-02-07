import datetime

 
def stringToDate(s) :
    #print(s.split('/'))
    x = [int(s) for s in (s.split('/'))]
    date = datetime.datetime(year=x[0],month=x[1],day=x[2])
    return date


dt1 = stringToDate(input('開始日(yyyy/mm/dd):'))
dt2 = stringToDate(input('終了日(yyyy/mm/dd):'))

rslt = str(dt2 - dt1)
list = rslt.split(',')
print("日数差：{0}".format(list[0]))