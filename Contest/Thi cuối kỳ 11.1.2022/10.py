class Thisinh():
    def __init__(self,ten,diemchuyencan,diemkiemtra,diembtl,diemcuoiky):
        self.ten = ten
        self.diemchuyencan = diemchuyencan
        self.diemkiemtra = diemkiemtra
        self.diembtl = diembtl
        self.diemcuoiky = diemcuoiky
        self.diemtb = self.tinh()
        self.tb = self.tbinh()
        self.xeploai = self.xeploai()
    def tinh(self):
        diem = (self.diemchuyencan*1 +self.diemkiemtra*1 + self.diembtl*2 + self.diemcuoiky*6)/10
        return round(diem,1)
    def tbinh(self):
        if 8.5<= self.diemtb <=10: return "Giỏi"
        if 7.0<=self.diemtb <=8.4: return "Khá"
        if 5.5 <= self.diemtb <= 6.9: return "Trung bình"
        if 4<= self.diemtb <=5.4: return "Trung bình kém"
        return "Kém"
    def xeploai(self):
        if self.tb =='Giỏi': return 'A'
        if self.tb == 'Khá': return 'B'
        if self.tb == 'Trung bình': return 'C'
        if self.tb == 'Trung bình kém': return 'D'
        return 'F'
    
    def res(self):
        res = []
        res.append(self.ten)
        res.append(self.xeploai)
        res.append(self.tb)
        return res

SinhVien = Thisinh(input(),float(input()),float(input()),float(input()),float(input()))
print(*SinhVien.res(),sep='\n')

