# # # import sys
# # # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QDialog, QLabel, QComboBox, QMenuBar, QMainWindow, QAction
# # # from PyQt5.QtCore import Qt
# # # from math import sqrt

# # # class Calculator(QMainWindow):  # 定义Calculator类，继承自QMainWindow
# # #     def __init__(self):
# # #         super().__init__()  # 调用父类的构造函数
# # #         self.initUI()  # 调用初始化界面的方法


# # # # import sys
# # # # from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QGridLayout, QDialog, QLabel, QComboBox, QMenuBar, QMainWindow, QAction
# # # # from PyQt5.QtCore import Qt
# # # # from math import sqrt

# # # # class Calculator(QMainWindow):  # 定义Calculator类，继承自QMainWindow
# # # #     def __init__(self):
# # # #         super().__init__()  # 调用父类的构造函数
# # # #         self.initUI()  # 调用初始化界面的方法

# # # #     def initUI(self):
# # # #         self.setWindowTitle('计算器')  # 设置窗口标题
# # # #         self.setGeometry(300, 300, 400, 400)  # 设置窗口大小和位置

# # # #         # 创建菜单栏
# # # #         menubar = self.menuBar()

# # # #         # 添加转换菜单
# # # #         convert_menu = menubar.addMenu('转换')

# # # #         # 添加进制转换菜单项
# # # #         base_convert_action = QAction('进制转换', self)  # 创建动作，绑定到'进制转换'文本
# # # #         base_convert_action.triggered.connect(self.open_base_converter)  # 当动作被触发时，调用open_base_converter方法
# # # #         convert_menu.addAction(base_convert_action)  # 将动作添加到转换菜单中

# # # #         # 添加汇率转换菜单项
# # # #         currency_convert_action = QAction('汇率转换', self)  # 创建动作，绑定到'汇率转换'文本
# # # #         currency_convert_action.triggered.connect(self.open_currency_converter)  # 当动作被触发时，调用open_currency_converter方法
# # # #         convert_menu.addAction(currency_convert_action)  # 将动作添加到转换菜单中

# # # #         # 显示屏幕
# # # #         self.display = QLineEdit(self)  # 创建一个文本输入框作为显示屏幕
# # # #         self.display.setReadOnly(False)  # 设置显示屏幕可编辑
# # # #         self.display.setAlignment(Qt.AlignRight)  # 设置文本右对齐
# # # #         self.display.setFixedHeight(50)  # 设置显示屏幕的高度为50

# # # #         # 按钮列表（修改为中文，新增退格按钮）
# # # #         buttons = [
# # # #             '7', '8', '9', '/', '(', ')',
# # # #             '4', '5', '6', '*', '√', '1/x',
# # # #             '1', '2', '3', '-', '平方', '←',  # 添加“退格”按钮
# # # #             '0', '.', '=', '+', '%', '清除'
# # # #         ]

# # # #         # 创建网格布局
# # # #         grid_layout = QGridLayout()

# # # #         # 创建按钮并添加到布局中
# # # #         row, col = 1, 0
# # # #         for button_text in buttons:
# # # #             button = QPushButton(button_text, self)  # 创建按钮，设置文本为按钮列表中的文本
# # # #             button.clicked.connect(self.on_click)  # 连接按钮的点击信号到on_click方法
# # # #             button.setFixedSize(60, 60)  # 设置按钮大小为60x60
# # # #             grid_layout.addWidget(button, row, col)  # 将按钮添加到网格布局中

# # # #             col += 1
# # # #             if col > 5:  # 每行6个按钮，超过则转到下一行
# # # #                 col = 0
# # # #                 row += 1

# # # #         # 创建一个容器QWidget，用于放置显示屏幕和按钮布局
# # # #         main_widget = QWidget()
# # # #         main_layout = QVBoxLayout()
# # # #         main_layout.addWidget(self.display)  # 将显示屏幕添加到垂直布局中
# # # #         main_layout.addLayout(grid_layout)  # 将网格布局添加到垂直布局中
# # # #         main_widget.setLayout(main_layout)  # 将垂直布局设置为容器QWidget的布局
# # # #         self.setCentralWidget(main_widget)  # 将容器QWidget设置为主窗口的中央部件

