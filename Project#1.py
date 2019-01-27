from random import *
from math import sqrt
import time

print()
print('Program#1')
print()


# Program_1
def removeConjunction(sentence):
    conjunction = {'and', 'by', 'in', 'of', 'on'}
    text = ''
    for word in sentence.split(' '):
        if word not in conjunction:
            text += word + ' '
    return text[:-1]


def findAcronym(sentence):
    acronym = ''
    acronym += sentence[0]
    for index in range(len(sentence)):
        if sentence[index] == ' ':
            acronym += sentence[index + 1]

    return acronym


print("Enter a sentence: ")
keyboard = str(input()).lower()

newText = removeConjunction(keyboard)

print(findAcronym(newText).upper())
print()

'''



Test1:

        Enter a sentence: 
        North Atlantic Treaty Organization
        NATO
        
        Process finished with exit code 0
    
Test2:

        Enter a sentence: 
        light amplification by stimulated emission of radiation
        LASER
        
        Process finished with exit code 0
        
Test3:

        Enter a sentence: 
        Central Intelligence Agency
        CIA
        
        Process finished with exit code 0
        
Test:4

        Enter a sentence: 
        National Security Agency
        NSA
        
        Process finished with exit code 0



'''

print('Program#2')
print()


# Program#2
def isPerfectNumber(number):
    arr = [number]
    total = 0
    for i in range(1, number):
        num = int(number % i)
        if num == 0:
            arr.append(i)
            total += i
            if total == number:
                for value in arr:
                    if value != number:
                        print(value)
                print('%d is a perfect number' % number)
                return True

    print('%d is not a perfect number' % number)
    return False


isPerfectNumber(496)

'''


Test1:

        1
        2
        3
        6 is a perfect number

        Process finished with exit code 0

Test2:

        1
        2
        4
        7
        14
        28 is a perfect number

        Process finished with exit code 0

Test3:

        325 is not a perfect number

        Process finished with exit code 0

Test4:

        1
        2
        4
        8
        16
        31
        62
        124
        248
        496 is a perfect number

        Process finished with exit code 0



'''

print()
print("Program#3")
print()


# Program#3
def monteCarloSim(n):
    m = 0
    for i in range(0, n):
        x = random()
        y = random()
        if sqrt(x * x + y * y) <= 1:
            m += 1
    pi = 4 * m / n
    print('n = %d' % n)
    print('Time = ', time.time())
    print('Pi value = ', pi)


monteCarloSim(10000)

'''


Test1: 

        n = 100
        Time =  1506965735.343974
        Pi value =  3.2

        Process finished with exit code 0

Test2: 

        n = 1000
        Time =  1506965784.233778
        Pi value =  3.104

        Process finished with exit code 0

Test3:

        n = 10000
        Time =  1506965812.8223865
        Pi value =  3.1528

        Process finished with exit code 0


'''
