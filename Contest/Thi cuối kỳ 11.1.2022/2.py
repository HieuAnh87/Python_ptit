def jaccard_similarity(s1, s2):
    s1 =set(s1)
    s2 =set(s2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

def run():
    s1 = input()
    s2 = input()
    if len(s1) == 0 or len(s2)== 0:
        print(1)
        return
    s1 = s1.replace(","," ")
    s1 = s1.replace("."," ")
    s1 = s1.replace("?"," ")
    s2 = s2.replace(","," ")
    s2 = s2.replace("."," ")
    s2 = s2.replace("?"," ")
    s1 = s1.lower().split()
    s2 = s2.lower().split()
    res = jaccard_similarity(s1,s2)
    print(round(res,2))
run()