# # # #     def on_click(self):
# # # #         button = self.sender()  # 获取被点击的按钮
# # # #         if button:
# # # #             text = button.text()  # 获取按钮文本
# # # #             if text == '清除':
# # # #                 self.display.clear()  # 清除显示屏幕内容
# # # #             elif text == '←':  # 处理退格按钮
# # # #                 current_text = self.display.text()  # 获取当前显示屏幕文本
# # # #                 self.display.setText(current_text[:-1])  # 删除最后一个字符
# # # #             elif text == '=':
# # # #                 try:
# # # #                     self.display.setText(str(eval(self.display.text())))  # 计算表达式并显示结果
# # # #                 except Exception as e:
# # # #                     self.display.setText('Error')  # 显示错误信息
# # # #             elif text == '√':
# # # #                 try:
# # # #                     result = sqrt(float(self.display.text()))  # 计算平方根
# # # #                     self.display.setText(str(result))  # 显示结果
# # # #                 except Exception as e:
# # # #                     self.display.setText('Error')  # 显示错误信息
# # # #             elif text == '平方':
# # # #                 try:
# # # #                     result = float(self.display.text()) ** 2  # 计算平方
# # # #                     self.display.setText(str(result))  # 显示结果
# # # #                 except Exception as e:
# # # #                     self.display.setText('Error')  # 显示错误信息
# # # #             elif text == '1/x':
# # # #                 try:
# # # #                     result = 1 / float(self.display.text())  # 计算倒数
# # # #                     self.display.setText(str(result))  # 显示结果
# # # #                 except Exception as e:
# # # #                     self.display.setText('Error')  # 显示错误信息
# # # #             else:
# # # #                 self.display.setText(self.display.text() + text)  # 将按钮文本添加到显示屏幕

# # # #     def open_base_converter(self):
# # # #         # 创建进制转换器窗口
# # # #         dialog = BaseConverter(self)
# # # #         dialog.exec_()  # 显示窗口

# # # #     def open_currency_converter(self):
# # # #         # 创建汇率转换器窗口
# # # #         dialog = CurrencyConverter(self)
# # # #         dialog.exec_()  # 显示窗口

# # # # class BaseConverter(QDialog):  # 定义BaseConverter类，继承自QDialog
# # # #     def __init__(self, parent=None):
# # # #         super().__init__(parent)  # 调用父类的构造函数
# # # #         self.initUI()  # 调用初始化界面的方法

# # # #     def initUI(self):
# # # #         self.setWindowTitle("进制转换器")  # 设置窗口标题
# # # #         self.setGeometry(400, 400, 300, 200)  # 设置窗口大小和位置

# # # #         # 创建进制转换的UI元素
# # # #         self.input_label = QLabel('输入数字:', self)  # 创建标签
# # # #         self.input_field = QLineEdit(self)  # 创建输入框

# # # #         self.base_label = QLabel('选择进制:', self)  # 创建标签
# # # #         self.base_combo = QComboBox(self)  # 创建下拉框
# # # #         self.base_combo.addItems(['二进制', '八进制', '十进制', '十六进制'])  # 添加选项

# # # #         self.result_label = QLabel('转换结果:', self)  # 创建标签
# # # #         self.result_output = QLineEdit(self)  # 创建输出框
# # # #         self.result_output.setReadOnly(True)  # 设置只读

# # # #         self.convert_button = QPushButton('转换', self)  # 创建按钮
# # # #         self.convert_button.clicked.connect(self.convert_base)  # 连接点击信号到convert_base方法

# # # #         # 布局
# # # #         layout = QVBoxLayout()  # 创建垂直布局
# # # #         layout.addWidget(self.input_label)  # 添加标签
# # # #         layout.addWidget(self.input_field)  # 添加输入框
# # # #         layout.addWidget(self.base_label)  # 添加标签
# # # #         layout.addWidget(self.base_combo)  # 添加下拉框
# # # #         layout.addWidget(self.result_label)  # 添加标签
# # # #         layout.addWidget(self.result_output)  # 添加输出框
# # # #         layout.addWidget(self.convert_button)  # 添加按钮

# # # #         self.setLayout(layout)  # 设置布局

