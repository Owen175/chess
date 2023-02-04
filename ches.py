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
            if mY == self.y + 1 and (mX - self.x) ** 2 == 1 and isOppPiece(self.colour, mX, mY):
                self.x = mX
                self.y = mY
                print('Piece taken')
            if mY == self.y + 2 and self.canDoubleMove == True and mX == self.x:
                self.y = mY
            if mY == self.y + 1 and board[mX][mY] == 0 and mX == self.x:
                self.y = mY
        if self.colour:
            if mY == self.y - 1 and (mX - self.x) ** 2 == 1 and isOppPiece(self.colour, mX, mY):
                self.x = mX
                self.y = mY
            if mY == self.y - 2 and self.canDoubleMove == True and mX == self.x:
                self.y = mY
            if mY == self.y - 1 and board[mX][mY] == 0 and mX == self.x:
                self.y = mY
        # if mX == self.x and mY == self.y:
        #    print('No move')
        #    return False
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


class Castle:
    def __init__(self, x, y, colour):
        self.colour = colour
        self.x = x
        self.y = y
        self.id = 4
        if colour:
            self.id += 6

    def calcPossMoves(self):
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

        return finalPossListDown + finalPossListUp + finalPossListLeft + finalPossListRight

    def move(self, mX, mY):
        moves = self.calcPossMoves()
        print(moves)
        if (mX, mY) in moves:
            print('can move')
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
        for j, comp in enumerate(finalRightUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalRightUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalRightUp.append(comp)
                else:
                    end = True


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
        for j, comp in enumerate(finalRightDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalRightDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalRightDown.append(comp)
                else:
                    end = True

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
        for j, comp in enumerate(finalLeftUp):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalLeftUp.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalLeftUp.append(comp)
                else:
                    end = True


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
        for j, comp in enumerate(finalLeftDown):
            if not end:
                if isOppPiece(self.colour, comp[0], comp[1]):
                    finalLeftDown.append(comp)
                    end = True
                elif board[comp[0]][comp[1]] == 0:
                    finalLeftDown.append(comp)
                else:
                    end = True

        return finalLeftUp + finalLeftDown + finalRightDown + finalRightUp

    def move(self, mX, mY):
        moves = self.calcPossMoves()
        print(moves)
        if (mX, mY) in moves:
            print('can move')
            self.x = mX
            self.y = mY
            return True
        else:
            return False

def isOppPiece(colour, x, y):
    if board[x][y] != 0:
        if board[x][y].colour != colour:
            return True
    return False


def promote(colour, x, y):
    pass


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
    print(pos, board[pos[0]][pos[1]])
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

spritesheet = pygame.image.load('pieces.png').convert_alpha()

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
turn = True  # White
pos1 = None
pos2 = None

for x in range(len(board)):
    for y in range(len(board)):
        if board[x][y] != 0:
            gameDisplay.blit(spritesheet, (x * size + (size - 83) / 2, (7 - y) * size + (size - 83) / 2),
                             cells[board[x][y].id])
pygame.display.update()
print('------------------')
[print(row) for row in board]
print('------------------')
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = getCoors(pygame.mouse.get_pos())
            if pos1 is not None:
                pos2 = pos

                if board[pos1[0]][pos1[1]].move(pos2[0], pos2[1]):
                    turn = not turn
                    x, y = board[pos1[0]][pos1[1]].x, board[pos1[0]][pos1[1]].y
                    # print(x,y)
                    print(board[pos1[0]][pos1[1]], '-=----=-=-=-=-=====')
                    board[pos2[0]][pos2[1]] = board[pos1[0]][pos1[1]]
                    board[pos1[0]][pos1[1]] = 0
                    print(board[pos2[0]][pos2[1]])
                    print(board[pos1[0]][pos1[1]], '-=----=-=-=-=-=====')
                    pygame.draw.rect(gameDisplay, boardColours[x][7 - y], [size * (x), size * (7 - y), size, size])
                    # print(board[pos2[0]][pos2[1]], 'pos')
                    # [print(row) for row in board]
                    pygame.draw.rect(gameDisplay, boardColours[pos1[0]][7 - pos1[1]],
                                     [size * (pos1[0]), size * (7 - pos1[1]), size, size])
                    gameDisplay.blit(spritesheet,
                                     (pos2[0] * size + (size - 83) / 2, (7 - pos2[1]) * size + (size - 83) / 2),
                                     cells[board[pos2[0]][pos2[1]].id])
                    # if (8 * y + x) % 2 == 0:
                    #     pygame.draw.rect(gameDisplay, white, [size, size, size, size])
                    # else:
                    #     pygame.draw.rect(gameDisplay, black, [size, size, size, size])
                    pygame.display.update()

                else:
                    print('invalid')
                pos1 = None

            else:
                if board[pos[0]][pos[1]] == 0:
                    pos1 = None

                else:
                    print(board[pos[0]][pos[1]])
                    pos1 = pos
    # draw((0,0), gameDisplay)
