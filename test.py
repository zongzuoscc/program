import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QDialog, QLabel, QComboBox, QMenuBar, QMainWindow, QAction
from PyQt5.QtCore import Qt
from math import sqrt

class Calculator(QMainWindow):  # 定义Calculator类，继承自QMainWindow
    def __init__(self):
        super().__init__()  # 调用父类的构造函数
        self.initUI()  # 调用初始化界面的方法

    def initUI(self):
        self.setWindowTitle('计算器')  # 设置窗口标题
        self.setGeometry(300, 300, 400, 400)  # 设置窗口大小和位置

        # 创建菜单栏
        menubar = self.menuBar()

        # 添加转换菜单
        convert_menu = menubar.addMenu('转换')

        # 添加进制转换菜单项
        base_convert_action = QAction('进制转换', self)  # 创建动作，绑定到'进制转换'文本
        base_convert_action.triggered.connect(self.open_base_converter)  # 当动作被触发时，调用open_base_converter方法
        convert_menu.addAction(base_convert_action)  # 将动作添加到转换菜单中

        # 添加汇率转换菜单项
        currency_convert_action = QAction('汇率转换', self)  # 创建动作，绑定到'汇率转换'文本
        currency_convert_action.triggered.connect(self.open_currency_converter)  # 当动作被触发时，调用open_currency_converter方法
        convert_menu.addAction(currency_convert_action)  # 将动作添加到转换菜单中

        # 显示屏幕
        self.display = QLineEdit(self)  # 创建一个文本输入框作为显示屏幕
        self.display.setReadOnly(False)  # 设置显示屏幕可编辑
        self.display.setAlignment(Qt.AlignRight)  # 设置文本右对齐
        self.display.setFixedHeight(50)  # 设置显示屏幕的高度为50

        # 按钮列表（修改为中文，新增退格按钮）
        buttons = [
            '7', '8', '9', '/', '(', ')',
            '4', '5', '6', '*', '√', '1/x',
            '1', '2', '3', '-', '平方', '←',  # 添加“退格”按钮
            '0', '.', '=', '+', '%', '清除'
        ]

        # 创建网格布局
        grid_layout = QGridLayout()

        # 创建按钮并添加到布局中
        row, col = 1, 0
        for button_text in buttons:
            button = QPushButton(button_text, self)  # 创建按钮，设置文本为按钮列表中的文本
            button.clicked.connect(self.on_click)  # 连接按钮的点击信号到on_click方法
            button.setFixedSize(60, 60)  # 设置按钮大小为60x60
            grid_layout.addWidget(button, row, col)  # 将按钮添加到网格布局中

            col += 1
            if col > 5:  # 每行6个按钮，超过则转到下一行
                col = 0
                row += 1

        # 创建一个容器QWidget，用于放置显示屏幕和按钮布局
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)  # 将显示屏幕添加到垂直布局中
        main_layout.addLayout(grid_layout)  # 将网格布局添加到垂直布局中
        main_widget.setLayout(main_layout)  # 将垂直布局设置为容器QWidget的布局
        self.setCentralWidget(main_widget)  # 将容器QWidget设置为主窗口的中央部件

    def on_click(self):
        button = self.sender()  # 获取被点击的按钮
        if button:
            text = button.text()  # 获取按钮文本
            if text == '清除':
                self.display.clear()  # 清除显示屏幕内容
            elif text == '←':  # 处理退格按钮
                current_text = self.display.text()  # 获取当前显示屏幕文本
                self.display.setText(current_text[:-1])  # 删除最后一个字符
            elif text == '=':
                try:
                    self.display.setText(str(eval(self.display.text())))  # 计算表达式并显示结果
                except Exception as e:
                    self.display.setText('Error')  # 显示错误信息
            elif text == '√':
                try:
                    result = sqrt(float(self.display.text()))  # 计算平方根
                    self.display.setText(str(result))  # 显示结果
                except Exception as e:
                    self.display.setText('Error')  # 显示错误信息
            elif text == '平方':
                try:
                    result = float(self.display.text()) ** 2  # 计算平方
                    self.display.setText(str(result))  # 显示结果
                except Exception as e:
                    self.display.setText('Error')  # 显示错误信息
            elif text == '1/x':
                try:
                    result = 1 / float(self.display.text())  # 计算倒数
                    self.display.setText(str(result))  # 显示结果
                except Exception as e:
                    self.display.setText('Error')  # 显示错误信息
            else:
                self.display.setText(self.display.text() + text)  # 将按钮文本添加到显示屏幕

    def open_base_converter(self):
        # 创建进制转换器窗口
        dialog = BaseConverter(self)
        dialog.exec_()  # 显示窗口

    def open_currency_converter(self):
        # 创建汇率转换器窗口
        dialog = CurrencyConverter(self)
        dialog.exec_()  # 显示窗口

