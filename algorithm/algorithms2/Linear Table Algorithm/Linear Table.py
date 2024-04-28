import sys
def main ():
    scores = [ 90 , 70 , 50 , 80 , 60 , 85 ]
    length = len( scores)
    for i in range( 0 , length):
        print ( scores[ i], "," , end= "" )
if __name__ == "__main__" :
    main()