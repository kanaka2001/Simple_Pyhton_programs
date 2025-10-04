def fibinocci (number):
    if number == 0:
        return number
    elif number == 1:
        return number
    else :
         return fibinocci(number-1) + fibinocci(number-2)
    
number_list = [1,2,3,4,5]
for index in number_list:
    result = fibinocci(index)
    print(result)

