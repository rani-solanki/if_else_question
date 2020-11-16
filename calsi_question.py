num_1=int(input("enter a number:"))
operator=input("enter any operator:")
num_2=int(input("enter another number:"))
if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1-num_2)
elif operator == "%":
    print(num_1 % num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
elif operator == "//":
    print(num_1 // num_2)
elif operator =="**":
    print(num_1 ** num_2)
else:
    print("invalidinput")