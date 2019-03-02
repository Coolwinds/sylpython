#!/usr/bin/python

import sys

try:
    salary = int(sys.argv[1]) 
except:
    print("Parameter Error")

true_salary = salary - 5000

if true_salary < 3000:
    tax = true_salary * 0.03
elif 3000 < true_salary < 12000:
    tax = true_salary * 0.1 - 210
elif 12000 < true_salary < 25000:
    tax = true_salary * 0.2 - 1410
elif 25000 < true_salary < 35000:
    tax = true_salary * 0.25 - 2660
elif 35000 < true_salary < 55000:
    tax = true_salary * 0.3 - 4410
elif 55000 < true_salary < 80000:
    tax = true_salary * 0.35 - 7160
else: 
    tax = true_salary * 0.45 - 15160
    
print(format(tax,".2f"))