# # # #     def convert_base(self):
# # # #         try:
# # # #             num = int(self.input_field.text())  # 获取输入的数字
# # # #             base = self.base_combo.currentText()  # 获取选择的进制
# # # #             if base == '二进制':
# # # #                 self.result_output.setText(bin(num)[2:])  # 转换为二进制
# # # #             elif base == '八进制':
# # # #                 self.result_output.setText(oct(num)[2:])  # 转换为八进制
# # # #             elif base == '十进制':
# # # #                 self.result_output.setText(str(num))  # 转换为十进制
# # # #             elif base == '十六进制':
# # # #                 self.result_output.setText(hex(num)[2:])  # 转换为十六进制
# # # #         except ValueError:
# # # #             self.result_output.setText('输入无效')  # 显示错误信息

# # # # class CurrencyConverter(QDialog):  # 定义CurrencyConverter类，继承自QDialog
# # # #     def __init__(self, parent=None):
# # # #         super().__init__(parent)  # 调用父类的构造函数
# # # #         self.initUI()  # 调用初始化界面的方法

# # # #     def initUI(self):
# # # #         self.setWindowTitle("汇率转换器")  # 设置窗口标题
# # # #         self.setGeometry(400, 400, 300, 200)  # 设置窗口大小和位置

# # # #         # 创建汇率转换的UI元素
# # # #         self.amount_label = QLabel('金额:', self)  # 创建标签
# # # #         self.amount_input = QLineEdit(self)  # 创建输入框

# # # #         self.from_currency_label = QLabel('从:', self)  # 创建标签
# # # #         self.from_currency = QComboBox(self)  # 创建下拉框
# # # #                # 继续创建汇率转换的UI元素
# # # #         self.to_currency_label = QLabel('到:', self)  # 创建标签，表示目标货币
# # # #         self.to_currency = QComboBox(self)  # 创建下拉框，用于选择目标货币
# # # #         self.to_currency.addItems(['USD', 'EUR', 'CNY', 'JPY'])  # 向下拉框中添加货币选项

# # # #         self.rate_label = QLabel('汇率:', self)  # 创建标签，表示汇率
# # # #         self.rate_input = QLineEdit(self)  # 创建输入框，用于输入汇率

# # # #         self.result_label = QLabel('转换结果:', self)  # 创建标签，表示转换结果
# # # #         self.result_output = QLineEdit(self)  # 创建输入框，用于显示转换结果
# # # #         self.result_output.setReadOnly(True)  # 设置输入框为只读，不允许用户编辑

# # # #         self.convert_button = QPushButton('转换', self)  # 创建按钮，用于触发转换操作
# # # #         self.convert_button.clicked.connect(self.convert_currency)  # 连接按钮的点击事件到convert_currency方法

# # # #         # 创建垂直布局
# # # #         layout = QVBoxLayout()
# # # #         layout.addWidget(self.amount_label)  # 将金额标签添加到布局
# # # #         layout.addWidget(self.amount_input)  # 将金额输入框添加到布局
# # # #         layout.addWidget(self.from_currency_label)  # 将源货币标签添加到布局
# # # #         layout.addWidget(self.from_currency)  # 将源货币下拉框添加到布局
# # # #         layout.addWidget(self.to_currency_label)  # 将目标货币标签添加到布局
# # # #         layout.addWidget(self.to_currency)  # 将目标货币下拉框添加到布局
# # # #         layout.addWidget(self.rate_label)  # 将汇率标签添加到布局
# # # #         layout.addWidget(self.rate_input)  # 将汇率输入框添加到布局
# # # #         layout.addWidget(self.result_label)  # 将结果标签添加到布局
# # # #         layout.addWidget(self.result_output)  # 将结果输出框添加到布局
# # # #         layout.addWidget(self.convert_button)  # 将转换按钮添加到布局

# # # #         self.setLayout(layout)  # 将布局设置为该对话框的布局

# # # #     def convert_currency(self):
# # # #         # 定义转换货币的方法
# # # #         try:
# # # #             amount = float(self.amount_input.text())  # 获取输入的金额并转换为浮点数
# # # #             rate = float(self.rate_input.text())  # 获取输入的汇率并转换为浮点数

