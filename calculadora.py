a = float(input("qual o primeiro número?"))
b = float(input("qual o segundo número?"))

operacao = input('escolha a operação sendo A= soma B= subtração C= divisão D= multiplicação ')

if operacao == 'A' :
    print(a + b)
elif operacao == 'B' :
    print(a - b)
elif operacao == 'C' :
    print(a / b)
elif operacao == 'D' :
    print(a * b)