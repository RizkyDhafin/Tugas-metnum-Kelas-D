def crout_decomposition(A):
    n = len(A)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    
    for i in range(n):
        U[i][i] = 1
        
        for k in range(i, n):
            sum_l = sum(L[k][p] * U[p][i] for p in range(i))
            L[k][i] = A[k][i] - sum_l
        
        for k in range(i + 1, n):
            sum_u = sum(L[i][p] * U[p][k] for p in range(i))
            U[i][k] = (A[i][k] - sum_u) / L[i][i]
    
    return L, U

def crout_solve(A, b):
    n = len(A)
    L, U = crout_decomposition(A)
    
    # Solusi Ly = b dengan substitusi maju
    y = [0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    
    # Solusi Ux = y dengan substitusi mundur
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]
    
    return x

# Contoh pengujian
A = [[2, 1], [5, 3]]
b = [4, 10]
x = crout_solve(A, b)
print("Solusi x =", x)