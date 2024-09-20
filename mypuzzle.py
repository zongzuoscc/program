import pygame
import sys
import random
from pygame.locals import *

# 游戏设置
background_color = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30

# 定义拼图碎片的大小和数量（默认3x3）
ROWS, COLS = 3, 3
cell_nums = ROWS * COLS
max_rand_time = 100

# 初始化
pygame.init()
mainClock = pygame.time.Clock()

# 加载图片
gameImage = pygame.image.load('star.jpg')
gameRect = gameImage.get_rect()

# 设置窗口
windowSurface = pygame.display.set_mode((800, 800))
pygame.display.set_caption('拼图游戏')

cellWidth = int(gameRect.width / ROWS)
cellHeight = int(gameRect.height / ROWS)

# 完成标志
finish = False
show_original = False  # 是否显示原图的标志

# 随机生成游戏盘面
def newGameBoard():
    board = [i for i in range(cell_nums)]
    black_cell = cell_nums - 1
    board[black_cell] = -1

    for _ in range(max_rand_time):
        direction = random.randint(0, 3)
        if direction == 0:
            black_cell = moveLeft(board, black_cell)
        elif direction == 1:
            black_cell = moveRight(board, black_cell)
        elif direction == 2:
            black_cell = moveUp(board, black_cell)
        elif direction == 3:
            black_cell = moveDown(board, black_cell)
    return board, black_cell

# 移动函数
def moveRight(board, black_cell):
    if black_cell % ROWS == 0:
        return black_cell
    board[black_cell - 1], board[black_cell] = board[black_cell], board[black_cell - 1]
    return black_cell - 1

def moveLeft(board, black_cell):
    if black_cell % ROWS == ROWS - 1:
        return black_cell
    board[black_cell + 1], board[black_cell] = board[black_cell], board[black_cell + 1]
    return black_cell + 1

def moveDown(board, black_cell):
    if black_cell < ROWS:
        return black_cell
    board[black_cell - ROWS], board[black_cell] = board[black_cell], board[black_cell - ROWS]
    return black_cell - ROWS

def moveUp(board, black_cell):
    if black_cell >= cell_nums - ROWS:
        return black_cell
    board[black_cell + ROWS], board[black_cell] = board[black_cell], board[black_cell + ROWS]
    return black_cell + ROWS

# 是否完成
def isFinished(board):
    for i in range(cell_nums - 1):
        if board[i] != i:
            return False
    return True

# 绘制按钮
def draw_button(text, x, y, w, h, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # 检查鼠标是否在按钮上并变更颜色
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(windowSurface, hover_color, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(windowSurface, color, (x, y, w, h))

    # 设置字体为宋体
    font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
    font = pygame.font.Font(font_path, 24)  # 设置字体大小
    text_surface = font.render(text, True, BLACK)  # 确保文字颜色与按钮颜色不同
    text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
    windowSurface.blit(text_surface, text_rect)

# 切换图片函数
def change_image():
    global gameImage, gameRect, cellWidth, cellHeight
    gameImage = pygame.image.load(random.choice(['star.jpg', 'tom.jpg', 'girl.jpg']))  # 替换为实际图片路径
    gameRect = gameImage.get_rect()
    cellWidth = int(gameRect.width / ROWS)
    cellHeight = int(gameRect.height / ROWS)

# 查看原图
def toggle_original():
    global show_original
    show_original = not show_original

# 图片重排
def shuffle_image():
    global gameBoard, black_cell, finish
    gameBoard, black_cell = newGameBoard()
    finish = False

gameBoard, black_cell = newGameBoard()

# 游戏主循环
while True:
    for event in pygame.event.get():
        # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if finish:
            continue

        # 按下方向键或字母键移动方块
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == ord('a'):
                black_cell = moveLeft(gameBoard, black_cell)
            if event.key == K_RIGHT or event.key == ord('d'):
                black_cell = moveRight(gameBoard, black_cell)
            if event.key == K_UP or event.key == ord('w'):
                black_cell = moveUp(gameBoard, black_cell)
            if event.key == K_DOWN or event.key == ord('s'):
                black_cell = moveDown(gameBoard, black_cell)

        # 点击鼠标左键，移动方块
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if y < gameRect.height:  # 确保点击的是拼图部分
                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * ROWS
                if index == black_cell - 1 or index == black_cell + 1 or index == black_cell - ROWS or index == black_cell + ROWS:
                    gameBoard[black_cell], gameBoard[index] = gameBoard[index], gameBoard[black_cell]
                    black_cell = index

    # 如果拼图完成，设置完成标志
    if isFinished(gameBoard):
        gameBoard[black_cell] = cell_nums - 1
        finish = True

    # 填充游戏窗口
    windowSurface.fill(background_color)

    # 查看原图
    if show_original:
        windowSurface.blit(gameImage, (0, 0))
    else:
        # 将拼图中的每个小块绘制到游戏窗口中
        for i in range(cell_nums):
            rowDst = int(i / ROWS)
            colDst = int(i % ROWS)
            rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

            if gameBoard[i] == -1:
                continue

            rowArea = int(gameBoard[i] / ROWS)
            colArea = int(gameBoard[i] % ROWS)
            rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
            windowSurface.blit(gameImage, rectDst, rectArea)

        # 绘制拼图的网格线
        for i in range(ROWS + 1):
            pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
        for i in range(ROWS + 1):
            pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))

    # 绘制按钮
    draw_button('查看原图', 50, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), toggle_original)
    draw_button('切换图片', 250, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), change_image)
    draw_button('图片重排', 450, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), shuffle_image)
    # 更新游戏窗口
    pygame.display.update()
    # 控制游戏帧率
    mainClock.tick(FPS)
