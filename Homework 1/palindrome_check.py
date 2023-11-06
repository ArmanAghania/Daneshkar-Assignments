

# We are going to get a string as an input and decide if the string is palindrome or not.
# Palindrome is a word that is the same when read from the front and from the back.

# Example: "radar" --> Palindrome
while True:
    word = input('Enter a word to check if it is a palindrome or not: ').lower()
    
    if word == word[::-1]: # [::-1] is used to reverse the string
        print('Yes')
    else:
        print('No')

    print('"ctrl + z" to exit the program')