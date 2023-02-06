import pygame


class Pawn:
    def __init__(self, x, y, colour):
        self.canDoubleMove = True
        self.x = x
        self.y = y
        self.colour = colour
        self.id = 5
        if colour:
            self.id += 6

    def move(self, mX, mY):
        initX = self.x
        initY = self.y

        if not self.colour:
            if self.colour == turn:
                if mY == self.y + 1 and (mX - self.x) ** 2 == 1 and isOppPiece(self.colour, mX, mY):
                    self.x = mX
                    self.y = mY
                    print('Piece taken')
                if mY == self.y + 2 and self.canDoubleMove == True and mX == self.x:
                    self.y = mY
                if mY == self.y + 1 and board[mX][mY] == 0 and mX == self.x:
                    self.y = mY
        if self.colour:
            if self.colour == turn:
                if mY == self.y - 1 and (mX - self.x) ** 2 == 1 and isOppPiece(self.colour, mX, mY):
                    self.x = mX
                    self.y = mY
                if mY == self.y - 2 and self.canDoubleMove == True and mX == self.x:
                    self.y = mY
                if mY == self.y - 1 and board[mX][mY] == 0 and mX == self.x:
                    self.y = mY

        if self.x == initX and self.y == initY:
            print('Invalid move')
            return False
        if self.x < 0 or self.x > 7 or self.y < 0 or self.y > 7:
            self.x = initX
            self.y = initY
            print('Out of bounds')
            return False

        if self.colour and self.y == 7:
            promote(self.colour, self.x, self.y)
        elif self.colour is False and self.y == 0:
            promote(self.colour, self.x, self.y)

        self.canDoubleMove = False
        return True

    def calcPossMoves(self):
        moves = []
        if self.colour:
            if self.y > 0:
                if self.x > 0:
                    if isOppPiece(self.colour, self.x - 1, self.y - 1):
                        moves.append((self.x - 1, self.y - 1))
                if self.x < 7:
                    if isOppPiece(self.colour, self.x + 1, self.y - 1):
                        moves.append((self.x + 1, self.y - 1))
                moves.append((self.x, self.y - 1))
        else:
            if self.y < 7:
                if self.x < 7:
                    if isOppPiece(self.colour, self.x + 1, self.y + 1):
                        moves.append((self.x + 1, self.y + 1))
                if self.x > 0:
                    if isOppPiece(self.colour, self.x - 1, self.y + 1):
                        moves.append((self.x - 1, self.y + 1))
                moves.append((self.x, self.y + 1))

        return '_', moves


