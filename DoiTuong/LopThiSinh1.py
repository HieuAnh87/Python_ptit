class Thisinh():
    def __init__(self,hoten,dob,mon1,mon2,mon3):
        self.hoten = hoten
        self.dob = dob
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        # self.tong = tong
    def solve(self):
        tong = (self.mon1 + self.mon2 + self.mon3)
        print(f"{self.hoten} {self.dob} {tong}")

def run():
    hoten= input()
    dob = input()
    mon1= float(input())
    mon2= float(input())
    mon3= float(input())
    ThiSinh = Thisinh(hoten,dob,mon1,mon2,mon3)
    ThiSinh.solve()
run()