#Giai thua voi for
n= int(input("Nhap vao gia tri n can tinh giai thừa "))
gt=1
for i in range(1,n+1):
    gt*=i
print(gt)
#Giai thua với while
n1= int(input("Nhap vao gia tri n can tinh giai thừa "))
i=1
gt1=1
while i<=n1:
    gt1*=i
    i+=1
print(gt1)

