def matrix_multiplication(A, B):
    # Fungsi untuk mengalikan dua matriks A dan B
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B")
    
    # Inisialisasi hasil perkalian
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # atau rows_B
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def transpose_matrix(A):
    # Fungsi untuk menghasilkan transpose dari matriks A
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def inverse_matrix(A):
    # Fungsi untuk menghitung invers dari matriks A (hanya untuk matriks 2x2)
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    
    if det == 0:
        raise ValueError("Determinan matriks A nol, invers tidak dapat dihitung")
    
    inv_det = 1 / det
    A_inv = [[A[1][1] * inv_det, -A[0][1] * inv_det],
             [-A[1][0] * inv_det, A[0][0] * inv_det]]
    
    return A_inv

def solve_linear_system_inverse(A, b):
    # Menghitung invers dari matriks A
    A_inv = inverse_matrix(A)
    
    # Menghitung solusi x = A_inv * b
    x = matrix_multiplication(A_inv, [[bi] for bi in b])
    
    return [xi[0] for xi in x]

# Contoh pengujian
A = [[1, 5], [1, 3]]
b = [4, 10]
x = solve_linear_system_inverse(A, b)
print("Solusi x =", x)