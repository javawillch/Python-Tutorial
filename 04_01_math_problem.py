num = 11
while True:
    # if True:
    # if (True) and (True) and (True) :
    if(str(bin(num)[2:]) == str(bin(num)[2:])[::-1]) and (str(num) == str(num)[::-1]) and (str(oct(num)[2:]) == str(oct(num)[2:])[::-1]):
        print(num)
        print(str(bin(num)[2:]))
        print(str(bin(num)[2:])[::-1])
        break
    print(num)
    num += 2

# print(bin(585))
# print(bin(585)[::-1])
# print(bin(585)[2:])