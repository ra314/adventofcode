ll = [x for x in open('input.txt').read().strip().split('\n')]

numbers = ll[0]
boards = [[y.split() for y in x.split("\n")] for x in open('input.txt').read().strip().split('\n\n')][1:]

def checkwin(board):
    for i in range(5):
        works = True
        for j in range(5):
            if board[i][j] is not None:
                works = False
        if works:
            return True
    for i in range(5):
        works = True
        for j in range(5):
            if board[j][i] is not None:
                works = False
        if works:
            return True
    works = True
    for j in range(5):
        if board[j][j] is not None:
            works = False
    if works:
        return True
    works = True
    for j in range(5):
        if board[j][4-j] is not None:
            works = False
    if works:
        return True
    return False


for number in numbers.split(","):
    for board in boards:
        for line in board:
            for i in range(len(line)):
                if line[i] == number:
                    line[i] = None
        if checkwin(board):
            un = 0
            for line in board:
                for x in line:
                    if x is not None:
                        un += int(x)
            print(un*int(number))
            raise Exception("done")

