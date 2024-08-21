a = int(input('Digite um numero'))
s = str(input('Digite o sinal'))
b = int(input('Digite um numero'))

if (s == '+'):
    print(a,' ', s,' ',b,' = ', a+b)
elif (s == '-'):
    print(a,' ', s,' ',b,' = ', a-b)
elif (s == '*'):
    print(a,' ', s,' ',b,' = ', a*b)
elif (s == '/'):
    print(a,' ', s,' ',b,' = ', a/b)
else:
    print('Sinal invalido')