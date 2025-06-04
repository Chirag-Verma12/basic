def righttriangle(nrows):
    '''
    objective: to print right triangle
    input parameter: nrows - intefer value
    return value: none
    '''

    for i in range(1, nrows + 1):
        print('*' * i)

def invertedtriangle(nrows):
        '''
        objective: to print inverted triangle
        input parameter: nrows - integer value
        return value: none
        '''

        nspace = 0
        nstars = 2 * nrows -1
        for i in range(1, nrows+1):
            print(' ' * nspace + '*' * nstars)
            nstars -= 2
            nspace += 1