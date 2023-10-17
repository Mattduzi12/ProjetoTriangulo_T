# Validador de triangulo

# aprasentação
print('\n\t\t\t -- Validador de Triangulo')

# entrada
a = int(input('Informe o lado a'))
b = int(input('Informe o lado b'))
c = int(input('Informe o lado c'))

# processamento e saida
if a < (b + c) and b < (a + c) and c < (a + b):
    print(f'{a}, {b}, {c} formam um triangulo!')

    # tipo do triangulo
    if (a == b) and (b == c):
        print('Equilatero')
    if (a == b) or (a == c) or (b == c):
        print('Isosceles')
    # if (a != b) and (a != c) and (b != c):
    else:
        print('Escaleno')
else:
    print(f'{a}, {b}, {c} não formam um triangulo!')
