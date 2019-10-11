import os


s = ""

try:
    if len(s) == 0:
        body_length, body_width, body_height = 0.0, 0.0, 0.0
    else:
        lst = [float(x) for x in s.split('x')]
        lst += [0] * (3 - len(lst))
        [body_length, body_width, body_height] = lst
except IndexError:
    pass


print(body_length, body_width, body_height)


