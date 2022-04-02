
def flip(s, n):
    s[n] = s[n] ^ 1

def parity(s, x):
    p = 0
    for i in range(64):
        if format(i, '#08b')[-(1+x)] == '1' and s[i] == 1:
            p = p ^ 1
    return p

def board_number(s):
    bn = [0,0,0,0,0,0]
    for i in range(6):
        bn[5 - i] = parity(s, i)
    return bn

def list_to_int(l):
    s = ""
    for i in range(len(l)):
        s = s + str(l[i])
    return int(s, 2)

def prisoner_1(s, k):
    bn = board_number(s)
    c = [0,0,0,0,0,0]
    for i in range(2, 8):
        if bn[i-2] != int(format(k, '#08b')[i]):
            c[i-2] = 1
    flip(s, list_to_int(c))
    return(list_to_int(c))

def prisoner_2(s):
    return list_to_int(board_number(s))


s1 = [0, 0, 0, 0, 0, 0, 0, 0]
s2 = [0, 0, 0, 0, 0, 0, 0, 0]
s3 = [0, 1, 0, 0, 0, 0, 0, 0]
s4 = [0, 0, 0, 0, 0, 0, 0, 0]
s5 = [0, 0, 0, 0, 1, 0, 0, 1]
s6 = [0, 1, 0, 0, 0, 0, 0, 0]
s7 = [0, 0, 0, 0, 0, 0, 0, 0]
s8 = [0, 0, 0, 0, 0, 0, 0, 0]

s = s1 + s2 + s3 + s4+ s5 + s6 + s7 + s8

print(prisoner_1(s, 10))
print(prisoner_2(s))



