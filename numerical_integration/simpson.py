import sympy as sp

# Função responsável pela entrada de dados
def input_data() -> tuple[float, float, callable]:
    # Recebe os limites de integração
    a: float = float(input("Digite o limite de integração a: "))
    b: float = float(input("Digite o limite de integração b: "))
    # Recebe a função em formato de string
    f_str: str = input("Digite a função f(x) que será integrada: ")

    # Transforma a string em uma função lambda
    x_sym: sp.Symbol = sp.symbols('x')
    f: callable = sp.lambdify(x_sym, sp.sympify(f_str))

    # Retorna os valores
    return a, b, f


# Função para aproximar o valor da integral
def sympson(a: float, b: float, f: callable) -> float:
    # Descobre o valore de h
    h: float = (b - a) / 2

    # Calcula o resultado
    result: float = (h / 3) * (f(a) + 4 * f(a + h) + f(b))

    # Retorna o resultado obtido
    return result


# Função principal do programa
def main():
    a, b, f = input_data()
    
    r = sympson(a, b, f)

    print(f"O valor da aproximação é: {r}")


if __name__ == "__main__":
    main()