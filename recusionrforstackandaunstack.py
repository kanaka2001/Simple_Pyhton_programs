def recursion (number) :
    number = number -1
    print(f"first recursion {number}")
    if number >=0 :
        recursion(number)
        print(f"second recursion {number}")

result = recursion(5)