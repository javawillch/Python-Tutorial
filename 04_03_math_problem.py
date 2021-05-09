import numpy  

cards = numpy.zeros(100, dtype=bool)

for i in range(2,100):
    add = i
    base = i
    while base <= len(cards):
        if cards[base-1] == True:
            cards[base-1] = False
        else:
            cards[base-1] = True
        base = base + add

print(cards)

for i in range(0,100,1):
    if cards[i] == False:
        print(i+1)
