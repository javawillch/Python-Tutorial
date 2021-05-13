
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

def cuttbar(knife, total_length):
    count = 0 
    current_num = 1
    while total_length > current_num:
        current_num += current_num if current_num < knife else knife
        count = count + 1
    return count


 
print(cuttbar(3, 20))   