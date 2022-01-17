s = input()
for i in range(len(s)):
    if s[i].islower():
        print(s[i].upper(),end="")
    else:
        print(s[i].lower(),end="")
# print(s)