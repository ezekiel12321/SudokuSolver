def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end='')
        print()


def empty_cell(array, emptySave):
    for x in range(9):
        for y in range(9):
            if array[x][y] == 0:
                emptySave[0] = x
                emptySave[1] = y
                return True
    return False


def unique_col_row(array, row, col, value):
    for x in range(9):
        if array[row][x] == value:
            ##print("row value")
            return False

    for x in range(9):
        if array[x][col] == value:
            # print("col value")
            return False

    for x in range(3):
        for y in range(3):
            if array[(row - row % 3) + x][(col - col % 3) + y] == value:
                return False
    return True


def board_complete(array):
    for x in range(9):
        for y in range(9):
            if array[x][y] != 0:
                return False
    return True


def back_tracking(array):
    emptySave = [0, 0]

    if not empty_cell(array, emptySave):
        return True
    empty_cell(array, emptySave)

    rowVal = emptySave[0]
    colVal = emptySave[1]
    #print("empty cell at " + str(rowVal) + " " + str(colVal))

    for x in range(1, 10):
        if unique_col_row(array, rowVal, colVal, x):
            # print("It is unique")
            array[rowVal][colVal] = x
            # print("testing rowVal / colVal" + str(rowVal) + str(colVal))
            if back_tracking(array):
                return True
            array[rowVal][colVal] = 0

    return False





if __name__ == '__main__':

    Array = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 3, 6, 0, 0, 0, 0, 0],
             [0, 7, 0, 0, 9, 0, 2, 0, 0],
             [0, 5, 0, 0, 0, 7, 0, 0, 0],
             [0, 0, 0, 0, 4, 5, 7, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 3, 0],
             [0, 0, 1, 0, 0, 0, 0, 6, 8],
             [0, 0, 1, 0, 0, 0, 0, 7, 8],
             [0, 9, 0, 0, 0, 0, 4, 0, 0]]


    back_tracking(Array)
    print_grid(Array)


