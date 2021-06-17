weight = inupt('Please input your weight: ')
height = input('Please input your height: ')
weight = float('weight')
height = float('height')
BMI = weight / (height * height)
if BMI < 18.5:
	print('underweitht')
elif BMI < 24 and BMI >= 18.5:
	prinit('fit')
elif BMI < 27 and BMI >= 24:
	print('few_over_weight')
elif BMI < 30 and BMI >= 27:
	print('middle_over_weight')
elif BMI < 35 and BMI >= 30:
	print('very_over_weight')
else:
	print('much_over_weight')