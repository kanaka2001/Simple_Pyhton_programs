#program1 addition of two numbers
'''
def sum_of_two_numbers(number1 :int , number2 : int) ->int : #defining a function with two arguments and return type
    return number1 + number2                                 # addition of two numbers

number1list = [1,2,3,4,5,6]                                  #list of numbers1
number2list = [4,5,6,7,8,9]                                  #list of numbers2 

for number in number1list:                                   #obtaining the all combinations on both lists
    for numbers in number2list:

        result =sum_of_two_numbers(number,numbers)           #assiging the result to a variable and printing
        print(result)
'''
#program2 SWAPING OF TWO NUMBERS

'''
def swaping_of_2_numbers(number1 :int, number2 : int ) :
    print(f"before swapping number values are number1 is {number1} and number2 {number2}")
    temp = number1 
    number1 = number2
    number2 = temp
    print(f"After swapping number values are number1 is {number1} and number2 {number2}")

number11 =int(input("Enter the first number :"))
number21 =int(input("Enter the second number :"))
swaping_of_2_numbers(number11,number21)
'''
#another unique technique
'''
def swap (num1 , num2) :
    temp = num1
    num1 = num2
    num2 = temp
    return num1 ,num2

number1 = 24
number2 = 30
print(f"{number1},{number2}")
element = swap(number1,number2)
print(f"{element}")
'''
#problem3 checking th number is even or odd
'''
def Odd_even_Check(number):
    if (number % 2 == 0):
        print(f"the given number {number} is even")
        #return True
    
    else:
        print(f"the given number {number} is odd")
        #return False
    

numbersList = [1,2,3,4,5,6,7,8,9,10]
for index in numbersList :
    Odd_even_Check(index)
    #result = Odd_even_Check(index)
    #print (result)
'''

#problem4  the entered number is integer checking

'''
def check_message(message) -> bool:
    if (message.isdigit()):
        return True
    else: 
        return False

messageinput = input("enter the message you are going to check :")
result = check_message(messageinput)
print(result)

'''
#problem5 simple input and giving the greetings

'''
def greetings(name) :
    print(f"good Mornng {name}")

name = input("enter your name :")
greetings(name)

def greeting(asdf) :
        print(f"good Mornng {name}")

name = input("Enter your name :")
greeting(name)

'''
#problem6 printing the ascii values of characters

'''
def returning_ASCII_value(character):
    for character in character :
        print(f"{character} -> {ord(character)}")

input = input ("enter the characters you neeed to caheck its ascci values :")
returning_ASCII_value(input)
'''

#Problem7 getting the length of the string

'''
def length_of_the_string(sting) :
    counter =0
    if sting != 'None:
        for character in sting :
            counter +=1 

    return counter

string = input("enter the message to calculate its length :")
result =length_of_the_string(string)
print(f"the length of {string} is {result}")

'''
#problem8 counting the number of vowels in a message/string

'''
def counting_vowels(message) :
    counter =0
    list = ['A','E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    
    for each_character in message :
         for index in list : 
            if (each_character == index): #instead of index also you give all the vowels with or for example each_character == 'a' or the other vowles
                counter +=1

            else :
                continue

    return counter

message = input("enter a message you need to check how many vowels are there in that the message :")
result = counting_vowels(message)
print(result)
'''

#problem9 reversing the string

def reversing_string(string) :
    last_element = len(string)-1
    reversed_string = ''
    for last_element in range(last_element , -1 , -1):
        reversed_string += string[last_element]

    return reversed_string


result =reversing_string("kanaka")
print(result)
