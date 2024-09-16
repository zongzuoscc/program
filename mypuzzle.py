import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import random

class MyPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("拼图游戏")
        self.root.geometry("600x600")

        # 初始化变量
        self.image_path = None
        self.puzzle_size = 3  # 默认拼图大小为 3x3
        self.tiles = []
        self.correct_order = []
        self.current_order = []
        self.tile_objects = []  # 存储每个拼图块的图像对象
        self.blank_index = None  # 存储空白块的位置

        # 被拖动的拼图块
        self.selected_tile = None
        self.selected_tile_index = None

        # 创建主界面控件
        self.create_widgets()

    def create_widgets(self):
        # 创建菜单栏
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # 图片菜单
        image_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="图片", menu=image_menu)
        image_menu.add_command(label="加载图片", command=self.load_image)
        image_menu.add_command(label="切换图片", command=self.random_image)
        image_menu.add_separator()
        image_menu.add_command(label="退出", command=self.root.quit)

        # 设置菜单
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="设置", menu=settings_menu)
        settings_menu.add_command(label="设置拼图大小", command=self.set_puzzle_size)

        # 创建画布，用于显示拼图
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack(pady=20)

        # 添加查看原图按钮
        self.view_button = tk.Button(self.root, text="查看原图", command=self.view_image)
        self.view_button.pack(side="left", padx=10)

        # 添加开始按钮
        self.start_button = tk.Button(self.root, text="开始游戏", command=self.start_game)
        self.start_button.pack(side="right", padx=10)

    def load_image(self):
        # 加载图片并调整大小
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.original_image = self.original_image.resize((500, 500))
            self.photo_image = ImageTk.PhotoImage(self.original_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

    def random_image(self):
        # 随机选择图片
        self.image_path = random.choice(["image1.jpg", "image2.jpg", "image3.jpg"])  # 替换为实际图片路径
        self.load_image()

    def set_puzzle_size(self):
        # 设置拼图矩阵大小（容易、中等、困难）
        size = tk.simpledialog.askinteger("拼图大小", "请输入拼图矩阵大小（如 3 表示 3x3）", minvalue=2, maxvalue=10)
        if size:
            self.puzzle_size = size

    def start_game(self):
        # 将图片分割为拼图块并打乱顺序
        if not self.image_path:
            messagebox.showerror("错误", "请先加载图片")
            return

        self.tiles = []
        self.correct_order = []
        self.current_order = []
        self.canvas.delete("all")
        width, height = self.original_image.size
        tile_width = width // self.puzzle_size
        tile_height = height // self.puzzle_size

        # 分割图片并打乱顺序
        for row in range(self.puzzle_size):
            for col in range(self.puzzle_size):
                x = col * tile_width
                y = row * tile_height
                if row == self.puzzle_size - 1 and col == self.puzzle_size - 1:
                    # 最后一块设为空白块
                    self.tiles.append(None)
                    self.correct_order.append((row, col))
                    self.current_order.append((row, col))
                    self.blank_index = len(self.current_order) - 1
                else:
                    tile_image = self.original_image.crop((x, y, x + tile_width, y + tile_height))
                    tile_photo = ImageTk.PhotoImage(tile_image)
                    self.tiles.append(tile_photo)
                    self.correct_order.append((row, col))
                    self.current_order.append((row, col))

        # 随机打乱拼图块
        random.shuffle(self.current_order)

        # 在画布上显示拼图块并绑定鼠标事件
        self.tile_objects = []
        for i, (row, col) in enumerate(self.current_order):
            x, y = col * tile_width, row * tile_height
            if self.tiles[i]:
                tile = self.canvas.create_image(x, y, anchor=tk.NW, image=self.tiles[i])
                self.tile_objects.append(tile)
            else:
                self.tile_objects.append(None)  # 空白块不显示图像

        # 绑定鼠标事件
        self.canvas.bind("<Button-1>", self.on_tile_click)

    def on_tile_click(self, event):
        # 检查用户点击了哪个拼图块
        clicked_item = self.canvas.find_closest(event.x, event.y)
        index = None

        for i, tile in enumerate(self.tile_objects):
            if tile and tile == clicked_item[0]:
                index = i
                break

        if index is None:
            return  # 如果点击的是空白处，忽略

        # 如果拼图块与空白块相邻，交换它们的位置
        if self.is_adjacent_to_blank(index):
            self.swap_tiles(index, self.blank_index)

            # 更新空白块的位置
            self.blank_index = index

            # 检查拼图是否完成
            self.check_puzzle()

    def is_adjacent_to_blank(self, index):
        # 检查点击的拼图块是否与空白块相邻
        row1, col1 = self.current_order[index]
        row2, col2 = self.current_order[self.blank_index]
        return (abs(row1 - row2) == 1 and col1 == col2) or (abs(col1 - col2) == 1 and row1 == row2)

    def swap_tiles(self, index1, index2):
        # 交换两个拼图块在画布上的位置
        self.current_order[index1], self.current_order[index2] = self.current_order[index2], self.current_order[index1]
        self.canvas.coords(self.tile_objects[index1], *self.canvas.coords(self.tile_objects[index2]))
        self.canvas.coords(self.tile_objects[index2], *self.canvas.coords(self.tile_objects[index1]))

    def view_image(self):
        # 查看原图
        if self.image_path:
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

    def check_puzzle(self):
        # 检查拼图是否完成
        if self.current_order == self.correct_order:
            messagebox.showinfo("恭喜", "拼图成功！")

if __name__ == "__main__":
    root = tk.Tk()
    game = MyPuzzleGame(root)
    root.mainloop()
