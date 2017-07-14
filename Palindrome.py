# 1) Palindrome
# TASK 1: By-Arjun
# Enter a string to check if it is palindrome using a function.
# Write a function that takes string as input and returns if that string is palindrome or not

print ("What is the word you would like to check?")

def isPalindrome():
    word1 = input ('>')
    word2 = word1[::-1]
    if word1 == word2:
        print('%s is a palindrome'% word1)
    else:
        print("%s is not a palindrome!" %word1)
isPalindrome() 

