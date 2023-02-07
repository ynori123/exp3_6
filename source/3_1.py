#うるう年判定

def main():
    x = int(input('西暦：'))
    if isLeapYear(x) :
        print("{0}年は「うるう年」です".format(x))
    else :
        print("{0}年は「平年」です".format(x))

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

main()