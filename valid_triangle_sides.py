side_1=int(input("enter a side length:"))
side_2=int(input("enter another szide lenght:"))
side_3=int(input("enter one more side lenght:"))
if side_1 + side_2 > side_3:
    print("its valid")
elif side_2 + side_3 > side_1:
    print("itsb valid")
elif side_3 + side_2 > side_1:
    print("its valid")
else:
    print("its invalid")