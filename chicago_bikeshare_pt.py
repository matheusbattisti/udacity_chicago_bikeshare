# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import math

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

#SOLUCAO TAREFA 1: Loop para as 20 primeiras linhas
i = 0

while(i < 20):
  print("Linha {}: ".format(i+1) + str(data_list[i]))
  i += 1
#FIM SOLUCAO TAREFA 1

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

#SOLUCAO TAREFA 2: Loop gẽnero 20 primeiras linhas
i = 0

while(i < 20):
  print("Gênero linha {}: ".format(i+1) + str(data_list[i][6]))
  i += 1
#FIM SOLUCAO TAREFA 2

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

#SOLUCAO TAREFA 3: Função coluna como lista
"""
Função para transformar uma coluna em lista
Argumentos:
    data: é a lista em si
    index: é o indice da coluna que vamos transformar em lista
Retorna:
    column_list: uma lista com a coluna
"""
def column_to_list(data, index):
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for i in range(len(data)):
      column_list.append(data[i][index])

    return column_list
#FIM SOLUCAO TAREFA 3

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

#SOLUCAO TAREFA 4: count male e female
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
for i in range(len(data_list)):
  if(data_list[i][-2] == 'Male'):
    male += 1
  elif(data_list[i][-2] == 'Female'):
    female += 1
#FIM SOLUCAO TAREFA 4

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

#SOLUCAO TAREFA 5: Função male e female
"""
Função para contar os generos do dataset
Argumentos:
    data_list: é a lista em si
Retorna:
   male: (int) qtd de males
   female: (int) qtd de females
"""
def count_gender(data_list):
    male = 0
    female = 0
    for i in range(len(data_list)):
      if(data_list[i][-2] == 'Male'):
        male += 1
      elif(data_list[i][-2] == 'Female'):
        female += 1
    return [male, female]
#FIM SOLUCAO TAREFA 5


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.

#SOLUCAO TAREFA 6: Função genero mais popular
"""
Função para ver qual o genero mais popular
Argumentos:
    data_list: é a lista em si
Retorna:
    string que mostra qual genero foi o mais populado, ou se são iguais
"""
def most_popular_gender(data_list):

    answer = ""

    male = 0
    female = 0

    for i in range(len(data_list)):
      if(data_list[i][-2] == 'Male'):
        male += 1
      elif(data_list[i][-2] == 'Female'):
        female += 1

    if(male > female):
      answer = 'Masculino'
    elif(female > male):
      answer = 'Feminino'
    else:
      answer = 'Igual'

    return answer
#FIM SOLUCAO TAREFA 6

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

gender_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Por que há linhas sem o registro de gênero."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().

trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

#SOLUCAO TAREFA 9: Função para calculos duracao da viagem
"""
Função para calcular a menor viagem, maior viagem, media e mediana das viagens
Argumentos:
    trip_duration_list: é a lista em si
Retorna:
    não ha saida de dados, muda as variaveis que são globais
"""

def trip_duration(trip_duration_list):

  global min_trip
  global max_trip
  global mean_trip
  global median_trip

  #setando algum valor para iniciar as comparacoes
  min_trip = float(trip_duration_list[0])
  max_trip = float(trip_duration_list[0])

  #min and max trip
  for i in range(len(trip_duration_list)):
    #verificando se faz parte do min
    if(float(trip_duration_list[i]) < min_trip):
      min_trip = float(trip_duration_list[i])

    #verificando se faz parte do max
    if(float(trip_duration_list[i]) > max_trip):
      max_trip = float(trip_duration_list[i])

    #somando a variavel de media
    mean_trip += float(trip_duration_list[i])

  #calculo final media
  mean_trip = mean_trip / len(trip_duration_list)

  #mediana
  middle = len(trip_duration_list)

  sorted_list = trip_duration_list
  sorted_list.sort(key=int)
 
  #verificando a lista se é impar ou par
  if(middle % 2 == 1):
    median_trip = float((sorted_list)[middle//2])
  else:
    median_trip = float((sum(sorted_list)[middle//2-1:middle//2+1])/2.0)

trip_duration(trip_duration_list)
#FIM SOLUCAO TAREFA 9

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set()

startstations_to_list = column_to_list(data_list, 3)

for i in range(len(startstations_to_list)):
  user_types.add(startstations_to_list[i])

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

"""
Função para definir os indices de uma coluna, e contar a ocorrẽncia de cada um deles
Argumentos:
    column_list: é a lista em si
Retorna:
    item_types: list que informa os indices existentes na coluna,
    count_itens: conta a quantidade de cada item
"""
def count_items(column_list):
    item_types = list(set(column_list))
    count_items = []

    for i in range(len(item_types)):
      count = 0
      for j in range(len(column_list)):        
        if(item_types[i] == column_list[j]):
          count += 1
      count_items.append(count)

    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
