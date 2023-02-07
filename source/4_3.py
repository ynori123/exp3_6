import os.path
import math

n = 0
total = 0.0
max = 0.0
min = 99.99
average = 0.0
map = {}

if(os.path.isfile("temperature.dat") == False):
    print("tempereture.dat: No such file or directory.")   
    #exit(1)


with open ("temperature.dat",'r',encoding="utf8") as r_file:
    for line_data in r_file:
        daily_data = line_data.split()
        if daily_data[1] == "気温［℃］":
            continue
        temperature = float(daily_data[1])

        map.setdefault(temperature, daily_data[0],)
        
        if min > temperature:
            min = temperature
            date2 = daily_data[0]

        if max < temperature:
            max = temperature
            date1 = daily_data[0]
        total += temperature
        n += 1

average = math.floor((total / n) * 1000) /1000

sortedDict = sorted(map.items())

with open ("temperature.dat",'w',encoding="utf8") as w_file:
    w_file.write("  年/月/日      気温［℃］\n")
    for i in sortedDict:
        w_file.write("{0} {1}\n".format(i[1],i[0]))
