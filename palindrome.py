word =input("enter the word to check the palindrome :")

rightindex = 0
leftindex = len(word) -1
if (word[rightindex] == word[leftindex]):
    print(f"given {word} is palindrome")
else:
    print(f"given {word} is not palindrome")