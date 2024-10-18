# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
#     QVBoxLayout, QWidget, QFontDialog, QMessageBox, QMdiArea, QMdiSubWindow,
#     QDialog, QLineEdit, QLabel, QPushButton, QInputDialog, QStatusBar
# )
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QFont


# class SimpleMDIExample(QMainWindow):
#     def __init__(self):
#         super().__init__()#super函数用来调用父类，init是类的初始化方法

#         self.setWindowTitle("不简单多文档文本编辑器")#设置标题
#         self.setGeometry(100, 100, 800, 600)#设置窗口位置和大小

#         # 主窗口中心部件，使用MdiArea来管理多个子窗口
#         self.mdi_area = QMdiArea()
#         self.setCentralWidget(self.mdi_area) # 设置多文档区域为主窗口的中心部件

#         # 用于保存查找游标的变量
#         self.search_cursor = None

#         # 初始化菜单栏
#         self.init_menu()

#         # 初始化状态栏，用于显示字数
#         self.status_bar = QStatusBar()
#         self.setStatusBar(self.status_bar)

#     #初始化菜单函数
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

#         # 字体设置
#         font_action = QAction("设置字体", self)
#         font_action.triggered.connect(self.set_font)
#         file_menu.addAction(font_action)

#         # 格式菜单
#         format_menu = menubar.addMenu("格式")
#         bold_action = QAction("粗体", self)
#         bold_action.triggered.connect(self.toggle_bold)
#         format_menu.addAction(bold_action)

#         italic_action = QAction("斜体", self)
#         italic_action.triggered.connect(self.toggle_italic)
#         format_menu.addAction(italic_action)

#         underline_action = QAction("下划线", self)
#         underline_action.triggered.connect(self.toggle_underline)
#         format_menu.addAction(underline_action)

#         # 对齐方式
#         align_menu = format_menu.addMenu("对齐方式")
#         align_left_action = QAction("左对齐", self)
#         align_left_action.triggered.connect(self.align_left)
#         align_menu.addAction(align_left_action)

#         align_center_action = QAction("居中对齐", self)
#         align_center_action.triggered.connect(self.align_center)
#         align_menu.addAction(align_center_action)

#         align_right_action = QAction("右对齐", self)
#         align_right_action.triggered.connect(self.align_right)
#         align_menu.addAction(align_right_action)

#         # 编辑菜单
#         edit_menu = menubar.addMenu("编辑")
#         undo_action = QAction("撤销", self)
#         undo_action.triggered.connect(self.undo)
#         edit_menu.addAction(undo_action)

#         redo_action = QAction("重做", self)
#         redo_action.triggered.connect(self.redo)
#         edit_menu.addAction(redo_action)

#         copy_action = QAction("复制", self)
#         copy_action.triggered.connect(self.copy)
#         edit_menu.addAction(copy_action)

#         cut_action = QAction("剪切", self)
#         cut_action.triggered.connect(self.cut)
#         edit_menu.addAction(cut_action)

#         paste_action = QAction("粘贴", self)
#         paste_action.triggered.connect(self.paste)
#         edit_menu.addAction(paste_action)

#         find_action = QAction("查找", self)
#         find_action.triggered.connect(self.find_text)
#         edit_menu.addAction(find_action)

#         replace_action = QAction("替换", self)
#         replace_action.triggered.connect(self.replace_text)
#         edit_menu.addAction(replace_action)

#         clear_search_action = QAction("清除高亮", self)
#         clear_search_action.triggered.connect(self.clear_search_highlight)
#         edit_menu.addAction(clear_search_action)

#         # 窗口菜单
#         window_menu = menubar.addMenu("窗口")
#         cascade_action = QAction("层叠窗口", self)
#         cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)
#         window_menu.addAction(cascade_action)

#         tile_horizontally_action = QAction("水平平铺", self)
#         tile_horizontally_action.triggered.connect(self.tile_horizontally)
#         window_menu.addAction(tile_horizontally_action)

#         tile_vertically_action = QAction("垂直平铺", self)
#         tile_vertically_action.triggered.connect(self.tile_vertically)
#         window_menu.addAction(tile_vertically_action)

