import sys

def sort(arrays):
    length = len(arrays) -1
    minIndex = 0
    for i in range(0, length):
        minIndex = i
        minValue = arrays[minIndex]
        for j in range(i, length):
            if minValue > arrays[j+1]:
                minValue = arrays[j+1]
                minIndex = j+1
        if i!= minIndex:
            temp = arrays[i]
            arrays[i] = arrays[minIndex]
            arrays[minIndex] = temp


def main():
    scores = [60,50,95,80,70]
    sort(scores)
    for score in scores:
        print(score)

if __name__ == '__main__':
    main()