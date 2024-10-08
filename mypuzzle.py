# # import pygame
# # import sys
# # import random
# # from pygame.locals import *
# # import time
# # from PyQt5.QtWidgets import QApplication, QMessageBox

# # # 游戏设置
# # background_color = (255, 255, 255)
# # BLACK = (0, 0, 0)
# # FPS = 30

# # # 初始化
# # pygame.init()
# # mainClock = pygame.time.Clock()

# # # 加载图片
# # gameImage = pygame.image.load('star.jpg')
# # gameRect = gameImage.get_rect()

# # # 设置窗口
# # windowSurface = pygame.display.set_mode((550, 650))
# # pygame.display.set_caption('拼图游戏')

# # # 拼图的默认大小（可以调整）
# # ROWS, COLS = 3, 3
# # cell_nums = ROWS * COLS
# # cellWidth = int(gameRect.width / ROWS)
# # cellHeight = int(gameRect.height / COLS)
# # max_rand_time = 100
# # finish = False
# # show_original = False

# # # 初始化计时器
# # start_time = time.time()

# # # 随机生成游戏盘面
# # def newGameBoard():
# #     board = [i for i in range(cell_nums)]
# #     black_cell = cell_nums - 1
# #     board[black_cell] = -1

# #     for _ in range(max_rand_time):
# #         direction = random.randint(0, 3)
# #         if direction == 0:
# #             black_cell = moveLeft(board, black_cell)
# #         elif direction == 1:
# #             black_cell = moveRight(board, black_cell)
# #         elif direction == 2:
# #             black_cell = moveUp(board, black_cell)
# #         elif direction == 3:
# #             black_cell = moveDown(board, black_cell)
# #     return board, black_cell

# # # 移动函数
# # def moveRight(board, black_cell):
# #     if black_cell % ROWS == 0:
# #         return black_cell
# #     board[black_cell - 1], board[black_cell] = board[black_cell], board[black_cell - 1]
# #     return black_cell - 1

# # def moveLeft(board, black_cell):
# #     if black_cell % ROWS == ROWS - 1:
# #         return black_cell
# #     board[black_cell + 1], board[black_cell] = board[black_cell], board[black_cell + 1]
# #     return black_cell + 1

# # def moveDown(board, black_cell):
# #     if black_cell < ROWS:
# #         return black_cell
# #     board[black_cell - ROWS], board[black_cell] = board[black_cell], board[black_cell - ROWS]
# #     return black_cell - ROWS

# # def moveUp(board, black_cell):
# #     if black_cell >= cell_nums - ROWS:
# #         return black_cell
# #     board[black_cell + ROWS], board[black_cell] = board[black_cell], board[black_cell + ROWS]
# #     return black_cell + ROWS

# # # 是否完成
# # def isFinished(board):
# #     for i in range(cell_nums - 1):
# #         if board[i] != i:
# #             return False
# #     return True

# # # 绘制按钮
# # def draw_button(text, x, y, w, h, color, hover_color, action=None):
# #     mouse = pygame.mouse.get_pos()
# #     click = pygame.mouse.get_pressed()
    
# #     # 检查鼠标是否在按钮上并变更颜色
# #     if x + w > mouse[0] > x and y + h > mouse[1] > y:
# #         pygame.draw.rect(windowSurface, hover_color, (x, y, w, h))
# #         if click[0] == 1 and action is not None:
# #             action()
# #     else:
# #         pygame.draw.rect(windowSurface, color, (x, y, w, h))

# #     font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
# #     font = pygame.font.Font(font_path, 24)  # 设置字体大小
# #     text_surface = font.render(text, True, BLACK)  # 确保文字颜色与按钮颜色不同
# #     text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
# #     windowSurface.blit(text_surface, text_rect)

# # # 切换图片函数
# # def change_image():
# #     global gameImage, gameRect, cellWidth, cellHeight
# #     try:
# #         image_path = random.choice(['star.jpg', 'tom.jpg', 'girl.jpg'])  # 替换为实际图片路径
# #         gameImage = pygame.image.load(image_path)
# #         gameImage = pygame.transform.scale(gameImage, (550, 550))  
# #         gameRect = gameImage.get_rect()
# #         cellWidth = int(gameRect.width / ROWS)
# #         cellHeight = int(gameRect.height / ROWS)
# #     except pygame.error as e:
# #         print(f"Error loading image: {e}")
# #         sys.exit()

# # # 查看原图
# # def toggle_original():
# #     global show_original
# #     show_original = not show_original

