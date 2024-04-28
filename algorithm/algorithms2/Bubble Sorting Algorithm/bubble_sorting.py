import sys

def sort(arrays):
    length = len(arrays)
    for i in range(0, length- 1):
        for j in range(0, length - i - 1):
            if arrays[j] > arrays[j + 1]:
                flag = arrays[j]
                arrays[j] = arrays[j + 1]
                arrays[j+1] = flag

def main():
    scores = [ 60 , 50 , 95 , 80 , 70 ]
    sort( scores)
    for score in scores:
        print ( score, "," , end= "" )

if __name__ == "__main__" :
    main()