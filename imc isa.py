
altura = float(input('digite sua altura em metros: '))
peso = float(input('digite seu peso em kg: '))
imc = peso/(altura*altura)
if(imc<18.5):
    print('seu imc é {:.1f} magreza'.format (imc))
elif((imc>18.5) and (imc<24.9)):
    print('seu imc é {:.1f}, normal'.format (imc))
else:
    print('seu imc é {:.1f}, sobrepeso'.format (imc))
    input()
    