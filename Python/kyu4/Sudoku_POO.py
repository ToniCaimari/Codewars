class Sudoku(object):

    def __init__(self, data):

        self.data = data

    def memory_H(self):

        memoryH = []

        for i in self.data:
            if len(i) == len(self.data):
                for t in i:
                    if t not in memoryH:
                        memoryH.append(t)
                    else:
                        return False
                memoryH = []
            else:
                return False
        return True

    def memory_L(self):

        memoryL = []
        count = 0

        while count < len(self.data):
            for i in self.data:
                if i[count] not in memoryL:
                    memoryL.append(i[count])
                else:
                    return False
            memoryL = []
            count += 1
        return True

    def is_valid(self):

        for i in self.data:
            for t in i:
                if isinstance(t, bool) == True:
                    return False
                else:
                    continue

        if len(self.data) == 1:
            if self.data[0][0] == 1:
                return True
            else:
                return False
        else:
            if self.data[0][len(self.data)-1] == self.data[len(self.data)-1][0]:
                return False

        if Sudoku.memory_H(self) == True:
            if Sudoku.memory_L(self) == True:
                return True
            else:
                return False
        else:
            return False
