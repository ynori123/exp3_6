import os.path
import math

n = 0
total = 0.0
max = 0.0
min = 99.99
average = 0.0

if(os.path.isfile("tenperature.dat") == False):
    print("tempereture.dat: No such file or directory.")   
    exit(1)

with open ("temperature.dat",'r',encoding="utf8") as r_file:
    for line_data in r_file:
        daily_data = line_data.split()
        if daily_data[1] == "気温［℃］":
            continue
        temperature = float(daily_data[1])
        
        if min > temperature:
            min = temperature
            date2 = daily_data[0]

        if max < temperature:
            max = temperature
            date1 = daily_data[0]
        total += temperature
        n += 1

average = math.floor((total / n) * 1000) /1000

print("日時：", date1, ",最高気温：", max, "℃ , 平均気温：", average, "℃\n")

with open("average.dat",'w',encoding="utf8") as w_file:
    w_file.write("日時：{0},最低気温：{1} ℃,\n".format(date2,str(min)))
    w_file.write("日時：{0},最高気温：{1} ℃,\n".format(date1,str(max)))
    w_file.write("平均気温： {0}℃\n".format(str(average)))