# # # 图片重排
# # def shuffle_image():
# #     global gameBoard, black_cell, finish, start_time
# #     gameBoard, black_cell = newGameBoard()
# #     finish = False
# #     start_time = time.time()  # 重排时重置计时器

# # # 调整拼图块的难度（修改ROWS和COLS）
# # def change_difficulty(new_rows, new_cols):
# #     global ROWS, COLS, cell_nums, cellWidth, cellHeight, gameBoard, black_cell, start_time
# #     ROWS, COLS = new_rows, new_cols
# #     cell_nums = ROWS * COLS
# #     cellWidth = int(gameRect.width / ROWS)
# #     cellHeight = int(gameRect.height / COLS)
# #     gameBoard, black_cell = newGameBoard()
# #     start_time = time.time()  # 修改难度时重置计时器

# # # 弹出提示框
# # def show_message(title, message):
# #     app = QApplication(sys.argv)
# #     msg_box = QMessageBox()
# #     msg_box.setWindowTitle(title)
# #     msg_box.setText(message)
# #     msg_box.setStandardButtons(QMessageBox.Ok)
# #     msg_box.exec_()

# # # 游戏主循环
# # gameBoard, black_cell = newGameBoard()
# # while True:
# #     for event in pygame.event.get():
# #         # 退出
# #         if event.type == QUIT:
# #             pygame.quit()
# #             sys.exit()
# #         if finish:
# #             continue

# #         # 按下方向键或字母键移动方块
# #         if event.type == KEYDOWN:
# #             if event.key == K_LEFT or event.key == ord('a'):
# #                 black_cell = moveLeft(gameBoard, black_cell)
# #             if event.key == K_RIGHT or event.key == ord('d'):
# #                 black_cell = moveRight(gameBoard, black_cell)
# #             if event.key == K_UP or event.key == ord('w'):
# #                 black_cell = moveUp(gameBoard, black_cell)
# #             if event.key == K_DOWN or event.key == ord('s'):
# #                 black_cell = moveDown(gameBoard, black_cell)

# #         # 点击鼠标左键，移动方块，允许交换方块位置
# #         if event.type == MOUSEBUTTONDOWN and event.button == 1:
# #             x, y = pygame.mouse.get_pos()
# #             if y < gameRect.height:  # 确保点击的是拼图部分
# #                 col = int(x / cellWidth)
# #                 row = int(y / cellHeight)
# #                 index = col + row * ROWS
# #                 if index != black_cell:
# #                     gameBoard[black_cell], gameBoard[index] = gameBoard[index], gameBoard[black_cell]
# #                     black_cell = index

# #     # 如果拼图完成，设置完成标志
# #     if isFinished(gameBoard):
# #         finish = True
# #         show_message("恭喜你！", "完成拼图！")

# #     # 填充游戏窗口
# #     windowSurface.fill(background_color)

# #     # 查看原图
# #     if show_original:
# #         windowSurface.blit(gameImage, (0, 0))
# #     else:
# #         # 将拼图中的每个小块绘制到游戏窗口中
# #         for i in range(cell_nums):
# #             rowDst = int(i / ROWS)
# #             colDst = int(i % ROWS)
# #             rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

# #             if gameBoard[i] == -1:
# #                 continue

# #             rowArea = int(gameBoard[i] / ROWS)
# #             colArea = int(gameBoard[i] % ROWS)
# #             rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
# #             windowSurface.blit(gameImage, rectDst, rectArea)

# #         # 绘制拼图的网格线
# #         for i in range(ROWS + 1):
# #             pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
# #         for i in range(ROWS + 1):
# #             pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))

# #     # 绘制计时器
# #     elapsed_time = int(time.time() - start_time)
# #     font = pygame.font.Font(None, 36)
# #     timer_surface = font.render(f"Time: {elapsed_time} sec", True, BLACK)
# #     windowSurface.blit(timer_surface, (400, 10))

# #     # 绘制按钮
# #     draw_button('查看原图', 30, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), toggle_original)
# #     draw_button('切换图片', 230, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), change_image)
# #     draw_button('图片重排', 430, gameRect.height +10, 100, 30, (200, 200, 200), (150, 150, 150), shuffle_image)

# #     # 绘制难度调节按钮
# #     draw_button('3x3', 30, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(3, 3))
# #     draw_button('4x4', 230, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(4, 4))
# #     draw_button('5x5', 430, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(5, 5))

# #     # 更新窗口
# #     pygame.display.update()
# #     mainClock.tick(FPS)


# import pygame
# import sys
# import random
# from pygame.locals import *
# import time

# # 游戏设置
# background_color = (255, 255, 255)
# BLACK = (0, 0, 0)
# FPS = 30

