import sys


def money(salary):
    
    true_salary= salary - 5000 - salary * 0.165
    if true_salary < 0:
        tax = 0

    elif 0 < true_salary <= 3000:
        tax = true_salary * 0.03

    elif 3000 < true_salary <= 12000:
        tax = true_salary * 0.1 -210

    elif  12000 < true_salary <= 25000:
        tax = true_salary * 0.2 -1410
 
    elif  25000 < true_salary <= 35000:
        tax = true_salary * 0.25 -2660

    elif  35000 < true_salary <= 55000:
        tax = true_salary * 0.3 -4410

    elif  55000 < true_salary <= 80000:
        tax = true_salary * 0.35 -7160

    else:
        tax = true_salary * 0.45 -15160
    
    owner_salary = salary - tax - salary * 0.165
    
    return owner_salary


for arg in sys.argv[1:]:
    list = arg.split(":")
    try:
        result = money(int(list[1]))
        result_format = str(format(result,".2f"))
        print((list[0]+':'+result_format))
    except:
        print("parameter error")

