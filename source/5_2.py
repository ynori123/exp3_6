import os.path
import math

def count_word(str):
    line_word = len(str.split())
    return line_word

def count_char(str):
    line_char = len(str)
    line_char -= (count_word(str) - 1)
    return line_char

def num_line(file_name):
    if(os.path.isfile(file_name) == False):
        print(file_name + ": No such file or directory.")   
        #exit(1)


    with open (file_name,'r',encoding="utf8") as r_file:
        line_data = r_file.readlines()
        
        #close file
        r_file.close()

    lines = len(line_data)
    words = 0
    char = 0
    for i in line_data:
        words += count_word(i)

    for i in line_data:
        char += count_char(i)

    return lines

def num_words(file_name):
    if(os.path.isfile(file_name) == False):
        print(file_name + ": No such file or directory.")   
        #exit(1)


    with open (file_name,'r',encoding="utf8") as r_file:
        line_data = r_file.readlines()
        
        #close file
        r_file.close()

    lines = len(line_data)
    words = 0
    char = 0
    for i in line_data:
        # 改行をエスケープ
        words += (count_word(i)) - 1

    for i in line_data:
        char += count_char(i)
    
    return words

def num_char(file_name):
    if(os.path.isfile(file_name) == False):
        print(file_name + ": No such file or directory.")   
        #exit(1)


    with open (file_name,'r',encoding="utf8") as r_file:
        line_data = r_file.readlines()
        
        #close file
        r_file.close()

    lines = len(line_data)
    words = 0
    char = 0
    for i in line_data:
        
        words += count_word(i)

    for i in line_data:
        char += count_char(i)
    
    return char



with open("wc.txt",'w',encoding="utf8") as w_file:
    fileList = ["overlap.dat", "unique.dat"]
    for i in fileList:
        w_file.write("{0}:  {1}文字，{2}語，{3}行\n".format(i, num_char(i), num_words(i), num_line(i)))
        print("{0}:  {1}文字，{2}語，{3}行\n".format(i, num_char(i), num_words(i), num_line(i)))
    
    w_file.close()