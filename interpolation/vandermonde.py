import numpy as np

# Função responsável pela entrada de dados
def input_data() -> tuple[float, float]:
    # Recebe a quantidade de pontos
    n: int = int(input("Digite a quantidade de pontos: "))
    # Recebe os valores de x e f(x)
    x: list[float] = [float(input("Digite o valor de x: ")) for _ in range(n)]
    y: list[float] = [float(input("Digite o valor de f(x): ")) for _ in range(n)]

    # Retorna os valores da entrada
    return x, y, n


# Função responsável por encontrar os coeficientes do polinômio
def vandermonde(x: list[float], y: list[float], n: int) -> list[float]:
    # Matriz para a resolução
    matrix: list[list] = []

    # Preenche a matriz com os valores
    for i in range(n):
        aux: list[float] = []

        # Preenche linha por linha
        for j in range(n):
            aux.append(x[i] ** j)

        # Adiciona a linha na matriz
        matrix.append(aux[:])
        # Prepara o vetor auxiliar para a próxima iteração
        aux.clear()

    # Resolve o sistema linear obtido
    z: list[float] = np.linalg.solve(matrix, y)

    # Retorna os coeficientes obtidos
    return z


# Função responsável por printar o resultado obtido
def print_result(z: list[float]):
    # Percorre o vetor de resultados e printa os valores
    for i, zi in enumerate(z):
        print(f"a{i} = {zi}")


# Função principal
def main():
    x, y, n = input_data()
    z = vandermonde(x, y, n)
    print_result(z)


if __name__ == "__main__":
    main()