#     # 新建文档功能 yes
#     def new_document(self):
#         text_edit = QTextEdit()
#         text_edit.cursorPositionChanged.connect(self.update_status_bar)
#         text_edit.textChanged.connect(self.update_status_bar)

#         sub_window = QMdiSubWindow()  # 创建一个子窗口
#         sub_window.setWidget(text_edit)
#         sub_window.setAttribute(Qt.WA_DeleteOnClose)
#         self.mdi_area.addSubWindow(sub_window)
#         sub_window.show()

#         self.update_status_bar()  # 初始化时更新状态栏

#     # 打开文档功能 yes
#     def open_document(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
#         if file_name:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 content = file.read()
#                 text_edit = QTextEdit()
#                 text_edit.setPlainText(content)
#                 text_edit.cursorPositionChanged.connect(self.update_status_bar)
#                 text_edit.textChanged.connect(self.update_status_bar)

#                 sub_window = QMdiSubWindow()
#                 sub_window.setWidget(text_edit)
#                 sub_window.setAttribute(Qt.WA_DeleteOnClose)
#                 self.mdi_area.addSubWindow(sub_window)
#                 sub_window.show()

#                 self.update_status_bar()  # 打开文档时更新状态栏

#     # 保存文档功能 yes
#     def save_document(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             if current_widget.document().isModified():
#                 options = QFileDialog.Options()
#                 file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
#                 if file_name:
#                     with open(file_name, 'w', encoding='utf-8') as file:
#                         content = current_widget.toPlainText()
#                         file.write(content)
#                     current_widget.document().setModified(False)  # 保存后标记为未修改

#     # 状态栏更新
#     def update_status_bar(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()

#             # 获取当前行和列
#             block_number = cursor.blockNumber() + 1
#             column_number = cursor.columnNumber() + 1

#             # 获取总字符数
#             total_chars = len(current_widget.toPlainText())

#             # 获取选中文字字符数
#             selected_chars = len(cursor.selectedText())

#             # 更新状态栏
#             self.status_bar.showMessage(f"行 {block_number}, 列 {column_number} | 选中 {selected_chars} 个字符, 共 {total_chars} 个字符")

#     # 字体设置 yes
#     def set_font(self):
#         font, ok = QFontDialog.getFont()
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if ok and current_widget is not None:
#             current_widget.setFont(font)

#     # 粗体切换 yes
#     def toggle_bold(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             if not cursor.hasSelection():
#                 return
#             fmt = cursor.charFormat()
#             fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
#             cursor.mergeCharFormat(fmt)

#     # 斜体切换 yes
#     def toggle_italic(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             if not cursor.hasSelection():
#                 return
#             fmt = cursor.charFormat()
#             fmt.setFontItalic(not fmt.fontItalic())
#             cursor.mergeCharFormat(fmt)

#     # 下划线切换 yes
#     def toggle_underline(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             if not cursor.hasSelection():
#                 return
#             fmt = cursor.charFormat()
#             fmt.setFontUnderline(not fmt.fontUnderline())
#             cursor.mergeCharFormat(fmt)

#     # 左对齐 yes
#     def align_left(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.setAlignment(Qt.AlignLeft)

#     # 居中对齐 yes
#     def align_center(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.setAlignment(Qt.AlignCenter)

#     # 右对齐 yes
#     def align_right(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.setAlignment(Qt.AlignRight)

#     # 撤销 yes
#     def undo(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.undo()

#     # 重做 yes
#     def redo(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.redo()

#     # 复制 yes
#     def copy(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.copy()

#     # 剪切 yes
#     def cut(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.cut()

#     # 粘贴 yes
#     def paste(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             current_widget.paste()

#     # 清除所有高亮
#     def clear_search_highlight(self):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             cursor.select(QTextCursor.Document)
#             default_format = QTextCharFormat()
#             cursor.setCharFormat(default_format)

#     # 查找功能
#     def find_text(self):
#         text, ok = QInputDialog.getText(self, "查找", "请输入要查找的文本:")
#         if ok and text:
#             current_widget = self.mdi_area.activeSubWindow().widget()
#             if current_widget is not None:
#                 self.clear_search_highlight()  # 清除之前的高亮

