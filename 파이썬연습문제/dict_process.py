
## 1
dic = {"name": "John", "age": 30}
print(f'나이: {dic["age"]}')

## 2
dic = {"math": 90, "science": 85, "history": 78}
print(f'과목들: {list(dic.keys())}')

## 3
dic = {'apple': 3, 'banana': 5}
dic["apple"] = dic["apple"] + 2
print(dic) 