# # # #             result = amount * rate  # 计算转换结果
# # # #             self.result_output.setText(f'{result:.2f}')  # 将结果显示在结果输出框，保留两位小数
# # # #         except ValueError:
# # # #             self.result_output.setText("输入无效")  # 如果输入无效，则在结果输出框显示错误信息

# # # # # 程序入口
# # # # if __name__ == '__main__':
# # # #     app = QApplication(sys.argv)  # 创建应用程序对象
# # # #     calc = Calculator()  # 创建计算器对象
# # # #     calc.show()  # 显示计算器窗口
# # # #     sys.exit(app.exec_())  # 启动应用程序的事件循环

# # # # # import tkinter as tk
# # # # # import math

# # # # # root=tk.Tk()
# # # # # root.title('计算器')
# # # # # root.geometry("500x700")
# # # # # root.iconbitmap(r'C:\Users\26515\Desktop\program\favicon.ico')   # 设置窗口图标

# # # # # expression=""

# # # # # #定义一个显示表达式的功能
# # # # # def display_expression(value):
# # # # #     global expression
# # # # #     expression+=str(value)
# # # # #     display_var.set(expression)

# # # # # #计算函数
# # # # # def calculate():
# # # # #     global expression
# # # # #     try:
# # # # #         result=str(eval)

# # # # # #创建显示屏
# # # # # display_var=tk.StringVar()
# # # # # display=tk.Entry(root,textvariable=display_var,font=("楷书",14),bd=2,width=20)


# # # # # root.mainloop()

# # import sys
# # from PyQt5.QtWidgets import (
# #     QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMdiArea, QMdiSubWindow,
# #     QFontDialog, QMessageBox
# # )
# # from PyQt5.QtCore import Qt
# # from PyQt5.QtGui import QFont


# # class SimpleEditor(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("简单多文档文本编辑器")
# #         self.setGeometry(100, 100, 800, 600)

# #         # 使用 QMdiArea 作为中心部件，用于多文档管理
# #         self.mdi_area = QMdiArea()
# #         self.setCentralWidget(self.mdi_area)

# #         # 默认开启 TabbedView 模式，标签页显示文档
# #         self.mdi_area.setViewMode(QMdiArea.ViewMode.TabbedView)

# #         # 初始化菜单栏
# #         self.init_menu()

# #     def init_menu(self):
# #         menubar = self.menuBar()

# #         # 文件菜单
# #         file_menu = menubar.addMenu("文件")
# #         new_action = QAction("新建", self)
# #         new_action.triggered.connect(self.new_document)
# #         file_menu.addAction(new_action)

# #         open_action = QAction("打开", self)
# #         open_action.triggered.connect(self.open_document)
# #         file_menu.addAction(open_action)

# #         save_action = QAction("保存", self)
# #         save_action.triggered.connect(self.save_document)
# #         file_menu.addAction(save_action)

# #         # 排列菜单：水平平铺和垂直平铺
# #         window_menu = menubar.addMenu("窗口")
# #         tile_action = QAction("水平平铺", self)
# #         tile_action.triggered.connect(self.tile_windows)
# #         window_menu.addAction(tile_action)

# #         cascade_action = QAction("垂直平铺", self)
# #         cascade_action.triggered.connect(self.cascade_windows)
# #         window_menu.addAction(cascade_action)

# #         tabbed_mode_action = QAction("标签模式", self)
# #         tabbed_mode_action.triggered.connect(self.toggle_tabbed_mode)
# #         window_menu.addAction(tabbed_mode_action)

# #         # 字体设置
# #         font_action = QAction("设置字体", self)
# #         font_action.triggered.connect(self.set_font)
# #         menubar.addAction(font_action)

# #     # 新建文档功能
# #     def new_document(self):
# #         text_edit = QTextEdit()
# #         sub_window = QMdiSubWindow()
# #         sub_window.setWidget(text_edit)
# #         sub_window.setAttribute(Qt.WA_DeleteOnClose)
# #         self.mdi_area.addSubWindow(sub_window)
# #         sub_window.show()

