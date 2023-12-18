import random

def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(-100, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def add_matrices(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def main():
    rows, cols = 10, 10
    matrix1 = create_matrix(rows, cols)
    matrix2 = create_matrix(rows, cols)

    print("Матрица 1:")
    for row in matrix1:
        print(row)

    print("\nМатрица 2:")
    for row in matrix2:
        print(row)

    matrix3 = add_matrices(matrix1, matrix2)

    print("\nРезультат сложения:")
    for row in matrix3:
        print(row)

if __name__ == "__main__":
    main()
