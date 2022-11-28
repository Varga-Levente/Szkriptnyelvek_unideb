import numpy as np
import pandas as pd

def key(state):
    if(state == 0):
        return 1
    else:
        return 0

def main():
    w, h = 2, 600
    Matrix = [[0 for x in range(w)] for y in range(h)]

    for i in range(0, h):
        Matrix[i][0] = i+1
        Matrix[i][1] = 0

    for i in range(0, h):
        n = i+1
        result = Matrix[n - 1::n]
        for j in range(0, len(result)):
            index = result[j][0]-1
            Matrix[index][1] = key(Matrix[index][1])

    # Select all rows where the second column is 1
    result = np.array(Matrix)[np.array(Matrix)[:,1] == 1]
    check = ""
    for i in range(0, len(result)):
        check+=str(result[i][0])

    df = pd.DataFrame(Matrix, columns = ['Cell','State'])
    df = df.set_index('Cell')
    print(df)
    print("CHECK: "+check)

if __name__ == '__main__':
    main()