#                 cursor = current_widget.textCursor()
#                 cursor.movePosition(QTextCursor.Start)

#                 highlight_format = QTextCharFormat()
#                 highlight_format.setBackground(QColor("yellow"))

#                 current_highlight_format = QTextCharFormat()
#                 current_highlight_format.setBackground(QColor("yellow"))

#                 document = current_widget.document()
#                 self.search_cursor = cursor
#                 count = 0  # 计数
#                 while True:
#                     cursor = document.find(text, self.search_cursor)
#                     if cursor.isNull():
#                         break

#                     cursor.mergeCharFormat(highlight_format)
#                     self.search_cursor = cursor
#                     count += 1

#                 cursor = document.find(text)
#                 if not cursor.isNull():
#                     cursor.mergeCharFormat(current_highlight_format)

#                 QMessageBox.information(self, "查找结果", f"找到 {count} 个匹配项。")

#     # 替换功能
#     def replace_text(self):
#         dialog = QDialog(self)
#         dialog.setWindowTitle("替换文本")
#         layout = QVBoxLayout(dialog)

#         layout.addWidget(QLabel("查找:"))
#         find_input = QLineEdit(dialog)
#         layout.addWidget(find_input)

#         layout.addWidget(QLabel("替换为:"))
#         replace_input = QLineEdit(dialog)
#         layout.addWidget(replace_input)

#         replace_button = QPushButton("替换", dialog)
#         replace_button.clicked.connect(lambda: self.do_replace(find_input.text(), replace_input.text(), dialog))
#         layout.addWidget(replace_button)

#         dialog.exec_()

#     def do_replace(self, find_text, replace_text, dialog):
#         current_widget = self.mdi_area.activeSubWindow().widget()
#         if current_widget is not None:
#             text = current_widget.toPlainText()
#             new_text, count = text.replace(find_text, replace_text), text.count(find_text)
#             current_widget.setPlainText(new_text)
#             dialog.accept()
#             QMessageBox.information(self, "替换结果", f"完成替换 {count} 处。")


#     # 层叠窗口
#     def tile_horizontally(self):
#         self.mdi_area.tileSubWindows()

