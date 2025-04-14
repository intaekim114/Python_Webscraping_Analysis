
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_li= [num**2 if num % 2 == 0 else num for num in li]

print(new_li)