# Para entrar com a dimensão da matrix A
n = int(input("Digitar a dimensão n da matriz A: "))
# Para inicializar a matriz A e o vetor v
A = [ ]; v = [ ]
for i in range(0,n+1):
    v.append(i); A.append([ ])
    for j in range(0,n+1):
        A[i].append(0.0)

# Para entrar com os valores de A[i,j]
for i in range (1,n+1): # i varia de 1 para n
    for j in range (1, n+1): # j varia de 1 para n 
        print("Digitar o valor de A[", i,",",j,"]: ", end = ' ')
        A[i][j] = float(input())

ut = 1 # ut representa τ
for i in range(1,n+1): # i varia de 1 para n
    v[i] = i

# Inicio do processo A -> LU
for k in range(1,n): # k varia de 1 para n-1
# parte pivoteamento
    mx = k
    for i in range(k+1,n+1): # i varia de k+1 para n
        if abs(A[i][k]) > abs(A[mx][k]) : mx = i
    if mx > k : # se mx > k trocar dos valores entre linha k e linha mx
        ut = - ut
        it = v[k]; v[k] = v[mx]; v[mx] = it
        for j in range(1,n+1): # j varia de 1 para n
            rt = A[k][j]; A[k][j] = A[mx][j]; A[mx][j] = rt

# parte eliminação
    for i in range(k+1,n+1):
        mult = A[i][k]/A[k][k]
        for j in range(k+1, n+1):
            A[i][j] = A[i][j] - mult * A[k][j]
        A[i][k] = mult

# Para resolver o sistema Ax = b
# Para inicializar os vetores b e x
b = [ ]; x = [ ]; y = [ ]
for i in range(0,n+1):
    b.append(0.0)
    x.append(0.0)
    y.append(0.0)
# Para entrar com os valores de b[i]
for i in range(1,n+1):
    print("Digitar o valor de b[", i, "]: ", end = ' '),
    b[i] = float(input())

# Para resolver o sistema Ly = ˜b
y[1] = b[v[1]]
for i in range(2, n+1): # i varia de 2 para n
    sum = 0.0
    for j in range(1,i): # j varia de 1 para i-1
        sum = sum + y[j]*A[i][j]
    y[i] = b[v[i]] - sum

# Para resolver o sistema Ux = y
x[n] = y[n]/A[n][n]
for i in range(n-1, 0,-1): # i varia de n-1 para 1
    sum = 0.0
    for j in range(i+1,n+1): # j varia de i+1 para n
        sum = sum + x[j]*A[i][j]
    x[i] = (y[i] - sum)/A[i][i]

for i in range(1,n+1):
    print(x[i])
