def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open(filename, 'r') as input_file:
        return [[int(column) for column in row.split()] for row in input_file]

def matrix_count(filename):
    matrix = read_matrix(filename)
    rowsums = []
    columnsums = []
    for i in range(0,len(matrix)):
        rowsums.append(sum(matrix[i]))
    for j in range(0,len(matrix[1])):
        columnsums.append(sum(matrix[:,j]))
    
    print("Row Sums:", rowsums)
    print("Column Sums:", columnsums)

matrix_count("testmatrix0.txt")
