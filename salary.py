basic_salary =eval(input("enter the value of basic salar"))
dearness_allowances =eval(input("enter the value of dearness_allowances"))
telephonoc_allowances =eval(input('enter the value of telephonoc_allowances'))
vehicle_allowances =eval(input("enter the value of vehicle_allowances"))
prominent_fund =eval(input("enter the value of prominent_fund"))
tax =eval(input("enter the value of tax)")
medical_insurance =eval(input("enter the value of medical_insurance"))
deduction=15/100(dearness_allowances+3/100(telephonoc_allowances))+10/100(medical_insurance)
gross_pay=basic_salary+dearness_allowances+telephonoc_allowances+vehicle_allowances
net_salry=gross_pay_deduction
print("gross pay is:",gross_pay)
print("total deduction is:",deduction)
print("net salry is:",net_salry)
