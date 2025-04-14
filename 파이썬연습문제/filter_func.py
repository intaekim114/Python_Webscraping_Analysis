

def FilterFunc(n):
    return n > 30

li = [10, 20, 30, 40, 50]

f_li = list(filter(FilterFunc, li))

print(f_li)