def print_hi(name):
    print(f'Olá mundo, {name}')

def soma(n1, n2):
    print(f'Somando {n1} + {n2}')
    resultado = n1 + n2

    return resultado

def subtracao(n1, n2):
    print(f'Subtraindo {n1} - {n2}')
    resultado = n1 - n2

    return resultado

def multiplicacao(n1, n2):
    print(f'Multiplicando {n1} * {n2}')
    resultado = n1 * n2

    return resultado

def divisao(n1, n2):
    print(f'Dividindo {n1} / {n2}')
    resultado = n1 / n2

    return resultado

if __name__ == '__main__':
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    operador = input('Digite o operador do cálculo:')

    resultado = None

    if operador == '+':
        resultado = soma(n1, n2)
    elif operador == '-':
        resultado = subtracao(n1, n2)
    elif operador == '*':
        resultado = multiplicacao(n1, n2)
    elif operador == '/':
        resultado = divisao(n1, n2)
    else:
        print('Operador incorreto')

    if resultado != None:
        print(f'O resultado da operação é: {resultado}')

'''    listaConvidados = ['Filipe', 'Douglas', 'Rafael']

    nome = input('Digite seu \n nome:') #quebra a linha \n
    idade = int(input('Digite sua idade:'))

    estaNaLista = nome in listaConvidados
    maiorIdade = idade >= 18

    if estaNaLista:
        if maiorIdade:
            print('Pode entrar e você é maior de idade')
        else:
            print('Desculpe, seu nome está na lista mas você não é maior de idade')
    else:
        print('Desculpe, mas seu nome não está na lista')
'''


'''    
    nota = int(input('Digite sua nota:'))

    if nota <= 30:
        print("você foi reprovado!")
    elif nota <= 60:
        print("voce ficou de prova final")
    else:
        print("Você está aprovado")
'''
'''
    valido = False #False em vez de false
    print(not valido) #em vez do ! deve usar o not

    numero = int(input("Digite um número:")) #mostra uma mensagem na tela e aguarda o usuário digitar
    print(f'O número digitado foi {numero}')
    print(type(numero))

    numero2 = 20
    #print('O número digitado foi ' + numero2) iria dar erro por numero2 ser int e o texto string


    print_hi('Daniel')
    temperatura = 20.0
    print(type(temperatura))
    temperatura = "Felipe"
    print(type(temperatura))
    listaNomes = ['Felipe', 'Daniel', 'Douglas']
    print(type(listaNomes))

    idade = 29
    print(type(idade))

    dicionarioPessoa = {
        'nome': 'Felipe',
        'idade': idade
    }
    print(dicionarioPessoa)

    numeroComplexo = 5 + 5j
    print(type(numeroComplexo))

    verificacao = False
    print(type(verificacao))

    #comentário no python

    variavelNula = None
    print(type(variavelNula))

    nome = 'Mauricio'

    if nome == 'João':
        print('O nome é João')
    elif nome == 'Filipe':
        print('O nome é Filipe')
    else:
        print('Não é nenhum dos nomes')
'''
