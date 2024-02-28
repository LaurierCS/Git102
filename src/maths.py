# write a function that calculates the wedge product of two vector.
def wedge_product(v1, v2):
    return -1

# write a function that calculates the dot product of two vectors.
def dot_product(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

# write a function that calculates the cross product of two vectors.
def cross_product(v1, v2):
    return 0

# write a function to calculate the determinant of a 2x2 matrix.
def determinant(matrix):
    result = 0;
    for i in range(2):
        result += matrix[i][0] * matrix[(i+1)%2][1]
    return result
