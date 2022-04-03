from game_of_life import Board, checker_helper
import pygame

pygame.init()  # to start making a pygame

# for start we want to make a screen for our game that will be 300x300
screen = pygame.display.set_mode([300, 300])
board_obj = Board()
random_board = board_obj.random_the_board_inside().board
screen.fill((255, 255, 255))
flag = True


# board_obj = [[0 for _ in range(100)] for x in range(100)] # another type of board that i haven't use
# for i in range(0, 100 - 1):
#     for j in range(0, 100 - 1):
#         board_obj[i][j] = random.randint(0, 1)


def createSquare(x, y, color):  # the func will help me make a squares on the board
    pygame.draw.rect(screen, color, [x, y, 10, 10])  # 10x10 is the size of the square


def checker_sqr_draw(
        board):  # this func will help us to print the board according to the cells size we already determined
    # it will go threw the matrix and give each cell a color
    y = 0  # the x, y will help us to draw the square in the right cooardintes we need to equte
    # to zero the the jump will beetween will be in the right way
    for row in range(len(board) - 1):
        x = 0
        for item in range(len(board[0]) - 1):
            if board[row][item] == 0:
                createSquare(x, y, (255, 20, 147))
            else:
                createSquare(x, y, (0, 0, 255))

            x += 10
        y += 10
    pygame.display.update()
    pygame.display.flip()


def checker(board):  # the func will send each cell to the helper and fix the board
    for row in range(len(board) - 1):
        for item in range(len(board[0]) - 1):
            board = checker_helper(row, item, board)
            checker_sqr_draw(board)


def set_text(string, coordx, coordy, fontSize):  # Function to set text

    font = pygame.font.Font('freesansbold.ttf', fontSize)
    # (0, 0, 0) is black, to make black text
    text = font.render(string, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)


# put the text to the screen get helped by the internet
totalText = set_text("welcome to the game of life!", 150, 150, 14)
for_start = set_text("To start hold spacebar", 150, 170, 14)
screen.blit(totalText[0], totalText[1])
screen.blit(for_start[0], for_start[1])
pygame.display.update()

regularboard = [
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1]]

shanatova = pygame.image.load("shanatova.jpg")

while flag:
    screen.blit(shanatova, (50, 150))

    for event in pygame.event.get():  # pygame library have alot of events that already have been written for us

        if event.type == pygame.QUIT:  # help the user get out of the game by clicking close button
            flag = False

        keys = pygame.key.get_pressed()  # wait for the player key press

        if keys[pygame.K_SPACE]:  # space will make the game start
            checker(regularboard)  # not random but recommand to open the random one beneth
            # checker(random_board) #space will make the game start with the random board that the code making with class board

        elif keys[pygame.K_ESCAPE]:  # escape make it get out
            flag = False

            # if event.key == pygame.K_ESCAPE:
            #     flag = False

pygame.quit()