# # 初始化
# pygame.init()
# mainClock = pygame.time.Clock()

# # 加载图片
# gameImage = pygame.image.load('star.jpg')
# gameImage = pygame.transform.scale(gameImage, (550, 550))  # 确保图片缩放为窗口大小
# gameRect = gameImage.get_rect()

# # 设置窗口
# windowSurface = pygame.display.set_mode((550, 650))
# pygame.display.set_caption('拼图游戏')

# # 拼图的默认大小（可以调整）
# ROWS, COLS = 3, 3
# cell_nums = ROWS * COLS
# cellWidth = int(gameRect.width / ROWS)
# cellHeight = int(gameRect.height / COLS)
# max_rand_time = 100
# finish = False
# show_original = False

# # 初始化计时器
# start_time = time.time()

# # 随机生成游戏盘面
# def newGameBoard():
#     board = [i for i in range(cell_nums)]
#     black_cell = cell_nums - 1
#     board[black_cell] = -1

#     for _ in range(max_rand_time):
#         direction = random.randint(0, 3)
#         if direction == 0:
#             black_cell = moveLeft(board, black_cell)
#         elif direction == 1:
#             black_cell = moveRight(board, black_cell)
#         elif direction == 2:
#             black_cell = moveUp(board, black_cell)
#         elif direction == 3:
#             black_cell = moveDown(board, black_cell)
#     return board, black_cell

# # 移动函数
# def moveRight(board, black_cell):
#     if black_cell % ROWS == 0:
#         return black_cell
#     board[black_cell - 1], board[black_cell] = board[black_cell], board[black_cell - 1]
#     return black_cell - 1

# def moveLeft(board, black_cell):
#     if black_cell % ROWS == ROWS - 1:
#         return black_cell
#     board[black_cell + 1], board[black_cell] = board[black_cell], board[black_cell + 1]
#     return black_cell + 1

# def moveDown(board, black_cell):
#     if black_cell < ROWS:
#         return black_cell
#     board[black_cell - ROWS], board[black_cell] = board[black_cell], board[black_cell - ROWS]
#     return black_cell - ROWS

# def moveUp(board, black_cell):
#     if black_cell >= cell_nums - ROWS:
#         return black_cell
#     board[black_cell + ROWS], board[black_cell] = board[black_cell], board[black_cell + ROWS]
#     return black_cell + ROWS

# # 是否完成并显示消息
# def isFinished(board):
#     for i in range(cell_nums - 1):
#         if board[i] != i:
#             return False
#     return True

# # 显示拼图完成消息
# def display_finish_message():
#     font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
#     font = pygame.font.Font(font_path, 24)  # 设置字体大小
#     message_surface = font.render("拼图完成！", True, (255, 0, 0))  # 红色的提示文字
#     message_rect = message_surface.get_rect(center=(windowSurface.get_width() // 2, windowSurface.get_height() // 2))
#     windowSurface.blit(message_surface, message_rect)

# # 绘制按钮
# def draw_button(text, x, y, w, h, color, hover_color, action=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
    
#     # 检查鼠标是否在按钮上并变更颜色
#     if x + w > mouse[0] > x and y + h > mouse[1] > y:
#         pygame.draw.rect(windowSurface, hover_color, (x, y, w, h))
#         if click[0] == 1 and action is not None:
#             action()
#     else:
#         pygame.draw.rect(windowSurface, color, (x, y, w, h))

#     font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
#     font = pygame.font.Font(font_path, 24)  # 设置字体大小
#     text_surface = font.render(text, True, BLACK)
#     text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
#     windowSurface.blit(text_surface, text_rect)

# # 切换图片函数
# def change_image():
#     global gameImage, gameRect, cellWidth, cellHeight
#     try:
#         image_path = random.choice(['star.jpg', 'tom.jpg', 'girl.jpg'])  # 替换为实际图片路径
#         gameImage = pygame.image.load(image_path)
#         gameImage = pygame.transform.scale(gameImage, (550, 550))  
#         gameRect = gameImage.get_rect()
#         cellWidth = int(gameRect.width / ROWS)
#         cellHeight = int(gameRect.height / ROWS)
#     except pygame.error as e:
#         print(f"Error loading image: {e}")
#         sys.exit()

# # 查看原图
# def toggle_original():
#     global show_original
#     show_original = not show_original

# # 图片重排
# def shuffle_image():
#     global gameBoard, black_cell, finish, start_time
#     gameBoard, black_cell = newGameBoard()
#     finish = False
#     start_time = time.time()  # 重排时重置计时器

