
'''
We are going to get two inputs from user:
    1. A long text
    2. A single word 

    And then we will search the text to count how many times the word appears in the text.
''' 
while True:
    text = input("Enter a long text: ").lower()
    word = input("Enter a word: ").lower()

    print(text.count(word))

    print('"ctrl + z" to exit the program')