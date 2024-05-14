def sort ( array):
    length = len( array)
    if length > 0 :
        quick_sort( array, 0 , length - 1 )
def quick_sort ( array, low, high):
    if low > high :
        return
    i = low
    j = high
    threshold = array[ low]
    # Alternately scanned from both ends of the list
    while i < j:
        # Find the first position less than threshold from right to left
        while i < j and array[ j] > threshold:
            j-= 1
            #Replace the low with a smaller number than the threshold
        if i < j:
            array[ i] = array[ j]
            i+= 1
                # Find the first position greater than threshold from left to right
        while i < j and array[ i] <= threshold:
            i+= 1
            # Replace the high with a number larger than the threshold
            if i < j:
                array[ j] = array[ i]
                j-= 1
        array[ i] = threshold
        # left quick_sort
        quick_sort( array, low, i - 1 )
        # right quick_sort
        quick_sort( array, i + 1 , high)
def main ():
    scores = [ 90 , 60 , 50 , 80 , 70 , 100 ]
    sort( scores)
    for score in scores:
        print ( score, "," , end= "" )
if __name__ == "__main__" :
    main()