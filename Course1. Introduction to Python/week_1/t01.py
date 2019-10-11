import sys

digit_string = sys.argv[1]
answ = 0
for i in digit_string:
    answ += int(i)

print(answ)