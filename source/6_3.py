import numpy as np
import matplotlib.pyplot as plt

import os.path
import math
from collections import Counter



if(os.path.isfile("access.log") == False):
    print("access.log: No such file or directory.")   
    #exit(1)


with open ("access.log",'r',encoding="utf8") as r_file:
    line_data = r_file.readlines()
    #close file
    r_file.close()

def count_IP(line):
    IP_List = []
    for i in line:
        wordList = i.split()
        IP_List.append(wordList[0])
    l = Counter(IP_List)
    return l.most_common()


length = len(line_data)
ip,access_num = zip(*count_IP(line_data))
num = len(ip)

#print("アクセス数：{0}".format(length))
#print("アクセス元のIPアドレス数：{0}".format(num))
#print("攻撃元のIPアドレス：{0}".format(ip))

with open ("ip.csv",'w',encoding="utf8") as w_file:
    w_file.write("IP,Accessed\n")
    for i in count_IP(line_data):
        w_file.write("{0},{1}\n".format(i[0],i[1]))
    
    w_file.close()
 
left = ip
height = access_num
plt.bar(left, height, tick_label=ip, align="center")
plt.title("IP and Accessed number")
plt.xlabel("x ip")
plt.ylabel("y Accessed number")
plt.grid(True)
plt.show()