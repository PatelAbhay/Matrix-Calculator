
def add_matrix(matrix_a, matrix_b):
    new_matrix = []
    for i in range(0, len(matrix_a)):
        sum_row = []
        for j in range(0, len(matrix_a[0])):
            sum_row.append(matrix_a[i][j] + matrix_b[i][j])
        new_matrix.append(sum_row)
    return new_matrix


def subtract_matrix(matrix_a, matrix_b):
    new_matrix = []
    for i in range(0, len(matrix_a)):
        subract_row = []
        for j in range(0, len(matrix_a[0])):
            subract_row.append(matrix_a[i][j] - matrix_b[i][j])
        new_matrix.append(subract_row)
    return new_matrix


def scalar_multiply(matrix_a, scalar):
    new_matrix = []
    for i in range(0, len(matrix_a)):
        new_row = []
        for j in range(0, len(matrix_a[0])):
            new_row.append(scalar * matrix_a[i][j])
        new_matrix.append(new_row)
    return new_matrix


def multiply_matrix(matrix_a, matrix_b):
    result = []
    for i in range(0, len(matrix_a)):
        final_row = []
        for j in range(0, len(matrix_b[0])):
            col_vector = []

            for k in range(0, len(matrix_b)):
                col_vector.append(matrix_b[k][j])

            for l in range(0, len(col_vector)):
                col_vector[l] *= matrix_a[i][l]

            sum = 0
            for m in range(0, len(col_vector)):
                sum += col_vector[m]
            final_row.append(sum)
        result.append(final_row)
    return result


def transpose(matrix_a):
    transposed = []
    for i in range(0, len(matrix_a[0])):
        new_row = []
        for j in range(0, len(matrix_a)):
            new_row.append(matrix_a[j][i])
        transposed.append(new_row)
    return transposed


def determinant(matrix):
    pass


def inverse(matrix):
    pass
