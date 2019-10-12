from math import sqrt
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == 0 and b == 0 and c == 0:
    print("all x are roots")
elif a == 0 and b == 0:
    print("no roots")
elif a == 0:
    print(int(-c / b))
else:
    d = b * b - 4 * a * c
    if d < 0:
        print("no roots")
    elif d == 0:
        print(int(-b/2*a))
    else:
        print(int((-b + sqrt(d))/2*a))
        print(int((-b - sqrt(d))/2*a))
