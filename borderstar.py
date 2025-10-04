def print_starsInBorder (matrixsize ):
    for row in range (1, matrixsize +1 ,1):
        for column in range (1, matrixsize +1 ,1):
            if (row ==1 or row ==matrixsize or column == 1 or column == matrixsize):
                print("* " , end = " ")
            
            else :
                print("  " ,end = " ")
        print("\n")

print_starsInBorder(4)
             