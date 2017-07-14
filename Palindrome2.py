# Palindrome2 
# TASK 2: By Arjun
# Function that takes array of strings as input and returns list of strings and 
#its lengths which are palindrome

words = [i for i in input().split()]

def isPalindrome(words):
    if list(words) == list(reversed(words)):
        print('%s is a palindrome'% words)
        print('The length of the word- "%s" is'% words,len(words))
    else:
        print("%s is not a palindrome!" %words)

for i in words:
    isPalindrome(i)