class Diem():
    def __init__(self,stt,ten,diem):
        self.stt = "HS" + "{0:02d}".format(stt)
        self.ten = ten
        self.diem = diem
        self.diemtb = self.tinh()
        self.xeploai = self.tbinh()
    def tinh(self):
        DiemTB =  (sum(self.diem) + self.diem[0] + self.diem[1])/(len(self.diem)+2)
        return round(DiemTB,1)

    def tbinh(self):
        if self.diemtb >=9: return "XUAT SAC"
        if self.diemtb >=8: return "GIOI"
        if self.diemtb >=7: return "KHA"
        if self.diemtb >=5: return "TB"
        return "YEU"
    def __str__(self):
        return "{} {} {} {}".format(self.stt, self.ten, self.diemtb, self.xeploai)
     
    
t = int(input())
ds = []
for i in range(t):
    ten = input()
    diem = list(map(float, input().split()))
    # print(Diem(i+1,ten,diem))
    ds.append(Diem(i+1,ten,diem))

for i in sorted(ds, key=lambda x: (x.diemtb,x.stt) ,reverse=True):
    print(i)
