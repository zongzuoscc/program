import sys
import requests
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
            '1', '2', '3', '-', 'x²', '←',  # 添加“退格”按钮
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
            elif text == 'x²':
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
    API_URL = "https://api.exchangerate-api.com/v4/latest/"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("汇率转换器")
        self.setGeometry(400, 400, 300, 200)

        # 创建UI元素
        self.amount_label = QLabel('金额:', self)
        self.amount_input = QLineEdit(self)

        self.from_currency_label = QLabel('从:', self)
        self.from_currency = QComboBox(self)
        self.from_currency.addItems(['USD', 'EUR', 'CNY', 'JPY'])  # 源货币选项

        self.to_currency_label = QLabel('到:', self)
        self.to_currency = QComboBox(self)
        self.to_currency.addItems(['USD', 'EUR', 'CNY', 'JPY'])  # 目标货币选项

        self.result_label = QLabel('转换结果:', self)
        self.result_output = QLineEdit(self)
        self.result_output.setReadOnly(True)

        self.convert_button = QPushButton('转换', self)
        self.convert_button.clicked.connect(self.convert_currency)  # 连接到汇率转换逻辑

        # 创建垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.amount_label)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.from_currency_label)
        layout.addWidget(self.from_currency)
        layout.addWidget(self.to_currency_label)
        layout.addWidget(self.to_currency)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    def get_exchange_rate(self, from_currency, to_currency):
        try:
            # 使用 API 获取汇率
            response = requests.get(self.API_URL + from_currency)
            data = response.json()  # 转换为 JSON 格式
            if response.status_code == 200:
                return data['rates'][to_currency]  # 返回目标货币的汇率
            else:
                self.result_output.setText("汇率不可用")
                return None
        except requests.exceptions.RequestException as e:
            self.result_output.setText("无法获取汇率")
            return None

    def convert_currency(self):
        try:
            # 获取输入的金额
            amount = float(self.amount_input.text())

            # 获取用户选择的源货币和目标货币
            from_curr = self.from_currency.currentText()
            to_curr = self.to_currency.currentText()

            # 获取汇率
            rate = self.get_exchange_rate(from_curr, to_curr)
            if rate is not None:
                result = amount * rate  # 计算结果
                self.result_output.setText(f'{result:.2f}')  # 显示结果
        except ValueError:
            self.result_output.setText("输入无效")
# 程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序对象
    calc = Calculator()  # 创建计算器对象
    calc.show()  # 显示计算器窗口
    sys.exit(app.exec_())  # 启动应用程序的事件循环

# import tkinter as tk  # 导入 tkinter 库，用于创建图形用户界面
# import math           # 导入 math 库，用于数学计算，例如平方根

# # 创建一个窗口
# root = tk.Tk()        # 实例化一个 Tkinter 的根窗口对象，所有的 GUI 元素都将在这个窗口中创建
# root.title("简易计算器")  # 设置窗口的标题
# root.geometry("500x700")  # 设置窗口的大小为 400x600 像素
# root.iconbitmap(r'C:\Users\26515\Desktop\program\favicon.ico')   # 设置窗口图标

# # 全局变量，用来存储表达式
# expression = ""  # 字符串变量，用于存储用户输入的数学表达式

# # 更新显示屏上的文本
# def update_display(value):
#     global expression        # 指定使用全局变量 expression
#     expression += str(value)  # 将用户点击的按钮值（数字或运算符）追加到表达式中
#     display_var.set(expression)  # 使用 set() 函数更新显示屏上的文本，显示当前的表达式

#     #需要说明的是，这里的display_var也是全局变量，
#     #但是不需要标识为global的原因是display_var 并不是在函数内部被修改，而是被用来赋值，所以它不需要被声明为 global
#     #但是expression因为要修改他的值，所以需要被标识为全局变量

# # 计算表达式并显示结果
# def calculate():
#     global expression        # 使用全局变量 expression
#     try:
#         result = str(eval(expression))  # 使用 eval() 函数计算表达式，将结果转换为字符串存储
#         display_var.set(result)         # 将计算结果显示在屏幕上
#         expression = result  # 结果变成下一次的表达式初始值，这样可以继续在上次的结果基础上计算
#     except:  # 如果表达式无效，执行以下内容
#         display_var.set("错误")  # 显示“错误”信息
#         expression = ""  # 重置表达式为空字符串

# # 清除显示屏
# def clear():
#     global expression        # 使用全局变量 expression
#     expression = ""          # 将表达式置为空
#     display_var.set("")      # 清空显示屏上的内容

# # 退格功能：删除最后一个字符
# def backspace():
#     global expression        # 使用全局变量 expression
#     expression = expression[:-1]  # 使用字符串切片删除最后一个字符
#     display_var.set(expression)   # 更新显示屏上的表达式

