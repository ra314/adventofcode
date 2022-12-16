import numpy as np
myfile = open("input.txt")
content = myfile.read()

numbers = list(map(int, content.splitlines()[0].split(',')))

boards = []

line_num = 1
for i in range((len(content.splitlines())-1)//6):
    array = []
    for line in content.splitlines()[line_num+1:line_num+6]:
        array.append((list(map(int, line.split()))))
    boards.append(np.array(array))
    line_num += 6


def g(boards):
    a = np.array(list(map(np.sum, boards)))
    return sum(a == (-10*25))

def f():
    winner = None
    for num in numbers:
        for board in boards:
            board[board == num] = -1
            if (-5 in board.sum(axis = 1)) or (-5 in board.sum(axis = 0)):
                if g(boards) == 99:
                    winner = board
                    return (winner[winner != -1].sum() * num)
                else:
                    board *= 0
                    board -= 10
                
print(f())
