a= 2
b = 2
def sum(a, b):
    return a +sum(a, b-1)
print(sum(a, b))
