def lu_decomposition(A):
    n = len(A)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]
    
    for i in range(n):
        L[i][i] = 1
        
        for k in range(i, n):
            sum_l = sum(L[i][p] * U[p][k] for p in range(i))
            U[i][k] = A[i][k] - sum_l
        
        for k in range(i + 1, n):
            sum_u = sum(L[k][p] * U[p][i] for p in range(i))
            L[k][i] = (A[k][i] - sum_u) / U[i][i]
    
    return L, U

def lu_gauss_solve(A, b):
    n = len(A)
    L, U = lu_decomposition(A)
    
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
A = [[1, 1], [5, 3]]
b = [4, 10]
x = lu_gauss_solve(A, b)
print("Solusi x =", x)