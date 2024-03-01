import sys

import cv2
import numpy as np
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QFileDialog,
    QWidget,
    QLabel,
    QVBoxLayout,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QGuiApplication


class MyMainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()

        # メニューバーに「ファイル」を追加
        file_menu = menubar.addMenu("ファイル")

        open_action = file_menu.addAction("開く")
        open_action.triggered.connect(self.open_image)

        quit_action = file_menu.addAction("ログアウト")
        quit_action.triggered.connect(self.logout_app)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.contrast_label = QLabel("Contrast Score: ", self)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.contrast_label)

        self.setGeometry(0, 0, 300, 200)
        self.setWindowTitle("メニューバーの例")
        self.center_window()
        self.show()

    def calculate_contrast_score(self, image_path):
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        contrast_score = np.std(binary_image)
        return contrast_score
    
    def center_window(self):
        # アプリケーションのプライマリスクリーンを取得
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # ウィンドウの中心座標を計算
        window_rect = self.frameGeometry()
        window_rect.moveCenter(screen_geometry.center())

        # ウィンドウを中央に配置
        self.move(window_rect.topLeft())

    def logout_app(self):
        self.app.quit()

    def open_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            contrast_score = self.calculate_contrast_score(file_path)
            self.contrast_label.setText(f"Contrast Score: {contrast_score}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MyMainWindow(app)
    sys.exit(app.exec_())
