def transpose():

    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    Y = [[5,8,1],
        [6,7,3],
        [4,5,9]]

    # X = input('enter the first matrix\n')
    # Y = input('enter the second matrix\n')

    result = [[0,0,0],
             [0,0,0],
             [0,0,0]]

    trans = [[0,0,0],
             [0,0,0],
             [0,0,0]]



    for i in range(len(X)):
        for j in range (len(X[0])):

            result [i][j] = X[i][j] + Y[i][j]

    print('addition of two matrices\n')

    for r in result:
    
        print(r)

    print('Transpose of two matrices\n')
    
    for i in range(len(result)):
        
        for j in range (len(result[0])):

            trans [j][i] = result [i][j]
    for R in trans:

        print(R)

transpose()
