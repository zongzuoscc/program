import tkinter as tk  # 导入 tkinter 库，用于创建图形用户界面
import math           # 导入 math 库，用于数学计算，例如平方根

# 创建一个窗口
root = tk.Tk()        # 实例化一个 Tkinter 的根窗口对象，所有的 GUI 元素都将在这个窗口中创建
root.title("简易计算器")  # 设置窗口的标题
root.geometry("400x600")  # 设置窗口的大小为 400x600 像素

# 全局变量，用来存储表达式
expression = ""  # 字符串变量，用于存储用户输入的数学表达式

# 更新显示屏上的文本
def update_display(value):
    global expression        # 指定使用全局变量 expression
    expression += str(value)  # 将用户点击的按钮值（数字或运算符）追加到表达式中
    display_var.set(expression)  # 使用 set() 函数更新显示屏上的文本，显示当前的表达式

# 计算表达式并显示结果
def calculate():
    global expression        # 使用全局变量 expression
    try:
        result = str(eval(expression))  # 使用 eval() 函数计算表达式，将结果转换为字符串存储
        display_var.set(result)         # 将计算结果显示在屏幕上
        expression = result  # 结果变成下一次的表达式初始值，这样可以继续在上次的结果基础上计算
    except:  # 如果表达式无效，执行以下内容
        display_var.set("错误")  # 显示“错误”信息
        expression = ""  # 重置表达式为空字符串

# 清除显示屏
def clear():
    global expression        # 使用全局变量 expression
    expression = ""          # 将表达式置为空
    display_var.set("")      # 清空显示屏上的内容

# 退格功能：删除最后一个字符
def backspace():
    global expression        # 使用全局变量 expression
    expression = expression[:-1]  # 使用字符串切片删除最后一个字符
    display_var.set(expression)   # 更新显示屏上的表达式

# 求倒数功能
def reciprocal():
    global expression        # 使用全局变量 expression
    try:
        result = 1 / float(expression)  # 将表达式转换为浮点数后，计算其倒数
        display_var.set(str(result))    # 将结果转换为字符串并显示在屏幕上
        expression = str(result)        # 将结果赋值给 expression，以便进行进一步的计算
    except:  # 如果出现错误（如除以零），执行以下内容
        display_var.set("错误")  # 显示错误信息
        expression = ""          # 重置表达式为空字符串

# 求平方根功能
def sqrt():
    global expression        # 使用全局变量 expression
    try:
        result = math.sqrt(float(expression))  # 使用 math.sqrt() 函数计算平方根
        display_var.set(str(result))           # 将结果显示在屏幕上
        expression = str(result)               # 将结果作为新的表达式
    except:  # 如果输入无效，执行以下内容
        display_var.set("错误")  # 显示错误信息
        expression = ""          # 重置表达式

# 创建显示屏
display_var = tk.StringVar()  # 创建一个 StringVar() 对象，作为显示屏中文本的控制变量
display = tk.Entry(root, textvariable=display_var, font=("宋体", 24), bd=10, insertwidth=2, width=24, borderwidth=4)
# 创建一个文本输入框 (Entry) ，用于显示当前输入的表达式和结果
# 参数：
#   root：父窗口
#   textvariable=display_var：显示屏中的内容由 display_var 控制
#   font=("Arial", 24)：设置字体为 Arial，字号为 24
#   bd=10：设置边框宽度
#   insertwidth=2：设置光标的宽度
#   width=24：设置输入框的宽度为 24 个字符
#   borderwidth=4：设置边框宽度

display.grid(row=0, column=0, columnspan=4)  # 使用 grid 布局，将显示屏放置在第 0 行，占据 4 列

# 定义按钮样式
button_font = ("宋体", 18)  # 设定按钮字体样式，宋体 字体，字号 18

# 数字按钮和运算符按钮的定义（新增了括号）
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),  # 第一行：数字 7, 8, 9 和除号 /
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),  # 第二行：数字 4, 5, 6 和乘号 *
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),  # 第三行：数字 1, 2, 3 和减号 -
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),  # 第四行：数字 0，小数点，百分号和加号 +
    ('(', 5, 0), (')', 5, 1), ('=', 5, 3)  # 第五行：左括号，右括号和等号
]

# 动态生成按钮
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=calculate).grid(row=row, column=col, sticky="nsew")
        # 如果按钮是 '='，创建一个按钮并绑定 calculate 函数，按下时计算表达式
    else:
        tk.Button(root, text=text, padx=20, pady=20, font=button_font, command=lambda t=text: update_display(t)).grid(row=row, column=col, sticky="nsew")
        # 对其他按钮，生成按钮，并绑定 update_display 函数，当按下时将对应的文本更新到表达式中
        # lambda 表达式用于传递当前的按钮文本给 update_display 函数

# 清除按钮
tk.Button(root, text='清除', padx=20, pady=20, font=button_font, command=clear).grid(row=6, column=0, columnspan=4, sticky="nsew")
# 创建 "清除" 按钮，并绑定 clear 函数，按下后清除表达式

# 退格按钮
tk.Button(root, text='退格', padx=20, pady=20, font=button_font, command=backspace).grid(row=6, column=2, sticky="nsew")
# 创建 "退格" 按钮，并绑定 backspace 函数，按下后删除最后一个字符

# 倒数按钮
tk.Button(root, text='1/x', padx=20, pady=20, font=button_font, command=reciprocal).grid(row=6, column=1, sticky="nsew")
# 创建 "1/x" 按钮，并绑定 reciprocal 函数，按下后计算倒数

# 平方根按钮
tk.Button(root, text='√', padx=20, pady=20, font=button_font, command=sqrt).grid(row=6, column=3, sticky="nsew")
# 创建 "√" 按钮，并绑定 sqrt 函数，按下后计算平方根

# 调整行列权重
for i in range(7):
    root.grid_rowconfigure(i, weight=1)  # 为每一行设置相同的权重，确保窗口调整大小时每行等比例变化
for i in range(4):
    root.grid_columnconfigure(i, weight=1)  # 为每一列设置相同的权重，确保窗口调整大小时每列等比例变化

# 开始主循环
root.mainloop()  # 进入 Tkinter 主循环，开始运行 GUI 程序
