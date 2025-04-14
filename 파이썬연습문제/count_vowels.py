
text = "Python is awesome"
vowel = "aeiou"
cnt = 0

for i in text:
    if i in vowel:
        cnt = cnt + 1

print(f'모음 개수: {cnt}')