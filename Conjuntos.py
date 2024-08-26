#Julia Machado Kociolek
#O programa deslvolvido irá receber como entrada um arquivo de texto (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
# seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
# operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas.


from itertools import product
import re

arquivo = input("Digite o nome do arquivo: ")

with open(arquivo, "r") as operacoes:
    operacoes_linhas = operacoes.readlines()

def obter_conjuntos(operacoes_arquivo):
    num_operacoes = int(operacoes_arquivo[0].strip())
    linha = 1

    for _ in range(num_operacoes):
        if linha + 2 >= len(operacoes_arquivo):
            print("Erro: Número insuficiente de linhas para as operações.")
            break

        tipo_operacao = operacoes_arquivo[linha].strip()
        linha += 1

        conjuntoA = set(re.findall(r'\w+', operacoes_arquivo[linha].strip()))
        conjuntoB = set(re.findall(r'\w+', operacoes_arquivo[linha + 1].strip()))

        A = set(map(int, conjuntoA)) if all(item.isdigit() for item in conjuntoA) else conjuntoA
        B = set(map(int, conjuntoB)) if all(item.isdigit() for item in conjuntoB) else conjuntoB

        if tipo_operacao == "U":
            resultado = A | B
            print(f"União: conjunto 1 {conjuntoA}, conjunto 2 {conjuntoB}. Resultado: {resultado}")
        elif tipo_operacao == "I":
            resultado = A & B
            print(f"Interseccção: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}")
        elif tipo_operacao == "D":
            resultado = A - B
            print(f"Diferença: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}")
        elif tipo_operacao == "C":
            resultado = list(product(A, B))
            print(f"Produto Cartesiano: conjunto 1 {A}, conjunto 2 {B}. Resultado: {resultado}")

        linha += 2

obter_conjuntos(operacoes_linhas)
