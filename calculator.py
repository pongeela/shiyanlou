#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:

    salary_input = int(sys.argv[1])
 
else:
     print('PARAMETER ERROR')

if salary_input <=3500:
    tax = 0
    print(format(tax,".2f"))

else:

    social_ins = 0
    tax_salary = salary_input - social_ins - 3500

    if tax_salary <= 1500:
        tax = tax_salary * 0.03 - 0

    elif 1500 < tax_salary <= 4500:
        tax = tax_salary * 0.1 - 105

    elif 4500 < tax_salary <= 9000:
        tax = tax_salary * 0.2 - 555

    elif 9000 < tax_salary <= 35000:
        tax = tax_salary * 0.25 -1005

    elif 35000 < tax_salary <= 55000:
        tax = tax_salary * 0.3 - 2755

    elif 55000 < tax_salary <= 80000:
        tax = tax_salary * 0.35 - 5505

    elif tax_salary > 80000:
        tax = tax_salary * 0.45 - 13505

    print(format(tax,".2f"))



