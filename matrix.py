def matrix_addition(matrix1, matrix2):
    """Adds two 2x2 matrices."""

    if len(matrix1) != 2 or len(matrix2) != 2 or len(matrix1[0]) != 2 or len(matrix2[0]) != 2:
        raise ValueError("Matrices must be 2x2")
    
    result_matrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
    return result_matrix

# Example Usage
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

try:
  sum_matrix = matrix_addition(matrix_a, matrix_b)
  print("Matrix A:", matrix_a)
  print("Matrix B:", matrix_b)
  print("Sum of A and B:", sum_matrix)
except ValueError as e:
  print("Error:", e)
