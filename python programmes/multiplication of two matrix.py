def matrix_multiplication(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Matrix multiplication not possible: Inner dimensions don't match.")
        return None

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Given matrices
A = [[2, 1], [3, 4]]
B = [[3, 1], [1, 2]]

# Perform matrix multiplication
C = matrix_multiplication(A, B)

# Print the result
if C is not None:
    print("Resultant Matrix (C):")
    for row in C:
        print(row)
