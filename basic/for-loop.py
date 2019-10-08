# Tính tổng tất cả các số trong danh sách A
# Danh sách A
A = [1, 3, 5, 9, 11, 2, 6, 8, 10]
# Biến để lưu trữ tổng các số là tong, gán giá trị ban đầu bằng 0 
tong = 0
# Vòng lặp for, a là biến lặp
for a in A: 
     tong = tong+a
# Đầu ra: Tổng các số là 55
print("Tổng các số là", tong)


# Ket hop ham range()
chuoi = ['bố','mẹ','em']

for tu in range(len(chuoi)):

    print("Anh yêu",chuoi[tu])


# Ket hop voi else
#Lặp dãy từ 0 đến 10
for num in range(0,10):
#Lặp trên các thừa số của một số trong dãy
    for i in range(2,num): 
#Xác định thừa số đầu tiên (phép chia có số dư bằng 0)
        if num%i == 0: 
            j=num/i #Ước lượng thừa số thứ 2
            print ('%d bằng %d * %d' % (num,i,j))
            break #Dừng vòng for hiện tại, chuyển đến số tiếp theo trong vòng for đầu tiên
        else: # Phần else trong vòng lặp
            print (num, 'là số nguyên tố')