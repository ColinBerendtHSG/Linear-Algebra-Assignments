# a) Take a square matrix as input and return its inverse without using any additional packages
def main():
    while True:
        print("Enter a square matrix:")
        matrix = get_matrix_from_user()
        print("\n")

        if matrix is not None:
            print("Original square matrix:")
            for row in matrix:
                print(row)
        determinant = check_determinant(matrix)
        if determinant != 0:
            inverse = turn_into_inverse(matrix)
            if inverse is not None:
                print("\nInverse of square matrix:")
                for row in inverse:
                    print(row)
        else:
            print("\nError: The matrix is singular (the determinant is zero) hence there is no inverse.")
        break

def get_matrix_from_user():
    matrix = []
    rows = int(input("Number of rows: "))
    columns = int(input("Number of columns: "))

    #Check if it is a square matrix
    while rows != columns:
        print("A square matrix must have the same number of rows as columns")
        return None
    
    if rows == columns:
        index = 0
        while index < rows:
            row = input(f"Element for row {index + 1} separate by commas: ").split(",")
            if len(row) == columns:
                row_elements = []
                for element in row: 
                    row_elements.append(float(element))
                matrix.append(row_elements)
                index += 1
            else:
                print("Number of elements in the row do not correspond the number of columns")              
    return matrix
        
def turn_into_inverse(matrix, decimal_places = 2):
    matrix_size = len(matrix)

    # Determine the identity matrix
    identity_matrix = []
    for i in range(matrix_size):
        identity_matrix_rows = []
        for column in range(matrix_size):
            if i == column:
                identity_matrix_rows.append(1)
            else:
                identity_matrix_rows.append(0)
        identity_matrix.append(identity_matrix_rows)

    # Add the identity matrix to the given matrix and turn it into an augmented matrix for calculation
    augmented_matrix = []
    for i, row in enumerate(matrix):
        augmented_matrix.append(row + identity_matrix[i])

    # Do Gauss elimination to get the solutions
    for i in range(matrix_size):
        pivot_row = i

        # Find the pivot row for calculation
        for j in range(i + 1, matrix_size):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[pivot_row][i]):  #Use abs to receive distance (signed or unsigned neglectable) -> 10.11.23 ChatGPT
                pivot_row = j

        # Swap the pivot row with the current row
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

        # Make the diagonal element of the current row equal to 1
        diagonal_entries = augmented_matrix[i][i]
        for j in range(matrix_size * 2):   #Multiply by 2 because the augemented matrix has two times more columns than the original matrix
            augmented_matrix[i][j] /= diagonal_entries

        # Eliminate other rows
        for j in range(matrix_size):
            if i != j:
                scalar = augmented_matrix[j][i]
                for x in range(matrix_size * 2):
                    augmented_matrix[j][x] -= scalar * augmented_matrix[i][x]

    # Round the elements of the matrix
    for i in range(matrix_size):
        for j in range(matrix_size * 2):
            augmented_matrix[i][j] = round(augmented_matrix[i][j], decimal_places)
   

    # Determine the inverse matrix
    inverse_matrix = [row[matrix_size:] for row in augmented_matrix]

    return inverse_matrix

#(b) Before calculating the inverse, include a check to ensure the input matrix is invertible
def check_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

#Use check_determinant in order to return the element in the minor matrix (first two lines of function) 
# -> This is the only function I needed a little help with and I hope that citing the source will suffice
# 11.11.23 StackOverflow https://stackoverflow.com/questieterminant-using-python-without-using-scipy-linalg-det

    determinant = 0
    for i in range(len(matrix[0])):
        minor_matrix = []
        for row in matrix[1:]:
            minor_matrix.append(row[:i] + row[i + 1:])
        
        determinant += ((-1) ** i) * matrix[0][i] * check_determinant(minor_matrix)  
    
    return determinant

if __name__ == '__main__':
    main()
        

            
