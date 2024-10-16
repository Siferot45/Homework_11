#Data validation
def input_validate(prompt):
    
    while True:
        try:
            return int(input(prompt))   
        except:
            print("Error: Enter an integer.")
#Building a matrix            
def get_matri(n,m,value):
    
    if n <= 0 or m <= 0:
        return []
    
    matrix = []
    
    for x in range(n):
        current_sting = []
        
        for y in range(m):
            current_sting.append(value)
            
        matrix.append(current_sting)
    return matrix
            
string = input_validate("Enter the number of rows of the matrix: ")
column = input_validate("Enter the number of columns of the matrix: ")
value = input_validate("Enter the value of the matrix: ")

result = get_matri(string, column, value)
print(result)