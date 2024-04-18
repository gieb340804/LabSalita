def permutationSort(massiv):
    n = len(massiv)
    
    while True:
        swapped = False
        for i in range(n - 1):
            if massiv[i] > massiv[i+1]:
                temp = massiv[i]
                massiv[i] = massiv[i+1]
                massiv[i+1] = temp
                swapped = True
        if swapped == False:
            break
    return massiv