def matrix_multiply_1(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matris boyutları uyumsuz. Çarpım yapılamaz.")
        return None

    result_matrix_1 = [
        [sum(x * y for x, y in zip(res_row, col)) for col in zip(*matrix2)]
        for res_row in matrix1
    ]

    return result_matrix_1


A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]

result = matrix_multiply_1(A, B)

if result is not None:
    print("Çarpım Matrisi:")
    for row in result:
        print(row)