# # 调整拼图块的难度
# def change_difficulty(new_rows, new_cols):
#     global ROWS, COLS, cell_nums, cellWidth, cellHeight, gameBoard, black_cell, start_time
#     ROWS, COLS = new_rows, new_cols
#     cell_nums = ROWS * COLS
#     cellWidth = int(gameRect.width / ROWS)
#     cellHeight = int(gameRect.height / COLS)
#     gameBoard, black_cell = newGameBoard()
#     start_time = time.time()  # 修改难度时重置计时器

# # 游戏主循环
# gameBoard, black_cell = newGameBoard()
# while True:
#     for event in pygame.event.get():
#         # 退出
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#         # 当拼图完成时，处理事件以让用户关闭提示并继续
#         if finish:
#             if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
#                 finish = False  # 重置完成状态以继续游戏
#             continue  # 跳过其余的事件处理

#         # 按下方向键或字母键移动方块
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT or event.key == ord('a'):
#                 black_cell = moveLeft(gameBoard, black_cell)
#             if event.key == K_RIGHT or event.key == ord('d'):
#                 black_cell = moveRight(gameBoard, black_cell)
#             if event.key == K_UP or event.key == ord('w'):
#                 black_cell = moveUp(gameBoard, black_cell)
#             if event.key == K_DOWN or event.key == ord('s'):
#                 black_cell = moveDown(gameBoard, black_cell)

#         # 点击鼠标左键，移动方块，允许交换方块位置
#         if event.type == MOUSEBUTTONDOWN and event.button == 1:
#             x, y = pygame.mouse.get_pos()
#             if y < gameRect.height:  # 确保点击的是拼图部分
#                 col = int(x / cellWidth)
#                 row = int(y / cellHeight)
#                 index = col + row * ROWS
#                 if index != black_cell:
#                     gameBoard[black_cell], gameBoard[index] = gameBoard[index], gameBoard[black_cell]
#                     black_cell = index

#     # 如果拼图完成，设置完成标志并显示消息
#     if isFinished(gameBoard):
#         finish = True

#     # 填充游戏窗口
#     windowSurface.fill(background_color)

#     # 查看原图
#     if show_original:
#         windowSurface.blit(gameImage, (0, 0))
#     else:
#         # 将拼图中的每个小块绘制到游戏窗口中
#         for i in range(cell_nums):
#             rowDst = int(i / ROWS)
#             colDst = int(i % ROWS)
#             rectDst = pygame.Rect(colDst * cellWidth, rowDst * cellHeight, cellWidth, cellHeight)

#             if gameBoard[i] == -1:
#                 continue

#             rowArea = int(gameBoard[i] / ROWS)
#             colArea = int(gameBoard[i] % ROWS)
#             rectArea = pygame.Rect(colArea * cellWidth, rowArea * cellHeight, cellWidth, cellHeight)
#             windowSurface.blit(gameImage, rectDst, rectArea)

#         # 绘制拼图的网格线
#         for i in range(ROWS + 1):
#             pygame.draw.line(windowSurface, BLACK, (i * cellWidth, 0), (i * cellWidth, gameRect.height))
#         for i in range(ROWS + 1):
#             pygame.draw.line(windowSurface, BLACK, (0, i * cellHeight), (gameRect.width, i * cellHeight))

#     # 如果完成，显示完成消息
#     if finish:
#         display_finish_message()

#     # 绘制计时器
#     elapsed_time = int(time.time() - start_time)
#     font = pygame.font.Font(None, 36)
#     timer_surface = font.render(f"Time: {elapsed_time} sec", True, BLACK)
#     windowSurface.blit(timer_surface, (400, 10))

#     # 绘制按钮
#     draw_button('查看原图', 30, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), toggle_original)
#     draw_button('切换图片', 230, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), change_image)
#     draw_button('图片重排', 430, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), shuffle_image)

#     # 绘制难度调节按钮
#     draw_button('3x3', 30, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(3, 3))
#     draw_button('4x4', 230, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(4, 4))
#     draw_button('5x5', 430, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(5, 5))

#     # 更新窗口
#     pygame.display.update()
#     mainClock.tick(FPS)

import pygame
import sys
import random
from pygame.locals import *
import time

# 游戏设置
background_color = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30

# 初始化
pygame.init()
mainClock = pygame.time.Clock()

# 加载图片
gameImage = pygame.image.load('star.jpg')
gameImage = pygame.transform.scale(gameImage, (550, 550))  # 确保图片缩放为窗口大小
gameRect = gameImage.get_rect()

# 设置窗口
windowSurface = pygame.display.set_mode((550, 650))
pygame.display.set_caption('拼图游戏')

