import sys
import random

x = int(sys.argv[1][0])
y = int(sys.argv[1][2:])
z = 0

for i in range(x):
    z = z + random.randint(1, y)

print("You rolled: " + str(z))