# P = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
def isPy(s):
    if s.lower() == '.py':
        return True
    return False
# def isName(s):
#     for i in range(len(s)):
#         if P.find(s[i])>=len(P) or P.find(s[i])<=0:
#             return False
#     return True

s = input()
s1 = s[:-3]
s2 = s[-3:]
# if isPy(s2) and isName(s1):
if isPy(s2):
    print("yes")
else:
    print("no")
    

