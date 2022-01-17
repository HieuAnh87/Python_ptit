from datetime import datetime

class Tinhtoan():
    def __init__(self,ma,ten,start,end,luongmua):
        self.ma = ma
        self.ten = ten
        self.start = start
        self.end = end
        self.luongmua = luongmua
        self.

    def Xuly_TimePlay(self):
        start = datetime.strptime(self.start, '%H:%M')
        end = datetime.strptime(self.end, '%H:%M')
        return start - end

    def __str__(self) -> str:
        hour, minute, second = map(int, str(self.Time_Play).split(':'))
        Time_str = '{} gio {} phut'.format(hour, minute)

        return '{}  {} {}'.format(self.ma, self.ten, self.Ten)
    
t = int(input())
ds = []
for i in range(t):
    ds.append