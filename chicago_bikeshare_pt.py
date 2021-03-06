# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

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

def print_data(list, size, column=False):
    """
    Função print_data(list, size, column=False).
    Utilizado para imprimir as linhas de uma base de dados.
    Argumentos:
        list: Lista que será varrida.
        size: Limite do indice a ser varrido.
        column: Determina qual característica a ser listado, caso não seja declarado será listado todas as características
    Retorna:
        Imprime uma lista a partir de uma lista de dados.

    """

    first_twenty_rows = list[:size]
    for row in first_twenty_rows:
        print(row if not column else row[column])

print_data(data_list, 20)

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2

print_data(data_list, 20, -2)


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
def column_to_list(data, index):
    """
    Função column_to_list(data, index).
    Adiciona colunas(features) de uma lista em outra lista, na mesma ordem.
    Argumentos:
        data: Base com a matriz a ser filtrada.
        index: Determina o índice da coluna a ser filtrada.
    Retorna:
        Uma lista com os dados da coluna filtrada da base.

    """

    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for row in data: column_list.append(row[index])
    return column_list

gender_list = column_to_list(data_list, -2)
# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(gender_list[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
def count_by_gender_filtered(gender_filtered):
    """
    Função count_by_gender_filtered(data_list).
    Contar a quantidade de resultados por gênero.
    Argumentos:
        gender_filtered: Gênero a ser filtrado.
    Retorna:
        Valor da contagem.

    """

    result_count_gender = 0

    for gender in gender_list:
        if gender == gender_filtered: result_count_gender += 1

    return result_count_gender

male = count_by_gender_filtered("Male")
female = count_by_gender_filtered("Female")
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função count_gender(data_list).
    Contar os gêneros e retorna em uma lista.
    Argumentos:
        data_list: Lista de dados de uma coluna de uma matriz filtrada.
    Retorna:
        Lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos).

    """

    return [count_by_gender_filtered("Male"), count_by_gender_filtered("Female")]


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
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
    """
    most_popular_gender(data_list).
    Pega o gênero mais popular, e retorne este gênero como uma string.
    Argumentos:
        data_list: Lista de dados de uma coluna de uma matriz filtrada.
    Retorna:
        Apresenta "Male", "Female", ou "Equal" como resposta.

    """

    answer = ""
    [count_result_by_male, count_result_by_female] = count_gender(data_list)

    if count_result_by_male == count_result_by_female:
        answer = "Equals"
    else:
        answer = "{}male".format("fe" if count_result_by_female > count_result_by_male else "").capitalize()

    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
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
user_type_list = column_to_list(data_list, -3)

def count_items(column_list, item_types=[], count_items=[]):
    """
    Função count_items(column_list).
    Conta os tipos de usuários, sem definir os tipos.
    Argumentos:
        column_list: Lista de dados de uma coluna de uma matriz filtrada.
    Retorna:
        Retorna 2 listas contendo [item_types] e [count_items] Ex: ['', 'Female', 'Male'], [316867, 298784, 935854]

    """

    for item in column_list:
        if item not in item_types:
            item_types.append(item)
            count_items.append(column_list.count(item))

    return item_types, count_items

# Se tudo está rodando como esperado, verifique este gráfico!
types, quantity = count_items(user_type_list, [], [])
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)
print("\nTAREFA 7: Verifique o gráfico!")

input("Aperte Enter para continuar...")
# TAREFA 8
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque apesar de termos 2 gêneros no nosso espaço amostral(\"male\" / \"female\"), possuimos {} registros sem cadastro.".format(count_by_gender_filtered(""))
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# Você não deve usar funções prontas para isso, como max() e min().

from statistics import median

trip_duration_list = list(map(int, filter(None, column_to_list(data_list, 2))))
min_trip = min(trip_duration_list)
max_trip = max(trip_duration_list)
mean_trip = sum(trip_duration_list) / len(trip_duration_list)
median_trip = median(trip_duration_list)

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
start_stations = set(filter(None, column_to_list(data_list, 3)))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
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
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list, [], [])
    print("\nTAREFA 12: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
    # -----------------------------------------------------
