s = input()[::-1] # lấy input rồi đảo ngược lại
res =''
for i in range(0, len(s)):
    res = s[i] + res 
    if i % 3 == 2:
        res = ',' + res

print(res.lstrip(','))

# Khi  viết giá trị số nguyên trong Tiếng Anh, người ta thường thêm dấu phẩy để phân tách các nhóm 3 chữ số (tính từ cuối). Ví dụ số 153920529 được viết lại thành 153,920,529.
# Cho số nguyên dương N trong phạm vi số int (không quá 2 tỷ). Hãy chèn dấu phẩy vào N theo quy tắc trên.
# Input
# Chỉ có 1 số N
# Output
# Kết quả sau khi đã chèn dầu phẩy
# Input
# 153920529
# Output
# 153,920,529