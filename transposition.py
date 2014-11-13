__author__ = 'ste'


def transpose(phrase):  # transpose array and create string for display
    # variables to create array of correct dimensions depending on length of input phrase
    rows = len(phrase) / 2
    columns = 2
    # create 2d array for transposition matrix according to size of input
    matrix = [['' for y in range(rows)] for x in range(columns)]
    cipher = ''
    k = 0
    while k < (len(phrase)):
        for j in range(columns):
            for i in range(rows):
                matrix[j][i] = phrase[k]
                k += 1
    k = 0
    while k < (len(matrix) * len(matrix[x])):
        for j in range(len(matrix[x]) - 1, -1, -1):  # range(start,end,step)
            for i in range(len(matrix) - 1, -1, -1):
                cipher += matrix[i][j]
                k += 1
    return cipher

 # create matrix from the cipher and reverse process to recover original text
def reverse_transpose(cipher):
    if len(cipher)%2!=0:
        cipher+=' '
    i = 0
    rows = len(cipher) / 2
    print len(cipher)
    columns = 2
    output = ''
    matrix = [['' for y in range(rows)] for x in range(columns)]
    output = ''
    while i < len(cipher):
        for j in range(rows - 1, -1, -1):
            for k in range(columns - 1, -1, -1):
                matrix[k][j] = cipher[i]
                i += 1
    k = 0
    while k < (len(matrix) * len(matrix[x])):
        for i in range(columns):
            for j in range(rows):
                output += matrix[i][j]
                k += 1
    output=output[1:]  # remove whitespace padding from end if present
    return output