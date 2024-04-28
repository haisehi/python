import sys
def sort ( arrays):
    length = len( arrays) - 1
    min_index = 0 # the index of the selected minimum
    for i in range( 0 , length):
        min_index = i
        # the minimum value of each loop as the first element
        min_value = arrays[ min_index]
        for j in range( i, length):
        # Compare with each element if it is less than the minimum value, exchange the min_index
            if min_value > arrays[ j + 1 ]:
                min_value = arrays[ j + 1 ]
                min_index = j + 1
        # if the minimum index changes, the current minimum is exchanged with the min_index
        if i != min_index:
            temp = arrays[ i]
            arrays[ i] = arrays[ min_index]
            arrays[ min_index] = temp
def main ():
    scores = [ 60 , 80 , 95 , 50 , 70 ]
    sort( scores)
    for score in scores:
        print ( score, "," , end= "" )
if __name__ == "__main__" :
    main()