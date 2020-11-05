'''
Lập chương trình thực hiện các công việc sau:
    - Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
    - Tính tổng các chữ số của số đó.
    - Hiển thị kết qủa ra màn hình
'''
while True:
    print("Nhap 1 so nguyen n:", end="")
    n = int(input())
    if n < 1000:
        break
    print("Đã nhập số lớn hơn 1000 Vui lòng nhập lại ")
temp=n
tong=0
while temp>0:
    b=temp%10
    temp/=10
    tong+=b
print(int(tong))