import math
#----------- QUESTÃO 1 ----------------

x = 1           #variavel que representa os numeros e é setada como 1 pois mod de zero é zero
aux = 0         #contador dos numeros com as caracteristicas pedidas
while x < 5000000:          #loop de ate 5 milhoes
    if x % 2 == 0 and x % 49 == 0 and x % 37 == 0:          #par, multiplo de 49 e de 37 ao mesmo tempo
        aux += 1            #incremento do contador de numeros
    x += 1          #incremento da variavel auxiliar
print('Resposta da Questão 1(Par, Multiplo de 49 e 37):', aux)          #saida no prompt

#----------- QUESTÃO 2 ----------------

myarray = [0]*10            #construcao do vetor de zeros com 10 posicoes
for i in range(10):         #loop no vetor usando i como indice
    if i % 2 == 0:          #verifica se é par
        myarray[i] = 3**i + 7 * (math.factorial(i))
    else:
        myarray[i] = 2**i + 4 * (math.log(i))
bigger_value = max(myarray)         #salva o valor maximo
n_pos = myarray.index(bigger_value)         #pega a posicao do valor maximo pelo index
pre_value = sum(myarray)            #salva a soma do vetor
average_value = round(pre_value/len(myarray), 2)            #faz a media dividindo a soma pelo tamanho do vetor e arredonda em 2 casas
print('Resposta da Questão 2:')
print('A posição do maior elemento é a de número:', n_pos)
print('A média dos elementos do vetor é:', average_value)

#----------- QUESTÃO 3 ----------------

data_ar = [()]*5            #construcao de um vetor de tuplas de 5 posições
j = 0           #seta o valor do contador de loop
while j < 5:
    print('Insira o Nome do Aluno:')
    z = input()         #recebe o nome do aluno pelo prompt
    print('Insira a Nota Respectiva ao Aluno')
    w = float(input())          #recebe a nota do aluno pelo prompt
    data_ar[(j)] = (z, w)           #salva o nome e a nota numa posicao do vetor de tuplas
    j += 1          #incremento do contador de loop
consulta_nota = dict(data_ar)           #transforma o vetor de tuplas em um dicionario
print('Resposta da Questão 3:')
for key, value in consulta_nota.items():            #loop por todos os itens do dicionario
    if value == max(consulta_nota.values()):        #seleciona o maior valor das notas
        print(key, value)                           #printa a nota e o index que é o nome do aluno