# # 求倒数功能
# def reciprocal():
#     global expression        # 使用全局变量 expression
#     try:
#         result = 1 / float(expression)  # 将表达式转换为浮点数后，计算其倒数
#         display_var.set(str(result))    # 将结果转换为字符串并显示在屏幕上
#         expression = str(result)        # 将结果赋值给 expression，以便进行进一步的计算
#     except:  # 如果出现错误（如除以零），执行以下内容
#         display_var.set("错误")  # 显示错误信息
#         expression = ""          # 重置表达式为空字符串

# # 求平方根功能
# def sqrt():
#     global expression        # 使用全局变量 expression
#     try:
#         result = math.sqrt(float(expression))  # 使用 math.sqrt() 函数计算平方根
#         display_var.set(str(result))           # 将结果显示在屏幕上
#         expression = str(result)               # 将结果作为新的表达式
#     except:  # 如果输入无效，执行以下内容
#         display_var.set("错误")  # 显示错误信息
#         expression = ""          # 重置表达式

# # 创建显示屏
# display_var = tk.StringVar()  # 创建一个 StringVar() 对象，作为显示屏中文本的控制变量
# display = tk.Entry(root, textvariable=display_var, font=("宋体", 24), bd=10, insertwidth=2, width=24, borderwidth=4)
# # 创建一个文本输入框 (Entry) ，用于显示当前输入的表达式和结果
# # 参数：
# #   root：父窗口
# #   textvariable=display_var：显示屏中的内容由 display_var 控制
# #   font=("宋体", 24)：设置字体为 宋体，字号为 24
# #   bd=10：设置边框宽度
# #   insertwidth=2：设置光标的宽度
# #   width=24：设置输入框的宽度为 24 个字符
# #   borderwidth=4：设置边框宽度

# display.grid(row=0, column=0, columnspan=4)  # 使用 grid 布局，将显示屏放置在第 0 行，占据 4 列

# # 定义按钮样式
# button_font = ("宋体", 18)  # 设定按钮字体样式，宋体 字体，字号 18

# # 数字按钮和运算符按钮的定义（新增了括号）
# buttons = [
#     (' 7 ', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),  # 第一行：数字 7, 8, 9 和除号 /
#     (' 4 ', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),  # 第二行：数字 4, 5, 6 和乘号 *
#     (' 1 ', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),  # 第三行：数字 1, 2, 3 和减号 -
#     (' 0 ', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),  # 第四行：数字 0，小数点，百分号和加号 +
#     (' ( ', 5, 0), (')', 5, 1), ('=', 5, 3)  # 第五行：左括号，右括号和等号
# ]

# # 动态生成按钮
# for (text, row, col) in buttons:
#     if text == '=':
#         tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=calculate).grid(row=row, column=col, sticky="nsew")
#         # 如果按钮是 '='，创建一个按钮并绑定 calculate 函数，按下时计算表达式
#     else:
#         tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=lambda t=text: update_display(t)).grid(row=row, column=col, sticky="nsew")
#         # 对其他按钮，生成按钮，并绑定 update_display 函数，当按下时将对应的文本更新到表达式中
#         # lambda 表达式用于传递当前的按钮文本给 update_display 函数

# # 清除按钮
# tk.Button(root, text='清除', padx=20, pady=20, font=button_font, command=clear).grid(row=6, column=0, columnspan=4, sticky="nsew")
# # 创建 "清除" 按钮，并绑定 clear 函数，按下后清除表达式

# # 退格按钮
# tk.Button(root, text='退格', padx=20, pady=20, font=button_font, command=backspace).grid(row=6, column=2, sticky="nsew")
# # 创建 "退格" 按钮，并绑定 backspace 函数，按下后删除最后一个字符

# # 倒数按钮
# tk.Button(root, text='1/x', padx=20, pady=20, font=button_font, command=reciprocal).grid(row=6, column=1, sticky="nsew")
# # 创建 "1/x" 按钮，并绑定 reciprocal 函数，按下后计算倒数

# # 平方根按钮
# tk.Button(root, text='√', padx=20, pady=20, font=button_font, command=sqrt).grid(row=6, column=3, sticky="nsew")
# # 创建 "√" 按钮，并绑定 sqrt 函数，按下后计算平方根

# # 调整行列权重
# for i in range(7):
#     root.grid_rowconfigure(i, weight=1)  # 为每一行设置相同的权重，确保窗口调整大小时每行等比例变化
# for i in range(4):
#     root.grid_columnconfigure(i, weight=1)  # 为每一列设置相同的权重，确保窗口调整大小时每列等比例变化

# # 开始主循环
# root.mainloop()  # 进入 Tkinter 主循环，开始运行 GUI 程序 能够确保窗口持续存在
