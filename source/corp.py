#!/usr/local/bin/python3

import os.path
import re

FILE_NAME = "corporation.html"


if( os.path.isfile(FILE_NAME) == False ):
    print("File open error!")
    exit(1)

# 正規表現用
dict = {}
is_corp  = False
is_count = False
corp_name  = ""
corp_count = 0
r_begin_column = re.compile(r"\s*<TR")
r_end_column   = re.compile(r"\s*</TR")
r_corp_name    = re.compile(r"\s*<TD.*>(\D+)</TD>")
r_corp_count   = re.compile(r"\s*<TD.*>(\d+)</TD>")


# ファイルの読み込み p.24参照
with open(FILE_NAME, 'r') as r_file:
    for line in r_file:
        line.strip() # 改行コード削除
        if( r_begin_column.match(line) != None ):
            is_corp = True
            corp_count = 0
        elif( r_end_column.match(line) != None ):
            is_corp = False
            is_count = False
            if( corp_count > 0 ):
                dict[corp_name] = corp_count
        elif( is_corp and (r_corp_name.match(line) != None) ):
            corp_name = r_corp_name.match(line).group(1)
            is_count = True
        elif( is_corp and is_count and (r_corp_count.match(line) != None) ):
            corp_count += int(r_corp_count.match(line).group(1))

for key, value in sorted(dict.items(), key=lambda x:x[1]):
    print( key , value)