# 拼图的默认大小（可以调整）
ROWS, COLS = 3, 3
cell_nums = ROWS * COLS
cellWidth = int(gameRect.width / ROWS)
cellHeight = int(gameRect.height / COLS)
max_rand_time = 100
finish = False
show_original = False

# 初始化计时器
start_time = 0
elapsed_time = 0

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

# 是否完成并显示消息
def isFinished(board):
    for i in range(cell_nums - 1):
        if board[i] != i:
            return False
    return True

# 显示拼图完成消息
def display_finish_message(elapsed_time):
    font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
    font = pygame.font.Font(font_path, 24)  # 设置字体大小
    message_surface = font.render(f"拼图完成！用时: {elapsed_time} 秒", True, (255, 0, 0))  # 红色的提示文字
    message_rect = message_surface.get_rect(center=(windowSurface.get_width() // 2, windowSurface.get_height() // 2))
    windowSurface.blit(message_surface, message_rect)

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

    font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
    font = pygame.font.Font(font_path, 24)  # 设置字体大小
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
    windowSurface.blit(text_surface, text_rect)

# 切换图片函数
def change_image():
    global gameImage, gameRect, cellWidth, cellHeight
    try:
        image_path = random.choice(['star.jpg', 'tom.jpg', 'girl.jpg'])  # 替换为实际图片路径
        gameImage = pygame.image.load(image_path)
        gameImage = pygame.transform.scale(gameImage, (550, 550))  
        gameRect = gameImage.get_rect()
        cellWidth = int(gameRect.width / ROWS)
        cellHeight = int(gameRect.height / ROWS)
    except pygame.error as e:
        print(f"Error loading image: {e}")
        sys.exit()

# 查看原图
def toggle_original():
    global show_original
    show_original = not show_original

# 图片重排
def shuffle_image():
    global gameBoard, black_cell, finish, start_time, elapsed_time
    gameBoard, black_cell = newGameBoard()
    finish = False
    start_time = time.time()  # 重排时重置计时器

# 调整拼图块的难度
def change_difficulty(new_rows, new_cols):
    global ROWS, COLS, cell_nums, cellWidth, cellHeight, gameBoard, black_cell, start_time, elapsed_time
    ROWS, COLS = new_rows, new_cols
    cell_nums = ROWS * COLS
    cellWidth = int(gameRect.width / ROWS)
    cellHeight = int(gameRect.height / COLS)
    gameBoard, black_cell = newGameBoard()
    start_time = time.time()  # 修改难度时重置计时器
    elapsed_time = 0  # 重置时间

# 游戏主循环
gameBoard, black_cell = newGameBoard()
while True:
    for event in pygame.event.get():
        # 退出
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 当拼图完成时，处理事件以让用户关闭提示并继续
        if finish:
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                finish = False  # 重置完成状态以继续游戏
                elapsed_time = 0  # 重置时间
                continue  # 跳过其余的事件处理

        # 更新计时器
        if not finish:
            elapsed_time = int(time.time() - start_time)

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

        # 点击鼠标左键，移动方块，允许交换方块位置
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if y < gameRect.height:  # 确保点击的是拼图部分
                col = int(x / cellWidth)
                row = int(y / cellHeight)
                index = col + row * ROWS
                if index != black_cell:
                    gameBoard[black_cell], gameBoard[index] = gameBoard[index], gameBoard[black_cell]
                    black_cell = index

    # 如果拼图完成，设置完成标志并显示消息
    if isFinished(gameBoard):
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

    # 如果完成，显示完成消息
    if finish:
        display_finish_message(elapsed_time)

    # 绘制计时器
    font_path = 'C:\\Windows\\Fonts\\simsun.ttc'  # Windows系统的宋体路径
    font = pygame.font.Font(font_path, 24)  # 设置字体大小
    timer_surface = font.render(f"Time: {elapsed_time} sec", True, BLACK)
    windowSurface.blit(timer_surface, (400, 10))

    # 绘制按钮
    draw_button('查看原图', 30, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), toggle_original)
    draw_button('切换图片', 230, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), change_image)
    draw_button('图片重排', 430, gameRect.height + 10, 100, 30, (200, 200, 200), (150, 150, 150), shuffle_image)

    # 绘制难度调节按钮
    draw_button('3x3', 30, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(3, 3))
    draw_button('4x4', 230, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(4, 4))
    draw_button('5x5', 430, gameRect.height + 50, 100, 30, (200, 200, 200), (150, 150, 150), lambda: change_difficulty(5, 5))

    # 更新窗口
    pygame.display.update()
    mainClock.tick(FPS)
