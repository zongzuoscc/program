# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
#     QVBoxLayout, QWidget, QFontDialog, QMessageBox, QTabWidget,
#     QDialog, QLineEdit, QLabel, QPushButton, QInputDialog
# )
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QFont 


# class SimpleMDIExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("简单多文档文本编辑器")
#         self.setGeometry(100, 100, 800, 600)

#         # 主窗口中心部件，使用TabWidget来管理多个文本编辑器
#         self.tab_widget = QTabWidget()
#         self.setCentralWidget(self.tab_widget)

#         # 用于保存查找游标的变量
#         self.search_cursor = None

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

#     # 新建文档功能
#     def new_document(self):
#         text_edit = QTextEdit()
#         text_edit.document().setModified(False)  # 标记为未修改
#         self.tab_widget.addTab(text_edit, "无标题")
#         self.tab_widget.setCurrentWidget(text_edit)

#     # 打开文档功能
#     def open_document(self):
#         options = QFileDialog.Options()
#         file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
#         if file_name:
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 content = file.read()
#                 text_edit = QTextEdit()
#                 text_edit.setPlainText(content)
#                 text_edit.document().setModified(False)  # 标记为未修改
#                 self.tab_widget.addTab(text_edit, file_name)
#                 self.tab_widget.setCurrentWidget(text_edit)

#     # 保存文档功能
#     def save_document(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             if current_widget.document().isModified():
#                 options = QFileDialog.Options()
#                 file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
#                 if file_name:
#                     with open(file_name, 'w', encoding='utf-8') as file:
#                         content = current_widget.toPlainText()
#                         file.write(content)
#                     current_widget.document().setModified(False)  # 保存后标记为未修改

#     # 字体设置
#     def set_font(self):
#         font, ok = QFontDialog.getFont()
#         if ok:
#             current_widget = self.tab_widget.currentWidget()
#             if current_widget is not None:
#                 current_widget.setFont(font)

#     # 粗体切换
#     def toggle_bold(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             if not cursor.hasSelection():
#                 # 如果没有选中文本，则返回
#                 return
#             # 切换粗体
#             fmt = cursor.charFormat()
#             fmt.setFontWeight(QFont.Bold if fmt.fontWeight() != QFont.Bold else QFont.Normal)
#             cursor.mergeCharFormat(fmt)

#     # 斜体切换
#     def toggle_italic(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             if not cursor.hasSelection():
#                 return
#             fmt = cursor.charFormat()
#             fmt.setFontItalic(not fmt.fontItalic())
#             cursor.mergeCharFormat(fmt)

#     # 下划线切换
#     def toggle_underline(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             if not cursor.hasSelection():
#                 return
#             fmt = cursor.charFormat()
#             fmt.setFontUnderline(not fmt.fontUnderline())
#             cursor.mergeCharFormat(fmt)

#     # 左对齐
#     def align_left(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.setAlignment(Qt.AlignLeft)

#     # 居中对齐
#     def align_center(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.setAlignment(Qt.AlignCenter)

#     # 右对齐
#     def align_right(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.setAlignment(Qt.AlignRight)

#     # 撤销
#     def undo(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.undo()

#     # 重做
#     def redo(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.redo()

#     # 复制
#     def copy(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.copy()

#     # 剪切
#     def cut(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.cut()

#     # 粘贴
#     def paste(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             current_widget.paste()

#     # 清除所有高亮
#     def clear_search_highlight(self):
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             cursor = current_widget.textCursor()
#             cursor.select(QTextCursor.Document)
#             default_format = QTextCharFormat()
#             cursor.setCharFormat(default_format)

#     # 查找功能
#     def find_text(self):
#         text, ok = QInputDialog.getText(self, "查找", "请输入要查找的文本:")
#         if ok and text:
#             current_widget = self.tab_widget.currentWidget()
#             if current_widget is not None:
#                 self.clear_search_highlight()  # 清除之前的高亮

#                 # 创建文本游标并重置到文档开头
#                 cursor = current_widget.textCursor()
#                 cursor.movePosition(QTextCursor.Start)

#                 # 设置文本格式
#                 highlight_format = QTextCharFormat()
#                 highlight_format.setBackground(QColor("yellow"))  # 普通高亮颜色

#                 current_highlight_format = QTextCharFormat()
#                 current_highlight_format.setBackground(QColor("yellow"))  # 当前查找到的颜色

#                 document = current_widget.document()
#                 self.search_cursor = cursor
#                 count = 0  # 计数变量
#                 while True:
#                     cursor = document.find(text, self.search_cursor)
#                     if cursor.isNull():
#                         break  # 如果找不到下一个，则退出循环

#                     # 高亮显示文本
#                     cursor.mergeCharFormat(highlight_format)
#                     self.search_cursor = cursor  # 更新查找游标
#                     count += 1  # 增加计数

#                 # 查找到第一个结果并设置不同颜色
#                 cursor = document.find(text)
#                 if not cursor.isNull():
#                     cursor.mergeCharFormat(current_highlight_format)  # 使用高亮当前查找到的内容

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
#         current_widget = self.tab_widget.currentWidget()
#         if current_widget is not None:
#             text = current_widget.toPlainText()
#             new_text, count = text.replace(find_text, replace_text), text.count(find_text)  # 计数替换
#             current_widget.setPlainText(new_text)
#             dialog.accept()
#             QMessageBox.information(self, "替换结果", f"完成替换 {count} 处。")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mainWin = SimpleMDIExample()
#     mainWin.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QVBoxLayout, QWidget, QFontDialog, QMessageBox, QMdiArea, QMdiSubWindow,
    QDialog, QLineEdit, QLabel, QPushButton, QInputDialog
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor, QFont


class SimpleMDIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("简单多文档文本编辑器")
        self.setGeometry(100, 100, 800, 600)

        # 主窗口中心部件，使用MdiArea来管理多个子窗口
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 用于保存查找游标的变量
        self.search_cursor = None

        # 初始化菜单栏
        self.init_menu()

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
        text_edit = QTextEdit()
        sub_window = QMdiSubWindow()  # 创建一个子窗口
        sub_window.setWidget(text_edit)
        sub_window.setAttribute(Qt.WA_DeleteOnClose)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

    # 打开文档功能
    def open_document(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                text_edit = QTextEdit()
                text_edit.setPlainText(content)
                sub_window = QMdiSubWindow()
                sub_window.setWidget(text_edit)
                sub_window.setAttribute(Qt.WA_DeleteOnClose)
                self.mdi_area.addSubWindow(sub_window)
                sub_window.show()

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

    # 水平平铺
    def tile_horizontally(self):
        sub_windows = self.mdi_area.subWindowList()
        if not sub_windows:
            return

        total_width = self.mdi_area.width()
        height = self.mdi_area.height() // len(sub_windows)

        for i, sub_window in enumerate(sub_windows):
            sub_window.setGeometry(0, i * height, total_width, height)

    # 垂直平铺
    def tile_vertically(self):
        sub_windows = self.mdi_area.subWindowList()
        if not sub_windows:
            return

        total_height = self.mdi_area.height()
        width = self.mdi_area.width() // len(sub_windows)

        for i, sub_window in enumerate(sub_windows):
            sub_window.setGeometry(i * width, 0, width, total_height)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = SimpleMDIExample()
    mainWin.show()
    sys.exit(app.exec_())
