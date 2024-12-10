import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import random


class DrawCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.circles = []

    def run(self):
        d = random.randint(1, 100)
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        self.circles.append((x, y, d))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        for (x, y, d) in self.circles:
            painter.drawEllipse(x, y, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawCircles()
    ex.show()
    sys.exit(app.exec())