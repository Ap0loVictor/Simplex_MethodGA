def findPivots(matriz):
    # finding a pivot collumn:
    pivot_collumn = []
    first_line = []
    for i in range (len(matriz[0])):
       first_line.append(matriz[0][i]) 
    
    pivot_collumn_number = first_line[0]

    for i in range(len(first_line)):
        if pivot_collumn_number > first_line[i]:
            pivot_collumn_number = first_line[i] # searching the smallest number
            pivot_collumn_index = i # Finding a pivot collumn index
    if pivot_collumn_number > 0:
        return 0

    for i in range(len(matriz)): # Make the pivot collumn
        for j in range(len(matriz[i])):
            if j==pivot_collumn_index:
                pivot_collumn.append(matriz[i][pivot_collumn_index])
    # print(f"pivot collumn: {pivot_collumn}")

    # pivot line:
    last_index = len(matriz[0])-1
    last_collumn = []

    for i in range(len(matriz)): # Make the last collumn
        for j in range(len(matriz[i])):
            if j==last_index:
                last_collumn.append(matriz[i][last_index])
    
    for i in range(len(last_collumn)):
        if last_collumn[i] != 0:
            last_collumn[i] = last_collumn[i]/pivot_collumn[i] # Discovering the smallest number
    #print(last_collumn)

    smallest_number = last_collumn[1]
    pivot_line_index = 1
    for i in range(len(last_collumn)):
        if smallest_number > last_collumn[i] and i>1:
            smallest_number = last_collumn[i] # searching the smallest number
            pivot_line_index = i # Finding the pivot line index

    pivot_line = []
    for i in range(len(matriz[pivot_line_index])): # making pivot line
        pivot_line.append(matriz[pivot_line_index][i])
    # print(f"pivot line: {pivot_line}")
    
    pivot_element = pivot_line[pivot_collumn_index] # finding pivot element
    # print(f"pivot element: {pivot_element}")

    return pivot_collumn , pivot_line, pivot_element,  pivot_line_index


def newLines(matriz):
    piv_co, piv_li, piv_el, piv_li_in  = findPivots(matriz)
    new_piv_li = []
    
    for i in range(len(piv_li)): # make a new pivot line
        new_piv_li.append(round(piv_li[i]/piv_el,3))
    #print(new_piv_li)
    other_lines = []
    new_matrix = []

    for i in range(len(piv_co)):  # Making the others lines
        old_line = matriz[i]
        for j in range(len(piv_li)):
            other_lines.append( round(-piv_co[i] * new_piv_li[j] + old_line[j],3))
        if i == piv_li_in:
            new_matrix.append(new_piv_li)
        else:
            new_matrix.append(other_lines)
        other_lines = []
    
    for i in range(len(piv_co)):
        print(new_matrix[i])
    return new_matrix

def maximizarFuncao(matriz):
    first_line = []
    negative = 0
    for i in range (len(matriz[0])):
       first_line.append(matriz[0][i]) 
    for i in range(len(first_line)):
        if first_line[i]<0:
            negative = 1
            new_matriz = newLines(matriz)
            break
    if negative == 0:
        return matriz, negative
    else:
        return new_matriz, negative

def main():
    matriz = [
        [1, -1, -1.5, -2, 0, 0, 0, 0],
        [0, 8,    5,   2, 1, 0, 0, 120],
        [0, 5,   10,   4, 0, 1, 0, 400],
        [0, 0.7,  1,   2, 0, 0, 1, 80]
    ]

    negative = 1
    i = 1
    while negative == 1:
        print(f"\nInteraction {i}:")
        matriz, negative = maximizarFuncao(matriz)
        i+=1
    print("\nNão há mais iterações\n")

if __name__ == "__main__":
    main()
