
# total_length = 8 
# knife = 3
# current_num = 1


# while current_num < knife:

def cutbar(m, n, current):
    if current >= n:
        return 0
    elif current < m:
        return 1 + cutbar(m, n, current*2)
    else:
        return 1 + cutbar(m, n, current+m)
    

print(cutbar(3, 20, 1))