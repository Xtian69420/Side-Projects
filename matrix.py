# nag create ako ng mga function na same as len, split or other method na restricted. para same functionality pero from scratch
# custom len
def get_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# custom range
def custom_range(start, stop, step=1):
    if step == 0:
        raise ValueError("Step must not be zero.")
    if (start < stop and step > 0) or (start > stop and step < 0):
        current = start
        while (current < stop and step > 0) or (current > stop and step < 0):
            yield current
            current += step

# custom append
def custom_append(lst, item):
    lst[get_length(lst):] = [item]

# custom join strings
def custom_join(lst, separator):
    return separator.join(str(lst[i]) for i in custom_range(0, get_length(lst)))

# input
def input_augmented_matrix():
    print("Enter the number of equations (rows): ")
    n = int(input())
    
    matrix = []
    for i in custom_range(0, n):
        print(f"Enter the values for row {i + 1} (space-separated, include constants in the last index):")
        user_input = input()

        # manual splitting kasi bawal xdd
        row = []
        number = ""
        for char in user_input:
            if char == " ":
                if number:
                    custom_append(row, float(number))
                    number = ""
            else:
                number += char
        if number:
            custom_append(row, float(number))

        if get_length(row) != n + 1:
            print("Error: Icorrect number of elements")
            return None

        custom_append(matrix, row)

    return matrix

def gaussian_elimination(matrix):
    n = get_length(matrix)

    for i in custom_range(0, n):
        if abs(matrix[i][i]) < 1e-9:  
            for j in custom_range(i + 1, n):
                if abs(matrix[j][i]) > 1e-9:
                    matrix[i], matrix[j] = matrix[j], matrix[i]  
                    print(f"Swapped row {i} with row {j}")
                    break

        for j in custom_range(i + 1, n):
            if abs(matrix[j][i]) > 1e-9:  
                factor = matrix[j][i] / matrix[i][i]
                for k in custom_range(i, n + 1):  
                    matrix[j][k] -= factor * matrix[i][k]

        print(f"\nMatrix after elimination row {i + 1}:")
        for row in matrix:
            print([round(x, 4) for x in row])

    solutions = [0] * n
    for i in custom_range(n - 1, -1, -1):  
        sum = matrix[i][n]  
        for j in custom_range(i + 1, n):
            sum -= matrix[i][j] * solutions[j]

        if abs(matrix[i][i]) < 1e-9: 
            if abs(sum) > 1e-9: 
                raise ValueError("The system has no solution.")
            solutions[i] = 0 
        else:
            solutions[i] = sum / matrix[i][i]

    return solutions

aug_matrix = input_augmented_matrix()
if aug_matrix:
    print("Matrix: ")
    for row in aug_matrix:
        row_coefficients = row[:-1]
        constant = row[-1]
        print(custom_join(row_coefficients, " ") + " | " + str(constant))

    solutions = gaussian_elimination(aug_matrix)

    print("\nResult: ")
    for i in custom_range(0, get_length(solutions)):
        print(f"x{i+1} = {solutions[i]}")
