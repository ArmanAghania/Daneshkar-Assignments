
'''
In this program we will try to choose the maximum number among multiple numbers and the trick to it is "WE CAN NOT USE MAX()"
1. Get 3 numbers from user
2. Calculate the maximum number
'''
while True:
    try:
        
        numbers = []
        for number in range(3):
            number = float(input("Enter a number: "))
            numbers.append(number)
            print(numbers)

        max_number = 0
        for number in numbers:
            if number > max_number:
                max_number = number
            
        print(max_number)
        print('"ctrl + z" to exit the program')
    
    except ValueError:
        print('Invalid Input, Try Again!!')
        continue