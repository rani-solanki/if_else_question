side_1=int(input("enter a side lenght:"))
side_2=int(input("enter another side lenght:"))
side_3=int(input("enter one more side length:"))
if side_1 != side_2 != side_3:
    print("its scalane triangle")
elif side_1 == side_2 == side_2:
    print("its equilateral triangle")
else:
    print("its isosceles triangle")