class BaseConverter(QDialog):  # 定义BaseConverter类，继承自QDialog
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类的构造函数
        self.initUI()  # 调用初始化界面的方法

    def initUI(self):
        self.setWindowTitle("进制转换器")  # 设置窗口标题
        self.setGeometry(400, 400, 300, 200)  # 设置窗口大小和位置

        # 创建进制转换的UI元素
        self.input_label = QLabel('输入数字:', self)  # 创建标签
        self.input_field = QLineEdit(self)  # 创建输入框

        self.base_label = QLabel('选择进制:', self)  # 创建标签
        self.base_combo = QComboBox(self)  # 创建下拉框
        self.base_combo.addItems(['二进制', '八进制', '十进制', '十六进制'])  # 添加选项

        self.result_label = QLabel('转换结果:', self)  # 创建标签
        self.result_output = QLineEdit(self)  # 创建输出框
        self.result_output.setReadOnly(True)  # 设置只读

        self.convert_button = QPushButton('转换', self)  # 创建按钮
        self.convert_button.clicked.connect(self.convert_base)  # 连接点击信号到convert_base方法

        # 布局
        layout = QVBoxLayout()  # 创建垂直布局
        layout.addWidget(self.input_label)  # 添加标签
        layout.addWidget(self.input_field)  # 添加输入框
        layout.addWidget(self.base_label)  # 添加标签
        layout.addWidget(self.base_combo)  # 添加下拉框
        layout.addWidget(self.result_label)  # 添加标签
        layout.addWidget(self.result_output)  # 添加输出框
        layout.addWidget(self.convert_button)  # 添加按钮

        self.setLayout(layout)  # 设置布局

    def convert_base(self):
        try:
            num = int(self.input_field.text())  # 获取输入的数字
            base = self.base_combo.currentText()  # 获取选择的进制
            if base == '二进制':
                self.result_output.setText(bin(num)[2:])  # 转换为二进制
            elif base == '八进制':
                self.result_output.setText(oct(num)[2:])  # 转换为八进制
            elif base == '十进制':
                self.result_output.setText(str(num))  # 转换为十进制
            elif base == '十六进制':
                self.result_output.setText(hex(num)[2:])  # 转换为十六进制
        except ValueError:
            self.result_output.setText('输入无效')  # 显示错误信息

class CurrencyConverter(QDialog):  # 定义CurrencyConverter类，继承自QDialog
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类的构造函数
        self.initUI()  # 调用初始化界面的方法

    def initUI(self):
        self.setWindowTitle("汇率转换器")  # 设置窗口标题
        self.setGeometry(400, 400, 300, 200)  # 设置窗口大小和位置

        # 创建汇率转换的UI元素
        self.amount_label = QLabel('金额:', self)  # 创建标签
        self.amount_input = QLineEdit(self)  # 创建输入框

        self.from_currency_label = QLabel('从:', self)  # 创建标签
        self.from_currency = QComboBox(self)  # 创建下拉框
               # 继续创建汇率转换的UI元素
        self.to_currency_label = QLabel('到:', self)  # 创建标签，表示目标货币
        self.to_currency = QComboBox(self)  # 创建下拉框，用于选择目标货币
        self.to_currency.addItems(['USD', 'EUR', 'CNY', 'JPY'])  # 向下拉框中添加货币选项

        self.rate_label = QLabel('汇率:', self)  # 创建标签，表示汇率
        self.rate_input = QLineEdit(self)  # 创建输入框，用于输入汇率

        self.result_label = QLabel('转换结果:', self)  # 创建标签，表示转换结果
        self.result_output = QLineEdit(self)  # 创建输入框，用于显示转换结果
        self.result_output.setReadOnly(True)  # 设置输入框为只读，不允许用户编辑

        self.convert_button = QPushButton('转换', self)  # 创建按钮，用于触发转换操作
        self.convert_button.clicked.connect(self.convert_currency)  # 连接按钮的点击事件到convert_currency方法

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.amount_label)  # 将金额标签添加到布局
        layout.addWidget(self.amount_input)  # 将金额输入框添加到布局
        layout.addWidget(self.from_currency_label)  # 将源货币标签添加到布局
        layout.addWidget(self.from_currency)  # 将源货币下拉框添加到布局
        layout.addWidget(self.to_currency_label)  # 将目标货币标签添加到布局
        layout.addWidget(self.to_currency)  # 将目标货币下拉框添加到布局
        layout.addWidget(self.rate_label)  # 将汇率标签添加到布局
        layout.addWidget(self.rate_input)  # 将汇率输入框添加到布局
        layout.addWidget(self.result_label)  # 将结果标签添加到布局
        layout.addWidget(self.result_output)  # 将结果输出框添加到布局
        layout.addWidget(self.convert_button)  # 将转换按钮添加到布局

        self.setLayout(layout)  # 将布局设置为该对话框的布局

    def convert_currency(self):
        # 定义转换货币的方法
        try:
            amount = float(self.amount_input.text())  # 获取输入的金额并转换为浮点数
            rate = float(self.rate_input.text())  # 获取输入的汇率并转换为浮点数

            result = amount * rate  # 计算转换结果
            self.result_output.setText(f'{result:.2f}')  # 将结果显示在结果输出框，保留两位小数
        except ValueError:
            self.result_output.setText("输入无效")  # 如果输入无效，则在结果输出框显示错误信息

# 程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    calc = Calculator()  # 创建计算器对象
    calc.show()  # 显示计算器窗口
    sys.exit(app.exec_())  # 启动应用程序的事件循环

# import tkinter as tk
# import math

# root=tk.Tk()
# root.title('计算器')
# root.geometry("500x700")
# root.iconbitmap(r'C:\Users\26515\Desktop\program\favicon.ico')   # 设置窗口图标

# expression=""

# #定义一个显示表达式的功能
# def display_expression(value):
#     global expression
#     expression+=str(value)
#     display_var.set(expression)

# #计算函数
# def calculate():
#     global expression
#     try:
#         result=str(eval)

# #创建显示屏
# display_var=tk.StringVar()
# display=tk.Entry(root,textvariable=display_var,font=("楷书",14),bd=2,width=20)


# root.mainloop()