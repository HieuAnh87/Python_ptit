import re
def Compare(opening, closing):
    if opening == '(' and closing == ')':
        return True
    return False

def run():
    stack = []
    res = []
    s = input()
    st = []
    pos_now = 1
    pos_stack = 1
    for char in s:
        # pos_stack = stack[-1]
        if char == '(':
            res.append(pos_now)
            pos_stack = pos_now
            # pos_stack = stack.pop()
            # stack.insert(pos_stack)
            pos_now += 1
            stack.append(pos_stack)
        if char ==')':
            top = stack.pop()
            print(stack)
            # print(stack)
            res.append(pos_stack)
            pos_stack -= 1
            if len(stack)==0:
                break
        # print(stack)
        # print(len)
    print(res)
run()