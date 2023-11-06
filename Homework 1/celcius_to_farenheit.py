

'''
This is a program to convert celcius to farenheit and vice versa
1. We get an input from the user about which option they want to choose: 1. C --> F, 2. F --> C
2. We will use the option to choose a formula and then we will get another input from the user as a float and convert
'''

while True:
    print('"ctrl + z" to exit the program')
    try:
        option = input('Choose "1" to convert Celcius to Farenheit or Choose "2" to convert Farenheit to Celcius: ')
        if int(option) == 1:
            celcius = float(input('Enter the temperature in celcius: '))
            farenheit = celcius * 1.8 + 32
            print(farenheit)

        elif int(option) == 2:
            farenheit = float(input('Enter the temperature in farenheit: '))
            celcius = (farenheit - 32) / 1.8
            print(celcius)

        else:
            continue

    except ValueError:
        continue