
email = input("이메일을 입력하세요:")

print(email)
if '@' in email and '.' in email:
    print("유효함")
else:
    print("유효하지 않음")
