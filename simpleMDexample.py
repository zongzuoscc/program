import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QAction, QFileDialog,
    QVBoxLayout, QWidget, QFontDialog, QMessageBox, QTabWidget,
    QDialog, QLineEdit, QVBoxLayout, QLabel, QPushButton, QInputDialog
)
from PyQt5.QtCore import Qt

class SimpleMDIExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("简单多文档文本编辑器")
        self.setGeometry(100, 100, 800, 600)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.init_menu()

    def init_menu(self):
        menubar = self.menuBar()

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

        font_action = QAction("设置字体", self)
        font_action.triggered.connect(self.set_font)
        file_menu.addAction(font_action)

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

        arrange_menu = menubar.addMenu("排列")
        cascade_action = QAction("层叠", self)
        cascade_action.triggered.connect(self.cascade_windows)
        arrange_menu.addAction(cascade_action)

        tile_horizontal_action = QAction("水平平铺", self)
        tile_horizontal_action.triggered.connect(self.tile_horizontal)
        arrange_menu.addAction(tile_horizontal_action)

        tile_vertical_action = QAction("垂直平铺", self)
        tile_vertical_action.triggered.connect(self.tile_vertical)
        arrange_menu.addAction(tile_vertical_action)

    def new_document(self):
        text_edit = QTextEdit()
        text_edit.document().setModified(False)  # 标记为未修改
        self.tab_widget.addTab(text_edit, "无标题")
        self.tab_widget.setCurrentWidget(text_edit)

    def open_document(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文本文件", "", "文本文件 (*.txt)", options=options)
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                content = file.read()
                text_edit = QTextEdit()
                text_edit.setPlainText(content)
                text_edit.document().setModified(False)  # 标记为未修改
                self.tab_widget.addTab(text_edit, file_name)
                self.tab_widget.setCurrentWidget(text_edit)

    def save_document(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            if current_widget.document().isModified():
                options = QFileDialog.Options()
                file_name, _ = QFileDialog.getSaveFileName(self, "保存文本文件", "", "文本文件 (*.txt)", options=options)
                if file_name:
                    with open(file_name, 'w', encoding='utf-8') as file:
                        content = current_widget.toPlainText()
                        file.write(content)
                    current_widget.document().setModified(False)  # 保存后标记为未修改

    def set_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            current_widget = self.tab_widget.currentWidget()
            if current_widget is not None:
                current_widget.setFont(font)

    def toggle_bold(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            font = current_widget.font()
            font.setBold(not font.bold())
            current_widget.setFont(font)

    def toggle_italic(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            font = current_widget.font()
            font.setItalic(not font.italic())
            current_widget.setFont(font)

    def toggle_underline(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            font = current_widget.font()
            font.setUnderline(not font.underline())
            current_widget.setFont(font)

    def align_left(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.setAlignment(Qt.AlignLeft)

    def align_center(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.setAlignment(Qt.AlignCenter)

    def align_right(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.setAlignment(Qt.AlignRight)

    def undo(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.undo()

    def redo(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.redo()

    def copy(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.copy()

    def cut(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.cut()

    def paste(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            current_widget.paste()

    def find_text(self):
        text, ok = QInputDialog.getText(self, "查找", "请输入要查找的文本:")
        if ok and text:
            current_widget = self.tab_widget.currentWidget()
            if current_widget is not None:
                cursor = current_widget.textCursor()
                found = current_widget.find(text, cursor)

                if not found:
                    QMessageBox.information(self, "查找", "未找到该文本。")

    def replace_text(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("替换")
        layout = QVBoxLayout(dialog)

        layout.addWidget(QLabel("查找:"))
        find_input = QLineEdit(dialog)
        layout.addWidget(find_input)

        layout.addWidget(QLabel("替换为:"))
        replace_input = QLineEdit(dialog)
        layout.addWidget(replace_input)

        replace_button = QPushButton("替换", dialog)
        layout.addWidget(replace_button)

        replace_button.clicked.connect(lambda: self.perform_replace(find_input.text(), replace_input.text(), dialog))

        dialog.exec_()

    def perform_replace(self, find_text, replace_text, dialog):
        current_widget = self.tab_widget.currentWidget()
        if current_widget is not None:
            text = current_widget.toPlainText()
            new_text = text.replace(find_text, replace_text)
            current_widget.setPlainText(new_text)
            dialog.accept()

    def cascade_windows(self):
        pass  # 这里可以实现窗口层叠功能

    def tile_horizontal(self):
        pass  # 这里可以实现水平平铺功能

    def tile_vertical(self):
        pass  # 这里可以实现垂直平铺功能

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = SimpleMDIExample()
    mainWin.show()
    sys.exit(app.exec_())