# #     # 打开文档功能
# #     def open_document(self):
# #         options = QFileDialog.Options()
# #         file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
# #         if file_name:
# #             with open(file_name, 'r', encoding='utf-8') as file:
# #                 content = file.read()
# #                 text_edit = QTextEdit()
# #                 text_edit.setPlainText(content)
# #                 sub_window = QMdiSubWindow()
# #                 sub_window.setWidget(text_edit)
# #                 sub_window.setAttribute(Qt.WA_DeleteOnClose)
# #                 self.mdi_area.addSubWindow(sub_window)
# #                 sub_window.show()

# #     # 保存文档功能
# #     def save_document(self):
# #         current_sub_window = self.mdi_area.activeSubWindow()
# #         if current_sub_window is not None:
# #             text_edit = current_sub_window.widget()
# #             options = QFileDialog.Options()
# #             file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
# #             if file_name:
# #                 with open(file_name, 'w', encoding='utf-8') as file:
# #                     content = text_edit.toPlainText()
# #                     file.write(content)

# #     # 设置字体
# #     def set_font(self):
# #         font, ok = QFontDialog.getFont()
# #         if ok:
# #             current_sub_window = self.mdi_area.activeSubWindow()
# #             if current_sub_window is not None:
# #                 text_edit = current_sub_window.widget()
# #                 text_edit.setFont(font)

# #     # 水平平铺窗口
# #     def tile_windows(self):
# #         self.mdi_area.tileSubWindows()

# #     # 垂直平铺窗口
# #     def cascade_windows(self):
# #         self.mdi_area.cascadeSubWindows()

# #     # 切换到标签页模式
# #     def toggle_tabbed_mode(self):
# #         if self.mdi_area.viewMode() == QMdiArea.SubWindowView:
# #             self.mdi_area.setViewMode(QMdiArea.ViewMode.TabbedView)
# #         else:
# #             self.mdi_area.setViewMode(QMdiArea.SubWindowView)


# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     window = SimpleEditor()
# #     window.show()
# #     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMdiArea, QMdiSubWindow,
#     QFontDialog, QMessageBox
# )
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont, QTextCursor, QTextCharFormat, QColor
# from spellchecker import SpellChecker


# class SimpleEditor(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("简单多文档文本编辑器")
#         self.setGeometry(100, 100, 800, 600)

#         # 使用 QMdiArea 作为中心部件，用于多文档管理
#         self.mdi_area = QMdiArea()
#         self.setCentralWidget(self.mdi_area)

#         # 拼写检查器
#         self.spell_checker = SpellChecker()

#         # 默认开启 TabbedView 模式，标签页显示文档
#         self.mdi_area.setViewMode(QMdiArea.ViewMode.TabbedView)

#         # 初始化菜单栏
#         self.init_menu()

#     def init_menu(self):
#         menubar = self.menuBar()

#         # 文件菜单
#         file_menu = menubar.addMenu("文件")
#         new_action = QAction("新建", self)
#         new_action.triggered.connect(self.new_document)
#         file_menu.addAction(new_action)

#         open_action = QAction("打开", self)
#         open_action.triggered.connect(self.open_document)
#         file_menu.addAction(open_action)

#         save_action = QAction("保存", self)
#         save_action.triggered.connect(self.save_document)
#         file_menu.addAction(save_action)

#         # 拼写检查菜单
#         spell_menu = menubar.addMenu("拼写检查")
#         check_spell_action = QAction("检查拼写", self)
#         check_spell_action.triggered.connect(self.check_spelling)
#         spell_menu.addAction(check_spell_action)

#         # 字体设置
#         font_action = QAction("设置字体", self)
#         font_action.triggered.connect(self.set_font)
#         menubar.addAction(font_action)

#     # 新建文档功能
#     def new_document(self):
#         text_edit = QTextEdit()
#         sub_window = QMdiSubWindow()
#         sub_window.setWidget(text_edit)
#         sub_window.setAttribute(Qt.WA_DeleteOnClose)
#         self.mdi_area.addSubWindow(sub_window)
#         sub_window.show()

#     # 打开文档功能
#     def open_document(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
#         if file_name:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 content = file.read()
#                 text_edit = QTextEdit()
#                 text_edit.setPlainText(content)
#                 sub_window = QMdiSubWindow()
#                 sub_window.setWidget(text_edit)
#                 sub_window.setAttribute(Qt.WA_DeleteOnClose)
#                 self.mdi_area.addSubWindow(sub_window)
#                 sub_window.show()

