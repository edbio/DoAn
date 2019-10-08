n = int(input("Nhập n: ")) #Nhập số n tùy ý
tong = 0 #khai báo và gán giá trị cho tong
i = 1 #khai báo và gán giá trị cho biến đếm i

while i <= n:
    tong = tong + i
    i = i+1 # cập nhật biến đếm
print("Tổng là", tong)

# Ket hop else
dem = 0
while dem < 3:
    print("Đang ở trong vòng lặp while")
    dem = dem + 1
else:
    print("Đang ở trong else")