import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton, QFileDialog, 
                             QHBoxLayout, QMessageBox, QDialog, QComboBox, QStackedWidget)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


# 预设图片库
PRESET_IMAGES = {
    "拼图1": "star.jpg",
    "拼图2": "tom.jpg",
    "拼图3": "girl.jpg",
}

class PuzzlePiece(QLabel):
    def __init__(self, pixmap, initial_position, puzzle):
        super().__init__()  # 调用父类 QLabel 的构造函数
        self.initial_position = initial_position  # 存储拼图块的初始正确位置
        self.current_position = initial_position  # 存储拼图块的当前显示位置
        self.puzzle = puzzle  # 引用所属的拼图游戏实例，便于调用游戏逻辑
        self.setAlignment(Qt.AlignCenter)  # 设置拼图块内容居中对齐
        self.setStyleSheet("border: 1px solid black;")  # 设置拼图块的边框样式
        self.setFixedSize(puzzle.piece_width, puzzle.piece_height)  # 设置拼图块的固定大小
        self.setPixmap(pixmap)  # 设置拼图块显示的图像
        self.setScaledContents(True)  # 使图片内容自适应控件大小

    def mousePressEvent(self, event):
        # 重写鼠标按下事件，处理拼图块的选择和交换
        if event.button() == Qt.LeftButton:  # 检查是否是左键点击
            if self.puzzle.selected_piece is None:
                # 如果没有选中的拼图块，则选中当前拼图块
                self.puzzle.selected_piece = self  # 记录当前选中的拼图块
                self.setStyleSheet("border: 2px solid red;")  # 高亮显示选中的拼图块
            else:
                # 如果已经选中了其他拼图块，执行交换操作
                self.puzzle.swapPieces(self.puzzle.selected_piece, self)  # 交换两个拼图块
                self.puzzle.selected_piece.setStyleSheet("border: 1px solid black;")  # 恢复之前选中块的样式
                self.puzzle.selected_piece = None  # 清空选中的拼图块引用

class ImageDialog(QDialog):
    def __init__(self, image):
        super().__init__()  # 调用父类 QDialog 的构造函数
        self.setWindowTitle("原图")  # 设置窗口标题
        self.setFixedSize(image.width(), image.height())  # 设置窗口固定大小为原图大小
        self.label = QLabel(self)  # 创建标签用于显示原图
        self.label.setPixmap(image)  # 设置标签的图像为传入的原图
        self.label.setScaledContents(True)  # 使标签内容自适应控件大小
        self.label.setAlignment(Qt.AlignCenter)  # 设置图片在标签中的居中对齐方式


