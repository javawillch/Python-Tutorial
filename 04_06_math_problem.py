def collatz(init, curr, isFirst):
    if curr == 1:
        return False
    elif curr == init:
        return True
    else:
        if isFirst == True:
            curr = init * 3 + 1
        if curr % 2 == 0:
            return collatz(init, curr/2, False)
        else:
            return collatz(init, curr*3 + 1, False)

def inLoopCount(target):
    result = 0
    for i in range(2, target, 2):
        if collatz(i, 0, True) == True:
            result += 1
    return result

print(inLoopCount(10000))