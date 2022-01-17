import math
class Phanso():
    def __init__(self, tu1, mau1, tu2, mau2):
        self.tu1 = tu1
        self.mau1 = mau1
        self.tu2 = tu2
        self.mau2 = mau2
    def solve(self):
        ucln1 = math.gcd(self.tu1, self.mau1)
        self.tu1 = self.tu1//ucln1
        self.mau1 = self.mau1//ucln1

        ucln2 = math.gcd(self.tu2, self.mau2)
        self.tu2 = self.tu2//ucln2
        self.mau2 = self.mau2//ucln2

        bcnn = self.mau1/math.gcd(self.mau1,self.mau2)*self.mau2
        if int(self.mau1) != int(bcnn):
            self.tu1 = self.tu1 * bcnn//self.mau1
        if int(self.mau2) != int(bcnn):
            self.tu2 = self.tu2 * bcnn//self.mau2
        tu = int(self.tu1 + self.tu2)
        mau = int(bcnn)
        print(f"{tu}/{mau}")

def run():
    tu1,mau1,tu2,mau2 = map(int, input().split())
    PhanSo = Phanso(tu1,mau1,tu2,mau2)
    PhanSo.solve()
run()
    