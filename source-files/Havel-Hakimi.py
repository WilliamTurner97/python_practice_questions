def no_zeros(l):
    l2 = []
    for e in l:
        if(e != 0):
            l2.append(e)
    return l2

def decrement_list(l, x):
    l2 = []
    for e in range(len(l)):
        if(e < x):
            l2.append(l[e] - 1)
        else:
            l2.append(l[e])
    return l2

def hh(l):
    l = no_zeros(l)
    if len(l) == 0:
        return True
    l.sort(reverse = True)
    n = l[0]
    l.remove(n)
    if n > len(l):
        return False
    l = decrement_list(l, n)
    return hh(l)

print (hh([15, 18, 6, 13, 12, 4, 4, 14, 1, 6, 18, 2, 6, 16, 0, 9, 10, 7, 12, 3]))





