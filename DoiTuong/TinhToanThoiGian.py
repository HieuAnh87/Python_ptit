from datetime import datetime
class Gamer:
    def __init__(self, Ma, Ten, Time_In, Time_Out) -> None:
        self.Ma = Ma
        self.Ten = Ten
        self.Time_In = Time_In
        self.Time_Out = Time_Out
        self.Time_Play = self.Xuly_TimePlay()

    def Xuly_TimePlay(self):
        time_in = datetime.strptime(self.Time_In, '%H:%M')
        time_out = datetime.strptime(self.Time_Out, '%H:%M')
        return time_out - time_in

    def __str__(self) -> str:
        hour, minute, second = map(int, str(self.Time_Play).split(':'))
        Time_str = '{} gio {} phut'.format(hour, minute)

        return '{}  {} {}'.format(self.Ma, self.Ten, Time_str)

t = int(input())
ds = []
while t>0:
    ds.append(Gamer(input(), input(), input(), input()))
    t-=1
for i in sorted(ds, key=lambda k: -k.Time_Play):
    print(i)

# PY04021 TÍNH TOÁN THỜI GIAN

# Bài làm tốt nhất
# Quán Game mùa này vắng khách nên chủ quán quyết định tính tiền chi tiết đến từng phút. Dựa trên dữ liệu giờ vào và giờ ra, hãy tính thời gian chơi game của các Game thủ nhé.

# Input

# Dòng đầu của dữ liệu vào ghi số lượng game thủ trong ngày (không quá 20).

# Thông tin về một game thủ đến chơi game được ghi lại trên 4 dòng lần lượt là:

# Mã người chơi (xâu ký tự độ dài không quá 10, không có khoảng trống)
# Tên người chơi (xâu ký tự độ dài không quá 100, có thể có khoảng trống).
# Giờ vào (định dạng hh:mm)
# Giờ ra (định dạng hh:mm)
# Ouput

# Ghi ra danh sách game thủ đã được sắp xếp theo thời gian chơi game giảm dần.

# Ví dụ

# Input

# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00

# Output

# 06T  Hoang Van Nam 2 gio 30 phut
# 01T  Nguyen Van An 1 gio 30 phut
# 02I  Tran Hoa Binh 0 gio 55 phut