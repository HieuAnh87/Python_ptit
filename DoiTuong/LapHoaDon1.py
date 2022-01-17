class Hoadon():
    def __init__(self,stt,ten,cu,moi):
        self.MaKH = "KH" +"{0:02d}".format(stt)        
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.hientai = self.tinh()
        self.gia = self.tong()
    def tinh(self):
        return self.moi - self.cu
    def tong(self):
        if 0<= self.hientai <= 50:
            gia = self.hientai*100
            return round(gia+ gia*0.02)
        elif 51<= self.hientai <= 100:
            gia = 50*100 + (self.hientai-50)*150
            return round(gia+gia*0.03)
        else:
            gia = 50*100 + 50*150 + (self.hientai-100)*200
            return round(gia+gia*0.05)
    def __str__(self):
        return '{} {} {}'.format(self.MaKH,self.ten,self.gia)

def run():
    t = int(input())
    ds = []
    for i in range(t):
        ds.append(Hoadon(i+1,input(),int(input()),int(input())))
    sorted_ds = sorted(ds, key=lambda k:-k.gia)
    for i in sorted_ds:
        print(i)
run()

# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612