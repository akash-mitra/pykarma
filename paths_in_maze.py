# show all the paths from (0,0) to (maxr, maxc) in maxr by maxc matrix
# not really done yet....!!!!!

maxc = 3
maxr = 3

def nextMoves(sr, sc):
    if sr == maxr - 1 and sc == maxc - 1:
        return []

    moves = []
    if sr < maxr - 1:
        moves.append((sr+1, sc))
    if sc < maxc - 1:
        moves.append((sr, sc+1))

    return moves


def traverse (ir, ic, path = []):

    path.append((ir, ic))
    print(path)

    for move in nextMoves(ir, ic):
        traverse(*move, path[:])
        # path.pop()

    # if ir == maxr-1 and ic == maxc-1 : print (path)

traverse(0, 0)
