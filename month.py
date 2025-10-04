def convertion_of_month_to_their_respective_month(month : int) -> str :
    match (month) :
        case 1 :
            return "jan"
        case 2 :
            return "feb"
        case 3:
            return "mar"
        case 4:
            return "apr"
        case 5 :
            return "may"
        case 6 :
            return "jun"
        case 7 :
            return "jul"
        case 8 :
            return "aug"
        case 9 :
            return "sep"
        case 10 :
            return "oct"
        case 11 :
            return "nov"
        case 12 :
            return "dec"
        
        case _:
            return "invalid month number"
month = 0      
month1 = 2        
month2 = 4        
month3 = 5        
month4 = 7        
month5 = 111        

print(convertion_of_month_to_their_respective_month(month))
print(convertion_of_month_to_their_respective_month(month1))
print(convertion_of_month_to_their_respective_month(month2))
print(convertion_of_month_to_their_respective_month(month3))
print(convertion_of_month_to_their_respective_month(month4))
print(convertion_of_month_to_their_respective_month(month5))


