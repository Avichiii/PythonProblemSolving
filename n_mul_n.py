# multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(size):
    columns = []
    for i in range(1,size+1):
        rows = []
        for j in range(1,size+1):
            rows.append(i*j)
        columns.append(rows)
    print(columns)

multiplication_table(3)