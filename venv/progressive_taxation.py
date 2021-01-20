brackets = [10000, 30000, 100000, float('inf')]
rates = [.1, .25, .4]

def tax(n):

    t = 0

    for i in range(3):
        if n >  brackets[i + 1]:
            t = t + ((brackets[i + 1] - brackets[i]) * rates[i])
        elif n > brackets[i]:
            t = t + ((n - brackets[i]) * rates[i])

    return int(t)

print(tax(56789))