#     # 保存文档功能
#     def save_document(self):
#         current_sub_window = self.mdi_area.activeSubWindow()
#         if current_sub_window is not None:
#             text_edit = current_sub_window.widget()
#             options = QFileDialog.Options()
#             file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
#             if file_name:
#                 with open(file_name, 'w', encoding='utf-8') as file:
#                     content = text_edit.toPlainText()
#                     file.write(content)

#     # 设置字体
#     def set_font(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             current_sub_window = self.mdi_area.activeSubWindow()
#             if current_sub_window is not None:
#                 text_edit = current_sub_window.widget()
#                 text_edit.setFont(font)

#     # 拼写检查功能
#     def check_spelling(self):
#         current_sub_window = self.mdi_area.activeSubWindow()
#         if current_sub_window is not None:
#             text_edit = current_sub_window.widget()
#             text = text_edit.toPlainText()
            
#             # 清除之前的高亮
#             self.clear_spell_highlight(text_edit)

#             # 分割为单词
#             words = text.split()

#             # 拼写错误的单词
#             misspelled = self.spell_checker.unknown(words)

#             # 使用 QTextCursor 遍历所有单词并进行高亮
#             cursor = text_edit.textCursor()
#             cursor.beginEditBlock()  # 开始编辑块，批量更新

#             for word in misspelled:
#                 self.highlight_word(text_edit, word, cursor)

#             cursor.endEditBlock()  # 结束编辑块
#             QMessageBox.information(self, "拼写检查", f"拼写检查完成，有 {len(misspelled)} 个拼写错误。")

#     # 高亮拼写错误的单词（红色波浪下划线）
#     def highlight_word(self, text_edit, word, cursor):
#         cursor.movePosition(QTextCursor.Start)
#         while cursor.find(word):
#             format = QTextCharFormat()
#             format.setUnderlineColor(QColor("red"))
#             format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
#             cursor.mergeCharFormat(format)

#     # 清除拼写检查高亮
#     def clear_spell_highlight(self, text_edit):
#         cursor = text_edit.textCursor()
#         cursor.select(QTextCursor.Document)
#         format = QTextCharFormat()
#         format.setUnderlineStyle(QTextCharFormat.NoUnderline)  # 去除波浪线
#         cursor.mergeCharFormat(format)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SimpleEditor()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
import math

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        self.initUI()

    def initUI(self):
        # 创建主布局
        vbox = QVBoxLayout()

        # 创建显示屏
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px; height: 50px;")
        vbox.addWidget(self.display)

        # 创建网格布局来存放按钮
        grid = QGridLayout()

        # 定义按钮文本及其在网格中的位置
        buttons = [
            ('%', 0, 0), ('CE', 0, 1), ('C', 0, 2), ('⌫', 0, 3),
            ('1/x', 1, 0), ('x²', 1, 1), ('²√x', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('±', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),
        ]

        # 遍历每个按钮，并将其添加到网格布局中
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 18px; height: 40px;")
            button.clicked.connect(self.on_button_clicked)
            grid.addWidget(button, row, col)

        # 将网格布局添加到主布局
        vbox.addLayout(grid)
        self.setLayout(vbox)

    def on_button_clicked(self):
        # 获取发送信号的按钮
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.display.clear()  # 清空屏幕
        elif text == 'CE':
            self.display.clear()  # 清空屏幕，功能与C相同
        elif text == '⌫':
            # 回退一个字符
            current_text = self.display.text()
            self.display.setText(current_text[:-1])
        elif text == '=':
            # 执行计算
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        elif text == '1/x':
            try:
                value = float(self.display.text())
                result = str(1 / value)
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        elif text == 'x²':
            try:
                value = float(self.display.text())
                result = str(value ** 2)
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        elif text == '²√x':
            try:
                value = float(self.display.text())
                result = str(math.sqrt(value))
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        elif text == '±':
            try:
                value = float(self.display.text())
                result = str(-value)
                self.display.setText(result)
            except Exception:
                self.display.setText('Error')
        else:
            # 将按钮的文本添加到屏幕
            self.display.setText(self.display.text() + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
