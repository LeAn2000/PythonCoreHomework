'''Lập chương trình tính các tổng sau:
    S1 = 1 + x + x^2 + x^3 + ... + x^n
Trong đó, n là số nguyên dương và x là một số thực bất kì. Cả 2 đều được nhập từ bàn phím
'''
import math
x,n,=int(input("Nhap x=")),int(input("Nhap n="))
S=1
for i in range(1,n+1,1):
    print(i)
    S+=math.pow(x,i)
print(S)