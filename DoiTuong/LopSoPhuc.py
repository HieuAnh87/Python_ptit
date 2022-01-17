class Sophuc():
    def __init__(self,thuc1,ao1,thuc2,ao2):
        self.thuc1 = thuc1
        self.ao1 = ao1
        self.thuc2 = thuc2
        self.ao2 = ao2
    
    def solve(self):
        tongthucC = self.thuc1 +self.thuc2
        tongaoC = self.ao1 + self.ao2
        # aa' - bb' + (ab' + a'b)i
        thucC = self.thuc1*tongthucC - self.ao1*tongaoC
        aoC = (self.thuc1*tongaoC + tongthucC*self.ao1)
        # aa' - bb' + (ab' + a'b)i
        thucD = tongthucC*tongthucC - tongaoC*tongaoC
        aoD = tongthucC*tongaoC + tongthucC*tongaoC
        if aoC > 0:
            resC = f"{thucC} + {aoC}i"
        else:
            resC = f"{thucC} - {abs(aoC)}i"
        if aoD > 0:
            resD = f"{thucD} + {aoD}i"
        else:
            resD = f"{thucD} - {abs(aoD)}i"
        # print(f"{thucC} {aoC}, {thucD} {aoD}")
        print(f"{resC}, {resD}")


def main():
    t = int(input())
    for i in range(t):
        thuc1,ao1,thuc2,ao2 = map(int, input().split())
        SoPhuc = Sophuc(thuc1,ao1,thuc2,ao2)
        SoPhuc.solve()
main()

        
