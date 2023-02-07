import os.path
import math


if(os.path.isfile("overlap.dat") == False):
    print("tempereture.dat: No such file or directory.")   
    #exit(1)


with open ("overlap.dat",'r',encoding="utf8") as r_file:
    line_data = r_file.readlines()
    
    #close file
    r_file.close()
        

with open("unique.dat",'w',encoding="utf8") as w_file:
    unique_data = sorted(set(line_data))
    for i in unique_data:
        w_file.write(i)