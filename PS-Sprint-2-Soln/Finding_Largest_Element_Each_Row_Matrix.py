def largest_elements_each_row(matrix):
    largest_elements = []
    for row in matrix:
        if row:  # Check if the row is not empty
            largest_elements.append(max(row))
        else:
            largest_elements.append(None)  # Handle empty rows
    return largest_elements

print(largest_elements_each_row([[3, 5, 2], [1, 4, 9], [7, 0, 6]]))  # Output: [5, 9, 7]