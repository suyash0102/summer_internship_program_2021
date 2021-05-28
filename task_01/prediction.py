import joblib
print(f'!!! WELCOME TO SALARY PREDICTOR PROGRAM !!!')
name = input('Kindly enter your name: ')
numyexp = float(input('Kindly enter your experience in no. of years: '))
model=joblib.load('salary_prediction.pk1')
print(f'\nName: {name}')
print(f'Years of experience you have: {numyexp}')
output=model.predict([[numyexp]])
print(f'{name}, your  monthly predicted salary in INR is: {round(output[0],2)}')                
