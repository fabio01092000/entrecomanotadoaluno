nota1 = int(input('Entre com uma nota1 '))
nota2= int(input('Entre com uma nota2 '))
nota3 = int(input('Entre com uma nota3 '))
nota4 = int(input('Entre com uma nota4 '))

media = (nota1+nota2+nota3+nota4)/4

if media >=7:
    print('Aluno aprovado com média ', media)
elif media >5.5:
    print('Aluno de recuperação com média ', media)
else:
    print('Aluno reprovado com média ', media)
sim = input('Quer continuar [s/n] ')
while sim == 's':
    nota1 = int(input('Entre com uma nota1 '))
    nota2 = int(input('Entre com uma nota2 '))
    nota3 = int(input('Entre com uma nota3 '))

    nota4 = int(input('Entre com uma nota4 '))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 7:
        print('Aluno aprovado com média ', media)
    elif media > 5.5:
        print('Aluno de recuperação com média ', media)
    else:
        print('Aluno reprovado com média ', media)
        sim = input('Quer continuar [s/n] ')
print('Boas férias')

