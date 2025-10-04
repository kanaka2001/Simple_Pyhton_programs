def starPramid(height):
    
    for row in range (1, height + 1, 1):
        num_spaces = height - row 
        noOfStars = 2*row -1
        print(" " * num_spaces , noOfStars * "*"  )
starPramid(3)