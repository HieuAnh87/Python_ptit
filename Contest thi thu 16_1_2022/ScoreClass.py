class Thisinh():
    def __init__(self,ten,diemchuyencan,diembtl,diemcuoiky):
        self.ten = ten
        self.diemchuyencan = diemchuyencan
        self.diembtl = diembtl
        self.diemcuoiky = diemcuoiky
        self.tongdem = self.tinh()
    def tinh(self):
        diem = (self.diemchuyencan*1 + self.diembtl*3 + self.diemcuoiky*6)/10
        return diem
    def __str__(self) -> str:
        return '{} {}'.format(self.ten, self.tongdem)
    
print(Thisinh(input(),float(input()),float(input()),float(input())))

# Nguyen Van A
# 10
# 7
# 8