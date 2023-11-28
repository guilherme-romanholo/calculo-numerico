# Função para realizar a entrada dos valores da matriz
def matrix_input(n):
    # Declara a matriz e um auxiliar
    matrix = []
    aux = []

    # Atribui os valores para a matriz
    for i in range(n):
        for j in range(n):
            # Coloca a primeira linha em uma lista auxiliar
            aux.append(float(input(f"A[{i + 1}][{j + 1}] = ")))
        # Coloca na matriz a cópia dessa lista
        matrix.append(aux[:])
        # Limpa o auxiliar para a próxima iteração
        aux.clear()

    # Retorna a matriz obtida
    return matrix


# Input para o vetor de resultados do sistema
def vector_input(n):
    # Declara o vetor
    vector = []

    # Realiza o input
    for i in range(n):
        vector.append(float(input(f"b[{i + 1}] = ")))

    # Retorna o vetor
    return vector


#Função para printar o sistema 
def print_system(A, b, n):
    for i in range(n):
        for j in range(n):
            print(f"{A[i][j]:.2f}", end = " ")
        print(f"| {b[i]:.2f}")


# Faz o escalonamento do sistema, eliminando os elementos
def gaussian_elimination(A, b, n):
    # Faz uma iteração de k até N
    for k in range(n - 1):
        for i in range(k + 1, n):
            # Faz a atribuição do multiplicador
            mult = A[i][k] / A[k][k]
            # Zera o elemento que desaparecerá no escalonamento
            A[i][k] = 0.0
            # Subtrai o valor dos outros elementos da linha
            for j in range(k + 1, n):
                A[i][j] -= mult * A[k][j]
            # Subtrai o valor do vetor do sistema
            b[i] -= mult * b[k]

        # Mostra o sistema resultante a cada iteração
        print(f"\nPara k = {k + 1}")
        print_system(A, b, n)


def system_resolution(A, b, n):
    # Inicializa a lista de resultados
    x = list(range(0, n))

    # Acha o ultimo elemento do sistema
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

    # Acha os outros elementos do sistema
    for i in range(n - 2, -1, -1):
        # Realiza a soma dos valores conhecidos
        sum = 0
        for j in range(i + 1, n):
            sum += A[i][j] * x[j]
        # Encontra o valor da variável
        x[i] = (b[i] - sum) / A[i][i]

    # Retorna o vetor de respostas
    return x


# Função principal
def main():
    # Recebe o valor de N
    n = int(input("Digite o tamanho da N da matriz: "))

    # Inicializa a matriz do sistema
    A = matrix_input(n)

    # Inicializa o vetor do sistema
    b = vector_input(n)

    # Printa o sistema de entrada
    print("Sistema inicial de entrada:")
    print_system(A, b, n)

    # Realiza a eliminação de Gauss-Jordan
    gaussian_elimination(A, b, n)

    print("\n========== Sistema escalonado =========")

    print_system(A, b, n)

    print("\n========== Resolução do sistema =========")

    # Realiza a resolução do sistema
    x = system_resolution(A, b, n)

    # Printa os valores encontrados
    for i in range(n):
        print(f"x[{i + 1}] = {x[i]:.2f}")


if __name__ == "__main__":
    main()