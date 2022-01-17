from math import  cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371
    return c * r
s1,s2 = input().split()
s3,s4 = input().split()
s1 = float(s1)
s2 = float(s2)
s3 = float(s3)
s4 = float(s4)
# print(s1,s2,s3,s4)
res = haversine(s1,s2,s3,s4)
print(round(res,2))
# 105.96 10.21
# 107.17 16.79
