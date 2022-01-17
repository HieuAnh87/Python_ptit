import math
class Phanso():
    def __init__(self, tu , mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu//ucln
        self.mau = self.mau//ucln
        print(f"{self.tu}/{self.mau}")



def run():
    tu,mau = map(int, input().split())
    PhanSo = Phanso(tu, mau)
    PhanSo.rutgon()
run()