class MyPuzzle(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类 QWidget 的构造函数
        self.setWindowTitle("拼图游戏")  # 设置窗口标题为“拼图游戏”
        self.mainLayout = QHBoxLayout()  # 创建主布局，使用水平布局
        self.setLayout(self.mainLayout)  # 设置当前窗口的布局为主布局
        self.initLayout()  # 初始化布局和控件
        self.pieces = []  # 存储所有拼图块的列表
        self.image = None  # 存储原始图片
        self.gridSize = 3  # 默认拼图难度，设定为 3x3
        self.selected_piece = None  # 用于记录当前选中的拼图块
        self.timer = QTimer(self)  # 创建计时器实例
        self.timer.timeout.connect(self.updateTime)  # 连接计时器的超时信号到更新时间的方法
        self.elapsed_time = 0  # 记录游戏进行时的已用时间
        self.shortest_time = None  # 存储最短用时
        self.shortestcount = None  # 初始化最短步数
        self.fullImageLabel = None  # 用于显示完整图片的标签
        self.piece_width = 0  # 每个拼图块的宽度
        self.piece_height = 0  # 每个拼图块的高度
        self.move_count = 0  # 初始化步数计数器

    def initLayout(self):
        # 初始化布局，包括拼图区域和控制区域
        self.puzzleLayout = QVBoxLayout()  # 创建拼图区域的垂直布局
        self.mainLayout.addLayout(self.puzzleLayout)  # 将拼图布局添加到主布局中

        self.controlLayout = QVBoxLayout()  # 创建控制区域的垂直布局
        self.mainLayout.addLayout(self.controlLayout)  # 将控制布局添加到主布局中

        # 难度选择控件
        self.difficultyLabel = QLabel("选择难度：")  # 创建难度标签
        self.controlLayout.addWidget(self.difficultyLabel)  # 添加标签到控制布局中
        self.difficultyComboBox = QComboBox()  # 创建下拉框选择难度
        self.difficultyComboBox.addItems(["容易 (3x3)", "中等 (4x4)", "困难 (5x5)"])  # 添加难度选项
        self.controlLayout.addWidget(self.difficultyComboBox)  # 添加下拉框到控制布局中

        # 图片选择控件（预设图片）
        self.imageLabel = QLabel("选择图片：")  # 创建图片选择标签
        self.controlLayout.addWidget(self.imageLabel)  # 添加标签到控制布局中
        self.imageComboBox = QComboBox()  # 创建下拉框用于选择预设图片
        self.imageComboBox.addItems(PRESET_IMAGES.keys())  # 添加预设图片的名称
        self.controlLayout.addWidget(self.imageComboBox)  # 添加下拉框到控制布局中

        # 提示标签
        self.label = QLabel("请加载一张图片或选择预设图片：")  # 创建提示标签
        self.controlLayout.addWidget(self.label)  # 添加提示标签到控制布局中

        # 加载图片按钮
        self.loadButton = QPushButton("加载图片")  # 创建加载图片按钮
        self.controlLayout.addWidget(self.loadButton)  # 添加按钮到控制布局中

        # 打乱按钮
        self.shuffleButton = QPushButton("打乱")  # 创建打乱按钮
        self.shuffleButton.setEnabled(False)  # 初始时禁用，需先加载图片后才能使用
        self.controlLayout.addWidget(self.shuffleButton)  # 添加按钮到控制布局中

        # 查看原图按钮
        self.viewOriginalButton = QPushButton("查看原图")  # 创建查看原图按钮
        self.viewOriginalButton.setEnabled(False)  # 初始时禁用，需先加载图片后才能使用
        self.controlLayout.addWidget(self.viewOriginalButton)  # 添加按钮到控制布局中

        # 挑战模式按钮
        self.challengeButton = QPushButton("开始挑战")  # 创建挑战模式按钮
        self.controlLayout.addWidget(self.challengeButton)  # 添加按钮到控制布局中

        # 计时器显示标签
        self.timerLabel = QLabel("计时: 0 秒")  # 创建计时标签
        self.controlLayout.addWidget(self.timerLabel)  # 添加计时标签到控制布局中

        # 最短用时显示标签
        self.shortestTimeLabel = QLabel("最短用时: -- 秒")  # 创建最短用时标签
        self.controlLayout.addWidget(self.shortestTimeLabel)  # 添加标签到控制布局中

        # 计步器显示标签
        self.countLabel = QLabel("计步: 0 步")  # 创建计时标签
        self.controlLayout.addWidget(self.countLabel)  # 添加计时标签到控制布局中

        # 最短步数显示标签
        self.shortestcountLabel = QLabel("最短步数: -- 步")  # 创建最短步数标签
        self.controlLayout.addWidget(self.shortestcountLabel)  # 添加标签到控制布局中

        # 连接按钮的点击信号到相应的方法
        self.loadButton.clicked.connect(self.loadImage)  # 加载图片按钮连接加载图片方法
        self.shuffleButton.clicked.connect(self.shuffle)  # 打乱按钮连接打乱方法
        self.viewOriginalButton.clicked.connect(self.viewOriginalImage)  # 查看原图按钮连接查看原图方法
        self.imageComboBox.currentTextChanged.connect(self.loadPresetImage)  # 图片选择框变化时加载相应图片
        self.challengeButton.clicked.connect(self.startChallenge)  # 挑战模式按钮连接开始挑战方法

        # 初始化拼图块布局
        self.gridLayout = QGridLayout()  # 创建拼图块的网格布局
        self.puzzleLayout.addLayout(self.gridLayout)  # 将网格布局添加到拼图区域中

    def clearLayout(self, layout):
        """清除布局中的所有子控件"""
        while layout.count():  # 循环遍历布局中的所有控件
            item = layout.takeAt(0)  # 取出布局中的第一个控件
            widget = item.widget()  # 获取控件对象
            if widget is not None:
                widget.deleteLater()  # 删除控件，释放内存

    def loadImage(self):
        """从文件系统加载图片"""
        filePath, _ = QFileDialog.getOpenFileName(self, "打开图片文件", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")  # 打开文件对话框选择图片
        if filePath:  # 如果选择了文件
            self.image = QPixmap(filePath)  # 创建 QPixmap 对象并加载选择的图片
            self.scaleImage()  # 调整图片大小以适应控件
            self.displayFullImage()  # 显示完整的原始图片
            self.adjustWindowSize()  # 调整窗口大小以适应图片
            self.label.clear()  # 清空提示标签内容
            self.shuffleButton.setEnabled(True)  # 启用打乱按钮
            self.viewOriginalButton.setEnabled(True)  # 启用查看原图按钮

    def loadPresetImage(self):
        """从预设图片库中加载图片"""
        selected_image_name = self.imageComboBox.currentText()  # 获取当前选择的预设图片名称
        if selected_image_name in PRESET_IMAGES:  # 检查所选图片是否在预设图片库中
            self.image = QPixmap(PRESET_IMAGES[selected_image_name])  # 创建 QPixmap 对象并加载预设图片
            self.scaleImage()  # 调整图片大小以适应控件
            self.splitImage()  # 切割图片为拼图块
            self.displayFullImage()  # 显示完整的原始图片
            self.adjustWindowSize()  # 调整窗口大小以适应图片
            self.label.clear()  # 清空提示标签内容
            self.shuffleButton.setEnabled(True)  # 启用打乱按钮
            self.viewOriginalButton.setEnabled(True)  # 启用查看原图按钮


    def scaleImage(self):
        """将图片缩放到合适的大小"""
        fixed_size = (600, 600)  # 定义固定尺寸为 600x600
        # 将图片按比例缩放到固定尺寸，保持宽高比，并使用平滑变换
        self.image = self.image.scaled(fixed_size[0], fixed_size[1], Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # 计算每个拼图块的宽度，根据网格大小将图片宽度分割
        self.piece_width = self.image.width() // self.gridSize
        # 计算每个拼图块的高度，根据网格大小将图片高度分割
        self.piece_height = self.image.height() // self.gridSize

    def displayFullImage(self):
        """在拼图区域显示完整的图片"""
        self.clearLayout(self.gridLayout)  # 清空拼图布局以准备显示完整图片
        self.fullImageLabel = QLabel()  # 创建新的标签用于显示完整图片
        self.fullImageLabel.setPixmap(self.image)  # 设置标签的图片为当前图片
        self.fullImageLabel.setAlignment(Qt.AlignCenter)  # 设置图片在标签中的居中对齐
        self.gridLayout.addWidget(self.fullImageLabel)  # 将标签添加到网格布局中

    def startGameLayout(self):
        """切换到拼图游戏布局"""
        if self.fullImageLabel is not None:  # 检查完整图片标签是否存在
            # 删除完整图片视图
            self.fullImageLabel.deleteLater()  # 删除完整图片标签并释放资源
            # 重置标签引用
            self.fullImageLabel = None  # 将完整图片标签重置为 None

    def splitImage(self):
        """将图片切割成拼图块"""
        # 清空布局和拼图块列表
        self.clearLayout(self.gridLayout)  # 清空网格布局
        self.pieces.clear()  # 清空拼图块列表
        # 计算每个拼图块的宽度和高度
        self.piece_width = self.image.width() // self.gridSize
        self.piece_height = self.image.height() // self.gridSize
        # 遍历网格，切割图片并创建拼图块
        for y in range(self.gridSize):  # 遍历行
            for x in range(self.gridSize):  # 遍历列
                # 获取图片的子区域，作为拼图块
                piece = self.image.copy(x * self.piece_width, y * self.piece_height, self.piece_width, self.piece_height)
                # 创建拼图块实例，并添加到网格布局中
                label = PuzzlePiece(piece, (x, y), self)  # 创建拼图块对象
                self.gridLayout.addWidget(label, y, x)  # 将拼图块添加到网格布局中
                # 将拼图块添加到拼图块列表
                self.pieces.append(label)  # 存储拼图块对象

    def swapPieces(self, piece1, piece2):
        """交换两个拼图块的位置"""
        # 获取两个拼图块的当前位置
        piece1_position = piece1.current_position
        piece2_position = piece2.current_position

        # 交换位置
        piece1.current_position = piece2_position  # 更新拼图块1的当前位置
        piece2.current_position = piece1_position  # 更新拼图块2的当前位置

        # 更新布局中的位置
        self.gridLayout.addWidget(piece1, piece2_position[1], piece2_position[0])  # 将拼图块1放到拼图块2原来的位置
        self.gridLayout.addWidget(piece2, piece1_position[1], piece1_position[0])  # 将拼图块2放到拼图块1原来的位置

        # 更新步数计数
        self.move_count += 1  # 步数加一
        # 更新计步器显示
        self.countLabel.setText(f"计步: {self.move_count} 步")

        # 检查拼图是否完成
        if self.isPuzzleCompleted():
            # 停止计时
            self.timer.stop()
            # 更新最短用时
            if self.shortest_time is None or self.elapsed_time < self.shortest_time:
                self.shortest_time = self.elapsed_time
                self.shortestTimeLabel.setText(f"最短用时: {self.shortest_time} 秒")
            
            # 更新最短步数逻辑
            if self.shortestcount is None or self.move_count < self.shortestcount:
                self.shortestcount = self.move_count
                self.shortestcountLabel.setText(f"最短步数: {self.shortestcount} 步")  # 更新最短步数显示

            # 弹出完成提示，包括用时和步数
            QMessageBox.information(self, "恭喜", 
                                    f"您完成了拼图！\n用时: {self.elapsed_time} 秒\n步数: {self.move_count} 步")


    def isPuzzleCompleted(self):
        """检查所有拼图块是否都在正确位置"""
        # 遍历所有拼图块
        for piece in self.pieces:
            # 如果有任意拼图块不在初始位置，则返回 False
            if piece.current_position != piece.initial_position:
                return False
        return True  # 所有拼图块都在正确位置，返回 True

    def shuffle(self):
        """打乱拼图块"""
        # 检查是否加载了图片
        if self.image is None:  # 如果没有加载图片
            QMessageBox.warning(self, "警告", "请先加载图片。")  # 提示用户
            return

        # 根据选择的难度设置 gridSize
        difficulty = self.difficultyComboBox.currentText()  # 获取当前选择的难度
        if "容易" in difficulty:
            self.gridSize = 3  # 设置网格大小为 3x3
        elif "中等" in difficulty:
            self.gridSize = 4  # 设置网格大小为 4x4
        else:
            self.gridSize = 5  # 设置网格大小为 5x5

        # 将原始图片切割成 gridSize 的拼图块
        self.splitImage()  # 切割图片
        # 切换到游戏布局
        self.startGameLayout()  # 准备游戏布局

        # 打乱拼图块的位置
        positions = [piece.current_position for piece in self.pieces]  # 获取当前所有拼图块的位置
        random.shuffle(positions)  # 随机打乱位置
        for piece, pos in zip(self.pieces, positions):  # 将打乱后的位置赋值给拼图块
            piece.current_position = pos  # 更新拼图块的当前位置
            self.gridLayout.addWidget(piece, pos[1], pos[0])  # 将拼图块放到新的位置
        
        # 调整大小重置计时和步数
        self.adjustWindowSize()  # 调整窗口大小
        self.elapsed_time = 0  # 重置已用时间
        self.timerLabel.setText(f"计时: {self.elapsed_time} 秒")  # 更新计时器显示
        self.timer.start(1000)  # 开始计时，每秒更新一次
        self.move_count = 0  # 重置步数
        self.countLabel.setText("计步: 0 步")  # 更新步数显示

    def adjustWindowSize(self):
        """根据拼图大小调整窗口尺寸"""
        # 计算窗口总宽度
        total_width = self.image.width() + 250  # 加上控制区域的宽度
        # 计算窗口总高度
        total_height = max(self.image.height(), self.sizeHint().height())  # 取最大值以适应内容
        # 调整窗口尺寸
        self.resize(total_width, total_height)  # 设置窗口大小

    def updateTime(self):
        """更新计时器显示"""
        # 每次调用增加1秒
        self.elapsed_time += 1  # 增加已用时间
        self.timerLabel.setText(f"计时: {self.elapsed_time} 秒")  # 更新计时器标签显示

    def startChallenge(self):
        """开始挑战模式"""
        self.shuffle()  # 随机打乱拼图块
        # 初始化
        self.elapsed_time = 0  # 重置计时
        # 更新计时器
        self.timerLabel.setText(f"计时: {self.elapsed_time} 秒")  # 更新计时器显示
        self.timer.start(1000)  # 启动计时器，每秒更新一次
        self.move_count = 0  # 重置步数
        self.countLabel.setText("计步: 0 步")  # 更新步数显示

    def viewOriginalImage(self):
        """查看原始完整图片"""
        if self.image:  # 检查是否已加载图片
            # 将当前加载的图片传递给构造函数
            dialog = ImageDialog(self.image)  # 创建对话框显示原始图片
            dialog.exec_()  # 使用 exec_() 在 PyQt5 中显示对话框

class WelcomeScreen(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()  # 调用父类的构造函数
        # 保存实例，用于界面切换
        self.stacked_widget = stacked_widget  # 保存堆叠窗口引用以进行界面切换
        self.initUI()  # 初始化用户界面

    def initUI(self):
        layout = QVBoxLayout()  # 创建垂直布局
        self.setLayout(layout)  # 设置当前窗口的布局为垂直布局

        # 欢迎标题，使用富文本显示彩色艺术字
        title = QLabel()  # 创建标签用于显示标题
        # 启用富文本格式，使其支持HTML
        title.setTextFormat(Qt.RichText)  # 设置文本格式为富文本
        # 设置对齐方式（居中）
        title.setAlignment(Qt.AlignCenter)  # 设置文本居中对齐

        # 设置彩色艺术字
        title_text = "<p style='font-size:40pt; font-weight:bold;'>"  # 设置标题文本样式
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']  # 定义颜色列表
        text = "欢迎来到拼图游戏！"  # 欢迎文本

        for i, char in enumerate(text):  # 遍历欢迎文本的每个字符
            # 用取模运算来实现颜色的循环选择
            color = colors[i % len(colors)]  # 根据字符索引选择颜色
            title_text += f"<span style='color:{color};'>{char}</span>"  # 为字符设置颜色
        title_text += "</p>"  # 结束HTML段落
        title.setText(title_text)  # 设置标签的文本为富文本
        layout.addWidget(title)  # 将标题添加到布局中

        # 游戏说明
        description = QLabel("请选择难度并开始游戏，点击按钮开始拼图挑战。")  # 创建说明标签
        description.setAlignment(Qt.AlignCenter)  # 设置说明文本居中对齐
        layout.addWidget(description)  # 将说明添加到布局中

        # 开始游戏按钮
        start_button = QPushButton("开始游戏")  # 创建开始游戏按钮
        start_button.setFont(QFont("Arial", 25))  # 设置按钮字体和大小
        start_button.clicked.connect(self.start_game)  # 连接按钮点击事件到 start_game 方法
        layout.addWidget(start_button)  # 将按钮添加到布局中

    def start_game(self):
        """切换到拼图游戏界面"""
        self.stacked_widget.setCurrentIndex(1)  # 切换到堆叠窗口中的第二个页面（拼图游戏界面）

class GameApp(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.setWindowTitle("拼图游戏")  # 设置窗口标题

        # 切换界面
        self.stacked_widget = QStackedWidget()  # 创建堆叠窗口用于界面切换

        # 创建欢迎界面和拼图游戏界面
        self.welcome_screen = WelcomeScreen(self.stacked_widget)  # 创建欢迎界面实例
        self.puzzle_game = MyPuzzle()  # 创建拼图游戏实例

        # 将界面添加到 stacked_widget
        self.stacked_widget.addWidget(self.welcome_screen)  # 添加欢迎界面到堆叠窗口
        self.stacked_widget.addWidget(self.puzzle_game)  # 添加拼图游戏界面到堆叠窗口

        # 设置布局
        layout = QVBoxLayout()  # 创建垂直布局
        layout.addWidget(self.stacked_widget)  # 将堆叠窗口添加到布局中
        self.setLayout(layout)  # 设置当前窗口的布局为垂直布局

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    window = GameApp()  # 创建游戏应用窗口
    window.show()  # 显示窗口
    sys.exit(app.exec_())  # 启动应用程序事件循环