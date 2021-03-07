def valid_solution(board):
    memoryH = []
    memoryL = []
    count = 0
    for i in board:
        for t in i:
            if t not in memoryH:
                memoryH.append(t)
            else:
                return False
        memoryH = []
    while count < 9:
        for i in board:
            if i[count] not in memoryL:
                memoryL.append(i[count])
            else:
                return False
        count += 1
    if board[0][2] == board[1][1]:
        return False
    return True
