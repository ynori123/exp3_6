
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

def isSQLattacked(line):
    ip_list = []
    for i in line:
        wordlist = i.split(" ")
        for j in wordlist:
            if(j.count('%27') > 0):
                ip_list.append(wordlist[0])
    return ip_list

length = len(line_data)
ip,access_num = zip(*count_IP(line_data))
ip = set(ip)
num = len(ip)
sql_ip = isSQLattacked(line_data)
sql_ip = sorted(set(sql_ip))

print("アクセス数：{0}".format(length))
print("アクセス元のIPアドレス数：{0}".format(num))
print("攻撃元のIPアドレス：{0}".format(ip))
print("SQLコマンドインジェクションを行っていると思われるIPアドレス：{0}".format(sql_ip))
    