#     def tile_vertically(self):
#         self.mdi_area.tileSubWindows()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SimpleMDIExample()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QVBoxLayout, QWidget, QFontDialog, QMessageBox, QMdiArea, QMdiSubWindow,
    QDialog, QLineEdit, QLabel, QPushButton, QInputDialog, QStatusBar, QToolBar
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class SimpleMDIExample(QMainWindow):
    def __init__(self):
        super().__init__()#super函数用来调用父类，init是类的初始化方法

        self.setWindowTitle("不简单多文档文本编辑器")#设置标题
        self.setGeometry(100, 100, 800, 600)#设置窗口位置和大小

        # 主窗口中心部件，使用MdiArea来管理多个子窗口
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area) # 设置多文档区域为主窗口的中心部件

        # 用于保存查找游标的变量
        self.search_cursor = None

        # 初始化菜单栏
        self.init_menu()

        # 初始化状态栏，用于显示字数
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar("工具栏", self)
        toolbar.setIconSize(QSize(24, 24))  # 设置图标大小
        self.addToolBar(toolbar)

        # 新建文件按钮
        creat_new_file_action = QAction(QIcon('icons/creatnewfile.png'), '新建文件', self)
        creat_new_file_action.triggered.connect(self.new_document)
        toolbar.addAction(creat_new_file_action)

        # 打开文件按钮
        open_file_action = QAction(QIcon('icons/open.png'), '打开文件', self)
        open_file_action.triggered.connect(self.open_document)
        toolbar.addAction(open_file_action)

        # 保存文件按钮
        save_file_action = QAction(QIcon('icons/save.png'), '保存文件', self)
        save_file_action.triggered.connect(self.save_document)
        toolbar.addAction(save_file_action)

        # 字体设置按钮
        change_font_action = QAction(QIcon('icons/font.png'), '更改字体', self)
        change_font_action.triggered.connect(self.set_font)
        toolbar.addAction(change_font_action)

        # 粗体设置按钮
        bold_font_action = QAction(QIcon('icons/bold.png'), '粗体', self)
        bold_font_action.triggered.connect(self.toggle_bold)
        toolbar.addAction(bold_font_action)

        # 斜体设置按钮
        italic_font_action = QAction(QIcon('icons/italic.png'), '斜体', self)
        italic_font_action.triggered.connect(self.toggle_italic)
        toolbar.addAction(italic_font_action)

        # 下划线设置按钮
        underline_action = QAction(QIcon('icons/underline.png'), '下划线', self)
        underline_action.triggered.connect(self.toggle_underline)
        toolbar.addAction(underline_action)

        # 左对齐按钮
        left_action = QAction(QIcon('icons/left.png'), '左对齐', self)
        left_action.triggered.connect(self.align_left)
        toolbar.addAction(left_action)

        # 居中对齐按钮
        center_action = QAction(QIcon('icons/center.png'), '居中对齐', self)
        center_action.triggered.connect(self.align_center)
        toolbar.addAction(center_action)

        # 右对齐按钮
        right_action = QAction(QIcon('icons/right.png'), '右对齐', self)
        right_action.triggered.connect(self.align_right)
        toolbar.addAction(right_action)

        # 撤销按钮
        undo_action = QAction(QIcon('icons/undo.png'), '撤销', self)
        undo_action.triggered.connect(self.undo)
        toolbar.addAction(undo_action)

        # 重做按钮
        redo_action = QAction(QIcon('icons/redo.png'), '重做', self)
        redo_action.triggered.connect(self.redo)
        toolbar.addAction(redo_action)

        # 复制按钮
        copy_action = QAction(QIcon('icons/copy.png'), '复制', self)
        copy_action.triggered.connect(self.copy)
        toolbar.addAction(copy_action)

        # 粘贴按钮
        paste_action = QAction(QIcon('icons/paste.png'), '粘贴', self)
        paste_action.triggered.connect(self.paste)
        toolbar.addAction(paste_action)

        # 剪切按钮
        cut_action = QAction(QIcon('icons/cut.png'), '剪切', self)
        cut_action.triggered.connect(self.cut)
        toolbar.addAction(cut_action)

        # 查找按钮
        find_action = QAction(QIcon('icons/find.png'), '查找', self)
        find_action.triggered.connect(self.find_text)
        toolbar.addAction(find_action)

    #初始化菜单函数
    def init_menu(self):
        menubar = self.menuBar()

        # 文件菜单
        file_menu = menubar.addMenu("文件")
        new_action = QAction("新建", self)
        new_action.triggered.connect(self.new_document)
        file_menu.addAction(new_action)

        open_action = QAction("打开", self)
        open_action.triggered.connect(self.open_document)
        file_menu.addAction(open_action)

        save_action = QAction("保存", self)
        save_action.triggered.connect(self.save_document)
        file_menu.addAction(save_action)

        # 字体设置
        font_action = QAction("设置字体", self)
        font_action.triggered.connect(self.set_font)
        file_menu.addAction(font_action)

        # 格式菜单
        format_menu = menubar.addMenu("格式")
        bold_action = QAction("粗体", self)
        bold_action.triggered.connect(self.toggle_bold)
        format_menu.addAction(bold_action)

        italic_action = QAction("斜体", self)
        italic_action.triggered.connect(self.toggle_italic)
        format_menu.addAction(italic_action)

        underline_action = QAction("下划线", self)
        underline_action.triggered.connect(self.toggle_underline)
        format_menu.addAction(underline_action)

        # 对齐方式
        align_menu = format_menu.addMenu("对齐方式")
        align_left_action = QAction("左对齐", self)
        align_left_action.triggered.connect(self.align_left)
        align_menu.addAction(align_left_action)

        align_center_action = QAction("居中对齐", self)
        align_center_action.triggered.connect(self.align_center)
        align_menu.addAction(align_center_action)

        align_right_action = QAction("右对齐", self)
        align_right_action.triggered.connect(self.align_right)
        align_menu.addAction(align_right_action)

        # 编辑菜单
        edit_menu = menubar.addMenu("编辑")
        undo_action = QAction("撤销", self)
        undo_action.triggered.connect(self.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction("重做", self)
        redo_action.triggered.connect(self.redo)
        edit_menu.addAction(redo_action)

        copy_action = QAction("复制", self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)

        cut_action = QAction("剪切", self)
        cut_action.triggered.connect(self.cut)
        edit_menu.addAction(cut_action)

        paste_action = QAction("粘贴", self)
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

        find_action = QAction("查找", self)
        find_action.triggered.connect(self.find_text)
        edit_menu.addAction(find_action)

        replace_action = QAction("替换", self)
        replace_action.triggered.connect(self.replace_text)
        edit_menu.addAction(replace_action)

        clear_search_action = QAction("清除高亮", self)
        clear_search_action.triggered.connect(self.clear_search_highlight)
        edit_menu.addAction(clear_search_action)

        # 窗口菜单
        window_menu = menubar.addMenu("窗口")
        cascade_action = QAction("层叠窗口", self)
        cascade_action.triggered.connect(self.mdi_area.cascadeSubWindows)
        window_menu.addAction(cascade_action)

        tile_horizontally_action = QAction("水平平铺", self)
        tile_horizontally_action.triggered.connect(self.tile_horizontally)
        window_menu.addAction(tile_horizontally_action)

        tile_vertically_action = QAction("垂直平铺", self)
        tile_vertically_action.triggered.connect(self.tile_vertically)
        window_menu.addAction(tile_vertically_action)

    # 新建文档功能
    def new_document(self):
        text_edit = CustomTextEdit()  # 使用自定义的 QTextEdit
        text_edit.cursorPositionChanged.connect(self.update_status_bar)
        text_edit.textChanged.connect(self.update_status_bar)

        sub_window = CustomMdiSubWindow(text_edit)  # 使用自定义的子窗口
        sub_window.setWidget(text_edit)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

        self.update_status_bar()  # 初始化时更新状态栏

    # 打开文档功能
    def open_document(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                text_edit = CustomTextEdit()  # 使用自定义的 QTextEdit
                text_edit.setPlainText(content)
                text_edit.cursorPositionChanged.connect(self.update_status_bar)
                text_edit.textChanged.connect(self.update_status_bar)

                sub_window = CustomMdiSubWindow(text_edit)  # 使用自定义的子窗口
                sub_window.setWidget(text_edit)
                sub_window.setAttribute(Qt.WA_DeleteOnClose)
                self.mdi_area.addSubWindow(sub_window)
                sub_window.show()

                self.update_status_bar()  # 打开文档时更新状态栏

    # 保存文档功能
    def save_document(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            if current_widget.document().isModified():
                options = QFileDialog.Options()
                file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
                if file_name:
                    with open(file_name, 'w', encoding='utf-8') as file:
                        content = current_widget.toPlainText()
                        file.write(content)
                    current_widget.document().setModified(False)  # 保存后标记为未修改

    # 状态栏更新
    def update_status_bar(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            cursor = current_widget.textCursor()

            # 获取当前行和列
            block_number = cursor.blockNumber() + 1
            column_number = cursor.columnNumber() + 1

            # 获取总字符数
            total_chars = len(current_widget.toPlainText())

            # 获取选中文字字符数
            selected_chars = len(cursor.selectedText())

            # 更新状态栏
            self.status_bar.showMessage(f"行 {block_number}, 列 {column_number} | 选中 {selected_chars} 个字符, 共 {total_chars} 个字符")

    # 字体设置
    def set_font(self):
        font, ok = QFontDialog.getFont()
        current_widget = self.mdi_area.activeSubWindow().widget()
        if ok and current_widget is not None:
            current_widget.setFont(font)

    # 粗体切换
    def toggle_bold(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            cursor = current_widget.textCursor()
            if not cursor.hasSelection():
                return
            fmt = cursor.charFormat()
            fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
            cursor.mergeCharFormat(fmt)

    # 斜体切换
    def toggle_italic(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            cursor = current_widget.textCursor()
            if not cursor.hasSelection():
                return
            fmt = cursor.charFormat()
            fmt.setFontItalic(not fmt.fontItalic())
            cursor.mergeCharFormat(fmt)

    # 下划线切换
    def toggle_underline(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            cursor = current_widget.textCursor()
            if not cursor.hasSelection():
                return
            fmt = cursor.charFormat()
            fmt.setFontUnderline(not fmt.fontUnderline())
            cursor.mergeCharFormat(fmt)

    # 左对齐
    def align_left(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.setAlignment(Qt.AlignLeft)

    # 居中对齐
    def align_center(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.setAlignment(Qt.AlignCenter)

    # 右对齐
    def align_right(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.setAlignment(Qt.AlignRight)

    # 撤销
    def undo(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.undo()

    # 重做
    def redo(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.redo()

    # 复制
    def copy(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.copy()

    # 剪切
    def cut(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.cut()

    # 粘贴
    def paste(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            current_widget.paste()

    # 清除所有高亮
    def clear_search_highlight(self):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            cursor = current_widget.textCursor()
            cursor.select(QTextCursor.Document)
            default_format = QTextCharFormat()
            cursor.setCharFormat(default_format)

    # 查找功能
    def find_text(self):
        text, ok = QInputDialog.getText(self, "查找", "请输入要查找的文本:")
        if ok and text:
            current_widget = self.mdi_area.activeSubWindow().widget()
            if current_widget is not None:
                self.clear_search_highlight()  # 清除之前的高亮

                cursor = current_widget.textCursor()
                cursor.movePosition(QTextCursor.Start)

                highlight_format = QTextCharFormat()
                highlight_format.setBackground(QColor("yellow"))

                current_highlight_format = QTextCharFormat()
                current_highlight_format.setBackground(QColor("yellow"))

                document = current_widget.document()
                self.search_cursor = cursor
                count = 0  # 计数
                while True:
                    cursor = document.find(text, self.search_cursor)
                    if cursor.isNull():
                        break

                    cursor.mergeCharFormat(highlight_format)
                    self.search_cursor = cursor
                    count += 1

                cursor = document.find(text)
                if not cursor.isNull():
                    cursor.mergeCharFormat(current_highlight_format)

                QMessageBox.information(self, "查找结果", f"找到 {count} 个匹配项。")

    # 替换功能
    def replace_text(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("替换文本")
        layout = QVBoxLayout(dialog)

        layout.addWidget(QLabel("查找:"))
        find_input = QLineEdit(dialog)
        layout.addWidget(find_input)

        layout.addWidget(QLabel("替换为:"))
        replace_input = QLineEdit(dialog)
        layout.addWidget(replace_input)

        replace_button = QPushButton("替换", dialog)
        replace_button.clicked.connect(lambda: self.do_replace(find_input.text(), replace_input.text(), dialog))
        layout.addWidget(replace_button)

        dialog.exec_()

    def do_replace(self, find_text, replace_text, dialog):
        current_widget = self.mdi_area.activeSubWindow().widget()
        if current_widget is not None:
            text = current_widget.toPlainText()
            new_text, count = text.replace(find_text, replace_text), text.count(find_text)
            current_widget.setPlainText(new_text)
            dialog.accept()
            QMessageBox.information(self, "替换结果", f"完成替换 {count} 处。")


    # 层叠窗口
    def tile_horizontally(self):
        self.mdi_area.tileSubWindows()

    def tile_vertically(self):
        self.mdi_area.tileSubWindows()


class CustomMdiSubWindow(QMdiSubWindow):
    def __init__(self, editor, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.editor = editor

    def closeEvent(self, event):
        if self.editor.document().isModified():  # 检查文档是否被修改
            reply = QMessageBox.question(
                self, "未保存的更改",
                "文档未保存，是否保存更改？",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )

            if reply == QMessageBox.Yes:
                self.editor.save_document()  # 保存文档
                event.accept()
            elif reply == QMessageBox.No:
                event.accept()  # 直接关闭
            else:
                event.ignore()  # 取消关闭
        else:
            event.accept()


class CustomTextEdit(QTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save_document(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                content = self.toPlainText()
                file.write(content)
            self.document().setModified(False)  # 保存后标记为未修改

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleMDIExample()
    window.show()
    sys.exit(app.exec_())