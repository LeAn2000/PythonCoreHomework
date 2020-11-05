import math
#Giai he phương trình bậc 2
a,b,c=int(input("Nhap a=")),int(input("Nhap b=")),int(input("Nhap c="))
if(a==0):
    x=float(-c/b)
    print("Nghiem cua pt x= ",x)
elif a==0 and b==0:
    print("Phuong trinh vo nghiem")
else:
    delta=b*b-4*a*c
    if delta==0:
        x=-b/(2*a)
        print("Phuong trinh co nghiem duy nhat x1,x2=",x)
    elif delta<0:
        print("Phuong trinh vo nghiem")
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phuong trinh co nghiem duy nhat x1=",x1,"x2=",x2)



