import numpy as np

def complex_eigendecomposition(data):
    # Compute the correlation matrix
    correlation_matrix = np.corrcoef(data, rowvar=False)

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(correlation_matrix)

    return correlation_matrix, eigenvalues, eigenvectors


def mixed_correlation(matrix1, matrix2):
    '''
    Return Pearson product-moment correlation coefficients. I take just the upper right block that corresponds
    to the correlation between the matrix1 and the matrix 2, i.e. the ijth element is the correlation btw the
    i-th variable of the first dataframe and the j-th conjugate variable of the second dataframe
    '''

    def one_block(matrix):
        rows, cols = matrix.shape

        upper_left = matrix[:rows // 2, :cols // 2]
        upper_right = matrix[:rows // 2, cols // 2:]
        lower_left = matrix[rows // 2:, :cols // 2]
        lower_right = matrix[rows // 2:, cols // 2:]

        new_matrix = upper_right
        return new_matrix

    correlation_matrix = np.corrcoef(matrix1.T, matrix2.T)  # since I keep the rowval = True, I traspose both variables.
    # It's ok to use .T for the second variable since np.corrcoef already does the conjugation
    correlation_matrix = one_block(correlation_matrix)

    return correlation_matrix


def complex_svd(data1, data2):
    U, s, V = np.linalg.svd(mixed_correlation(data1, data2))

    return U, s, V