print("   |  1  2  3  4  5  6  7  8  9 ")
print("---+----------------------------")
for i in range(1,10):
    print(" {0} |".format(i),end='')
    for j in range(1,10):
        x = str(i * j) 
        
        print(x.rjust(3,' '),end = '')
    print("")