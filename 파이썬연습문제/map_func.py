
def add(a, b):
    return a + b

li1 = [1, 2, 3]
li2 = [4, 5, 6]

new_li = map(add, li1, li2)

print(list(new_li))