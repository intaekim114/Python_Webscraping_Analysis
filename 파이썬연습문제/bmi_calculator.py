
weight = int(input('체중(kg)을 입력해 주세요.'))
height = int(input('키(cm)를 입력해 주세요.'))

h = height / 100

bmi = weight / (h * h)

print(f'체중: {weight} \n  키: {height} \n BMI: {bmi:.1f}')