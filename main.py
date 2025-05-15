from calculadora import soma

# print(soma(2, 2))
# print(soma(20, 10))
try:
    print(soma('2.5', 1.5))
except AssertionError as e:
    print(f'Conta inválida: {e} ')

print('Conta', soma(25, 25))