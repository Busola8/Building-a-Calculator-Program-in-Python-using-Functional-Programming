# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:50:40 2023

@author: deji
"""

def add(a,b):
    return(a+b)
    
def subtract(b,c):
    return(b - c)
    
def multiply(d,e):
    return(d*e)
    
def divide(f,g):
    return(f/g)
    
operations = {'+':add, '-':subtract, '*':multiply, '/':divide}


num1 = int(input('enter the first number: '))
num2 = int(input('enter second number: '))
while True:
    while True:
        operation_symbol = input('select an operation symbol: \nto add - "+"\nto subtract - "-"\nto divide - "/"\nto multiply - "*"\nresponse: ')
        if operation_symbol == '+' or operation_symbol =='-' or operation_symbol == '/' or operation_symbol == '*':
            answer = operations[operation_symbol](num1,num2)
            print('\nnum1 + num2 = ',answer)
            break
        else:
            print('\nsymbol not in list')
                                
    
    switch = False
    while True:
        
        should_continue = int(input('would you like to use answer as first number to continue? \npress 0: exit \npress 1: yes\npress 2: no\nresponse: '))   
        if should_continue == 1:
            num1 = answer
            num2 = int(input('enter second number: '))
            break
        elif should_continue == 2:
            num1 = int(input('enter the first number: '))
            num2 = int(input('enter second number: '))
            break
        elif should_continue == 0:
            switch = True
            break
        else: 
            print('make the right choice')
    
    if switch == True:
        break