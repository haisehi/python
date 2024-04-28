import sys

def minimum(arrays):
    minIndex = 0
    length = len(arrays) - 1
    for i in range(0, length):
        if (arrays[minIndex] > arrays[i]):
            minIndex = i
    return arrays[minIndex]
def main():
    scores = [ 60 , 80 , 95 , 50 , 70 ]
    minValue = minimum( scores)
    print ( "Min Value = " , minValue)
if __name__ == "__main__":
    main()