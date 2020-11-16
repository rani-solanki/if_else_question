salary=int(input("enter the number"))
year=int(input("enter the number"))
if year > 5:
    new_salary=salary*5/100
    net_salary=new_salary+salary
    print(net_salary,"new salry:",new_salary)
else:
    print("sorry it is smaller than 5")