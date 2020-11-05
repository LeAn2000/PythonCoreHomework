#Nhập vào số tự nhiên n, tính tổng các số chia hết cho 3 mà nhỏ hơn n
#Đã dùng range() smart nhất có thể :)))
n= int(input("Nhap vao gia tri n can tinh "))
tong=0
for i in range(0,n,3):
    print(i)
    tong+=i
print(tong)