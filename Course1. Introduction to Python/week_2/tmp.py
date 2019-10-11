from builtins import str

a = [1, 2, 3, 4, 5, 2341]

def list_to_string(a):
   return list(map(str, a))

print(list_to_string(a))
