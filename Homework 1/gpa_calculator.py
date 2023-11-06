from statistics import mean
'''
In this program we will 
1. Get 5 grades from user ranging between 0 and 20 then 
2. Calculate mean of the numbers
3. Print the GPA according to the mean.
'''
while True:
    print('"ctrl + z" to exit the program')
    
    grades = []
    try:
        for grade in range(5):
            grade = float(input("Enter a grade between 0 and 20: "))

            if grade < 0 or grade > 20:
                print("Invalid Grade")
                break
            else:
                grades.append(grade)

        if len(grades) < 5:
            print('Try Again!')
            continue
        else:        
            # mean_grade= mean(grades) This is one option to calculate MEAN
            mean_grade = sum(grades)/5

            if mean_grade <= 11.99:
                # print('Your GPA is: F')
                print('F')

            elif mean_grade >= 12 and mean_grade <= 14.99:
                # print('Your GPA is: C')
                print('C')

            elif mean_grade >= 15 and mean_grade <= 17.99:
                # print('Your GPA is: B')
                print('B')

            elif mean_grade >= 18:
                # print('Your GPA is: A')
                print('A')

    except ValueError:
        print('Invalid input. Try again!')
        continue
        
    