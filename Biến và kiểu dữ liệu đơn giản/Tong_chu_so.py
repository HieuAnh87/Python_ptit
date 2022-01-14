s = input()
count = 0
if len(s) == 1:
    count = 1
else:
    while len(s) != 1:
        sum = 0
        for i in s:
            sum += ord(i) - ord('0')
            # print(sum)6
        s = str(sum)
        count += 1
print(count)
# Bài này phải chuyển dấu âm thàh mã ASCII rồi cộng với số nguyên :D