class Castle:
    def __init__(self, x, y, colour):
        self.colour = colour
        self.x = x
        self.y = y
        self.id = 4
        if colour:
            self.id += 6

    def calcPossMoves(self):
        movables = []
        cont = True
        count = 0
        possListRight = []
        while cont:
            if self.x < 7:
                count += 1
                if self.x + count == 7:
                    cont = False
                possListRight.append((self.x + count, self.y))
            else:
                cont = False
        finalPossListRight = []
        end = False
        for j, comp in enumerate(possListRight):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListRight.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListRight.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListLeft = []
        while cont:
            if self.x > 0:
                count += 1
                if self.x - count == 0:
                    cont = False
                possListLeft.append((self.x - count, self.y))
            else:
                cont = False
        finalPossListLeft = []
        end = False
        for j, comp in enumerate(possListLeft):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListLeft.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListLeft.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListUp = []
        while cont:
            if self.y < 7:
                count += 1
                if self.y + count == 7:
                    cont = False
                possListUp.append((self.x, self.y + count))
            else:
                cont = False
        finalPossListUp = []
        end = False
        for j, comp in enumerate(possListUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListUp.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListDown = []
        while cont:
            if self.y > 0:
                count += 1
                if self.y - count == 0:
                    cont = False
                possListDown.append((self.x, self.y - count))
            else:
                cont = False
        finalPossListDown = []
        end = False
        for j, comp in enumerate(possListDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListDown.append(comp)
                else:
                    end = True
                movables.append(comp)

        return finalPossListDown + finalPossListUp + finalPossListLeft + finalPossListRight, movables

    def move(self, mX, mY):
        moves, _ = self.calcPossMoves()
        if (mX, mY) in moves:
            if self.colour == turn:
                self.x = mX
                self.y = mY
            return True
        else:
            return False


class Bishop:
    def __init__(self, x, y, colour):
        self.colour = colour
        self.x = x
        self.y = y
        self.id = 2
        if colour:
            self.id += 6

    def calcPossMoves(self):
        movables = []
        rightUp = []
        cont = True
        count = 0
        while cont:
            if self.x < 7 and self.y < 7:
                count += 1
                if self.x + count == 7 or self.y + count == 7:
                    cont = False
                rightUp.append((self.x + count, self.y + count))
            else:
                cont = False
        finalRightUp = []
        end = False
        for j, comp in enumerate(rightUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalRightUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalRightUp.append(comp)
                else:
                    end = True
                movables.append(comp)

        rightDown = []
        cont = True
        count = 0
        while cont:
            if self.x < 7 and self.y > 0:
                count += 1
                if self.x + count == 7 or self.y - count == 0:
                    cont = False
                rightDown.append((self.x + count, self.y - count))
            else:
                cont = False
        finalRightDown = []
        end = False
        for j, comp in enumerate(rightDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalRightDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalRightDown.append(comp)
                else:
                    end = True
                movables.append(comp)

        leftUp = []
        cont = True
        count = 0
        while cont:
            if self.x > 0 and self.y < 7:
                count += 1
                if self.x - count == 0 or self.y + count == 7:
                    cont = False
                leftUp.append((self.x - count, self.y + count))
            else:
                cont = False
        finalLeftUp = []
        end = False
        for j, comp in enumerate(leftUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalLeftUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalLeftUp.append(comp)
                else:
                    end = True
                movables.append(comp)

        leftDown = []
        cont = True
        count = 0
        while cont:
            if self.x > 0 and self.y > 0:
                count += 1
                if self.x - count == 0 or self.y - count == 7:
                    cont = False
                leftDown.append((self.x - count, self.y - count))
            else:
                cont = False
        finalLeftDown = []
        end = False
        for j, comp in enumerate(leftDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalLeftDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalLeftDown.append(comp)
                else:
                    end = True
                movables.append(comp)
        return finalLeftUp + finalLeftDown + finalRightDown + finalRightUp, movables

    def move(self, mX, mY):
        moves, _ = self.calcPossMoves()
        if (mX, mY) in moves:
            if self.colour == turn:
                self.x = mX
                self.y = mY
            return True
        else:
            return False


class Queen:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.id = 1
        if colour:
            self.id += 6

    def calcPossMoves(self):
        movables = []
        rightUp = []
        cont = True
        count = 0
        while cont:
            if self.x < 7 and self.y < 7:
                count += 1
                if self.x + count == 7 or self.y + count == 7:
                    cont = False
                rightUp.append((self.x + count, self.y + count))
            else:
                cont = False
        finalRightUp = []
        end = False
        for j, comp in enumerate(rightUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalRightUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalRightUp.append(comp)
                else:
                    end = True
                movables.append(comp)

        rightDown = []
        cont = True
        count = 0
        while cont:
            if self.x < 7 and self.y > 0:
                count += 1
                if self.x + count == 7 or self.y - count == 0:
                    cont = False
                rightDown.append((self.x + count, self.y - count))
            else:
                cont = False
        finalRightDown = []
        end = False
        for j, comp in enumerate(rightDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalRightDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalRightDown.append(comp)
                else:
                    end = True

                movables.append(comp)

        leftUp = []
        cont = True
        count = 0
        while cont:
            if self.x > 0 and self.y < 7:
                count += 1
                if self.x - count == 0 or self.y + count == 7:
                    cont = False
                leftUp.append((self.x - count, self.y + count))
            else:
                cont = False
        finalLeftUp = []
        end = False
        for j, comp in enumerate(leftUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalLeftUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalLeftUp.append(comp)
                else:
                    end = True
                movables.append(comp)

        leftDown = []
        cont = True
        count = 0
        while cont:
            if self.x > 0 and self.y > 0:
                count += 1
                if self.x - count == 0 or self.y - count == 7:
                    cont = False
                leftDown.append((self.x - count, self.y - count))
            else:
                cont = False
        finalLeftDown = []
        end = False
        for j, comp in enumerate(leftDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalLeftDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalLeftDown.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListRight = []
        while cont:
            if self.x < 7:
                count += 1
                if self.x + count == 7:
                    cont = False
                possListRight.append((self.x + count, self.y))
            else:
                cont = False
        finalPossListRight = []
        end = False
        for j, comp in enumerate(possListRight):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListRight.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListRight.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListLeft = []
        while cont:
            if self.x > 0:
                count += 1
                if self.x - count == 0:
                    cont = False
                possListLeft.append((self.x - count, self.y))
            else:
                cont = False
        finalPossListLeft = []
        end = False
        for j, comp in enumerate(possListLeft):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListLeft.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListLeft.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListUp = []
        while cont:
            if self.y < 7:
                count += 1
                if self.y + count == 7:
                    cont = False
                possListUp.append((self.x, self.y + count))
            else:
                cont = False
        finalPossListUp = []
        end = False
        for j, comp in enumerate(possListUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListUp.append(comp)
                else:
                    end = True
                movables.append(comp)

        cont = True
        count = 0
        possListDown = []
        while cont:
            if self.y > 0:
                count += 1
                if self.y - count == 0:
                    cont = False
                possListDown.append((self.x, self.y - count))
            else:
                cont = False
        finalPossListDown = []
        end = False
        for j, comp in enumerate(possListDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalPossListDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalPossListDown.append(comp)
                else:
                    end = True
                movables.append(comp)

        return finalPossListDown + finalPossListUp + finalPossListLeft + finalPossListRight + finalRightDown + finalRightUp + finalLeftUp + finalLeftDown, movables

    def move(self, mX, mY):
        moves, _ = self.calcPossMoves()
        if (mX, mY) in moves:
            if self.colour == turn:
                self.x = mX
                self.y = mY
            return True
        else:
            return False


class Knight:
    def __init__(self, x, y, colour):
        self.colour = colour
        self.x = x
        self.y = y
        self.id = 3
        if colour:
            self.id += 6

    def calcPossMoves(self):
        moves = [(self.x + 1, self.y + 2), (self.x - 1, self.y + 2), (self.x - 1, self.y - 2), (self.x + 1, self.y - 2),
                 (self.x + 2, self.y + 1),
                 (self.x + 2, self.y - 1), (self.x - 2, self.y + 1), (self.x - 2, self.y - 1)]
        possMoves = []
        movables = []
        for i, move in enumerate(moves):
            if 7 >= move[0] >= 0 and 7 >= move[1] >= 0:
                movables.append(move)
                if board[move[0]][move[1]] == 0 or isOppPiece(self.colour, move[0], move[1]):
                    possMoves.append(move)

        return possMoves, movables

    def move(self, mX, mY):
        moves, _ = self.calcPossMoves()
        if (mX, mY) in moves:
            if self.colour == turn:
                self.x = mX
                self.y = mY
            return True
        else:
            return False


class King:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.id = 0
        if colour:
            self.id += 6

    def calcPossMoves(self):
        moves = [(self.x + 1, self.y), (self.x + 1, self.y + 1), (self.x, self.y + 1), (self.x - 1, self.y),
                 (self.x + 1, self.y - 1), (self.x - 1, self.y - 1), (self.x - 1, self.y + 1), (self.x, self.y - 1)]
        possMoves = []
        movableSquares = []
        for i, move in enumerate(moves):
            if 7 >= move[0] >= 0 and 7 >= move[1] >= 0:
                if not checkForCheck(move, self.colour):
                    movableSquares.append(move)
                    if board[move[0]][move[1]] == 0 or isOppPiece(self.colour, move[0], move[1]):
                        possMoves.append(move)

        return possMoves, movableSquares

    def move(self, mX, mY):
        moves, _ = self.calcPossMoves()
        if (mX, mY) in moves:
            if self.colour == turn:
                self.x = mX
                self.y = mY
            return True
        else:
            return False


def checkForCheck(move, colour):
    x, y = move
    diagonals = checkDiagonals(move, colour)
    horizontals = checkHorizontals(move, colour)
    lShapes = checkLShapes(move)

    if not colour:
        if y < 7 and x > 0:
            if type(board[x - 1][y + 1]) == Pawn and board[x - 1][y + 1].colour:
                return True
        if y < 7 and x < 7:
            if type(board[x + 1][y + 1]) == Pawn and board[x + 1][y + 1].colour:
                return True

        for danger in diagonals:
            tp = type(board[danger[0]][danger[1]])
            if tp == Bishop or tp == Queen:
                if board[danger[0]][danger[1]].colour:
                    return True

        for danger in horizontals:
            tp = type(board[danger[0]][danger[1]])
            if tp == Castle or tp == Queen:
                if board[danger[0]][danger[1]].colour:
                    return True

        for danger in lShapes:
            tp = type(board[danger[0]][danger[1]])
            if tp == Knight:
                if board[danger[0]][danger[1]].colour:
                    return True
    else:
        if y > 0 and x > 0:
            if type(board[x - 1][y - 1]) == Pawn and not board[x - 1][y - 1].colour:
                return True
        if y > 0 and x < 7:
            if type(board[x + 1][y - 1]) == Pawn and not board[x + 1][y - 1].colour:
                return True

        for danger in diagonals:
            tp = type(board[danger[0]][danger[1]])
            if tp == Bishop or tp == Queen:
                if not board[danger[0]][danger[1]].colour:
                    return True

        for danger in horizontals:
            tp = type(board[danger[0]][danger[1]])
            if tp == Castle or tp == Queen:
                if not board[danger[0]][danger[1]].colour:
                    return True

        for danger in lShapes:
            tp = type(board[danger[0]][danger[1]])
            if tp == Knight:
                if not board[danger[0]][danger[1]].colour:
                    return True
    return False

def checkLShapes(move):
    x, y = move
    places = [(x + 1, y + 2), (x - 1, y + 2), (x - 1, y - 2), (x + 1, y - 2),
              (x + 2, y + 1),
              (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1)]

    onBoard = []
    for place in places:
        if 7 > place[0] > 0 and 7 > place[1] > 0:
            onBoard.append(place)

    return onBoard


def checkHorizontals(move, colour):
    x, y = move
    cont = True
    horizontalList = []
    while x < 7 and cont:
        x += 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                horizontalList.append((x, y))

    x, y = move
    cont = True
    while x > 0 and cont:
        x -= 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                horizontalList.append((x, y))

    x, y = move
    cont = True
    while y > 0 and cont:
        y -= 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                horizontalList.append((x, y))

    x, y = move
    cont = True
    while y < 7 and cont:
        y += 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                horizontalList.append((x, y))

    return horizontalList


def checkDiagonals(move, colour):
    x, y = move
    cont = True
    diagonalList = []
    while x < 7 and y < 7 and cont:
        x += 1
        y += 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                diagonalList.append((x, y))

    x, y = move
    cont = True
    while x > 0 and y < 7 and cont:
        x -= 1
        y += 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                diagonalList.append((x, y))

    x, y = move
    cont = True
    while x > 0 and y > 0 and cont:
        x -= 1
        y -= 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                diagonalList.append((x, y))

    x, y = move
    cont = True
    while x < 7 and y > 0 and cont:
        x += 1
        y -= 1
        if board[x][y] != 0:
            if type(board[x][y]) == King and board[x][y].colour == colour:
                pass
            else:
                cont = False
                diagonalList.append((x, y))

    return diagonalList


# def checkForCheckmate(black, white, blak):


# To check for checkmate, create another grid for each side to check
# whether a piece can move there. [0, 1, 0, 1] etc. 0 being cant move, 1 being can. This makes it easy to check
# whether you can take the piece threatening the king, or if you can block
# Check for check then checkmate. If checkmate but not check, stalemate.
# Need to make it so you cant ignore checkmate


def makeMovableGrids():
    blackList = []
    whiteList = []
    for y in range(8):
        for x in range(8):
            if board[x][y] != 0:
                if board[x][y].colour == True:
                    _, moves = board[x][y].calcPossMoves()
                    blackList.extend(moves)
                else:
                    _, moves = board[x][y].calcPossMoves()
                    whiteList.extend(moves)
    return list(set(blackList)), list(set(whiteList))


def isOppPiece(colour, x, y):
    if board[x][y] != 0:
        if board[x][y].colour != colour:
            return True
    return False


def promote(colour, x, y):
    pass


def findKings(colour):
    for y in range(8):
        for x in range(8):
            if board[x][y] != 0:
                if type(board[x][y]) == King and board[x][y].colour == colour:
                    return (x, y)


def getCoors(pos):
    pos = (pos[0] // size, pos[1] // size)
    if pos[0] < 0:
        pos = (0, pos[1])
    if pos[0] > 7:
        pos = (7, pos[1])
    if pos[1] < 0:
        pos = (pos[0], 0)
    if pos[1] > 7:
        pos = (pos[0], 7)

    pos = (pos[0], 7 - pos[1])
    return pos


# Colour is bool
board = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]

# Board is [x][y]

for i in range(len(board)):
    board[i][1] = Pawn(i, 1, False)
    board[i][6] = Pawn(i, 6, True)

board[7][7] = Castle(7, 7, True)
board[0][7] = Castle(0, 7, True)
board[7][0] = Castle(7, 0, False)
board[0][0] = Castle(0, 0, False)

board[6][7] = Bishop(6, 7, True)
board[1][7] = Bishop(1, 7, True)
board[6][0] = Bishop(6, 0, False)
board[1][0] = Bishop(1, 0, False)

board[2][7] = Knight(2, 7, True)
board[5][7] = Knight(5, 7, True)
board[2][0] = Knight(2, 0, False)
board[5][0] = Knight(5, 0, False)

board[3][0] = Queen(3, 0, False)
board[3][7] = Queen(3, 7, True)

board[4][0] = King(4, 0, False)
board[4][7] = King(4, 7, True)
pygame.init()
# set color with rgb
white, black = (232, 235, 239), (125, 135, 150)

# set display
gameDisplay = pygame.display.set_mode((1000, 1000))

# caption
pygame.display.set_caption("Chess")

# Size of squares
size = 125

# board length, must be even
boardLength = 8
gameDisplay.fill(white)

count = 0
boardColours = []
for i in range(0, boardLength):
    bcTemp = []
    for z in range(0, boardLength):
        # check if current loop value is even
        if count % 2 == 0:
            pygame.draw.rect(gameDisplay, white, [size * z, size * i, size, size])
            bcTemp.append(white)
        else:
            pygame.draw.rect(gameDisplay, black, [size * z, size * i, size, size])
            bcTemp.append(black)
        count += 1
    count -= 1
    boardColours.append(bcTemp)

pygame.display.update()

spritesheet = pygame.image.load('../../../OneDrive - Ridgeway Education Trust/chess/pieces.png').convert_alpha()

cols = 6
rows = 2
cell_count = cols * rows

rect = spritesheet.get_rect()
w = cell_width = rect.width // cols
h = cell_height = rect.height // rows

cells = list([(i % cols * w, i // cols * h, w, h) for i in range(cell_count)])
# 83x83


# 0 - White king
# 1 - White queen
# 2 - White bishop
# 3 - White knight
# 4 - White castle
# 5 - White pawn
# + 6 for black


pygame.display.update()

gameExit = False
turn = False  # White is false
pos1 = None
pos2 = None
nextCheck = False
for x in range(len(board)):
    for y in range(len(board)):
        if board[x][y] != 0:
            gameDisplay.blit(spritesheet, (x * size + (size - 83) / 2, (7 - y) * size + (size - 83) / 2),
                             cells[board[x][y].id])
pygame.display.update()
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = getCoors(pygame.mouse.get_pos())
            if pos1 is not None:
                pos2 = pos
                if turn == board[pos1[0]][pos1[1]].colour:
                    if board[pos1[0]][pos1[1]].move(pos2[0], pos2[1]):
                        noDraw = False
                        oG2 = board[pos2[0]][pos2[1]]
                        board[pos2[0]][pos2[1]] = board[pos1[0]][pos1[1]]
                        board[pos1[0]][pos1[1]] = 0
                        potential_checked_king_pos = findKings(not turn)
                        if nextCheck:
                            checkedpos = findKings(checkColour)
                            if checkForCheck(checkedpos, checkColour):
                                noDraw = True
                                print('Still in check')
                                board[pos2[0]][pos2[1]].x = pos1[0]
                                board[pos2[0]][pos2[1]].y = pos1[1]
                            else:
                                nextCheck = False

                        print(checkForCheck(potential_checked_king_pos, not turn), 'CFC')
                        if checkForCheck(potential_checked_king_pos, not turn):
                            print('check')
                            nextCheck = True
                            checkColour = not turn
                            if turn == True:
                                print('White King in check')
                            else:
                                print('Black King in check')

                        if not noDraw:
                            x, y = board[pos2[0]][pos2[1]].x, board[pos2[0]][pos2[1]].y

                            pygame.draw.rect(gameDisplay, boardColours[x][7 - y],
                                             [size * (x), size * (7 - y), size, size])
                            pygame.draw.rect(gameDisplay, boardColours[pos1[0]][7 - pos1[1]],
                                             [size * (pos1[0]), size * (7 - pos1[1]), size, size])
                            gameDisplay.blit(spritesheet,
                                             (pos2[0] * size + (size - 83) / 2, (7 - pos2[1]) * size + (size - 83) / 2),
                                             cells[board[pos2[0]][pos2[1]].id])

                            pygame.display.update()
                            turn = not turn
                        else:
                            board[pos1[0]][pos1[1]] = board[pos2[0]][pos2[1]]
                            board[pos2[0]][pos2[1]] = oG2

                        #May need to revert the x, y in the class too.
                        # blackG, whiteG = makeMovableGrids()
                        # checkForCheckmate(blackG, whiteG)

                else:
                    print('invalid')
                pos1 = None

            else:
                if board[pos[0]][pos[1]] == 0:
                    pos1 = None

                else:
                    pos1 = pos