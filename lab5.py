import sys
from PySide6.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QBrush, QPen, QPainterPath

class CustomRectItem(QGraphicsRectItem):
    def __init__(self, color, width, height, corner_radius=0, parent=None):
        super().__init__(parent)
        self.color = color
        self.width = width
        self.height = height
        self.corner_radius = corner_radius

    def paint(self, painter, option, widget):
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(Qt.NoPen))

        if self.corner_radius > 0:
            path = QPainterPath()
            path.addRoundedRect(0, 0, self.width, self.height, self.corner_radius, self.corner_radius)
            painter.drawPath(path)
        else:
            painter.drawRect(0, 0, self.width, self.height)

class CustomScene(QGraphicsScene):
    def __init__(self, colors, positions, rotations, corner_radius=None, parent=None):
        super().__init__(parent)
        self.colors = colors
        self.positions = positions
        self.rotations = rotations
        self.corner_radius = corner_radius if corner_radius else [0] * len(colors)

        self.setupScene()

    def setupScene(self):
        for color, pos, rotation, radius in zip(self.colors, self.positions, self.rotations, self.corner_radius):
            rect = CustomRectItem(color, 200, 200, radius)
            rect.setPos(*pos)
            rect.setRotation(rotation)
            self.addItem(rect)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    colors = [
        QColor(136, 0, 0),   # Top-left
        QColor(255, 0, 0),   # Top-right
        QColor(0, 255, 0),   # Bottom-left
        QColor(0, 136, 0),   # Bottom-right
        QColor(65, 105, 225)  # Center
    ]

    positions = [
        (0, 0),           # Top-left
        (320, 0),         # Top-right
        (0, 240),         # Bottom-left
        (320, 240),       # Bottom-right
        (120, 220)        # Center
    ]

    rotations = [0, 0, 0, 0, -45]
    corner_radius = [0, 0, 0, 0, 20]  # Радіус заокруглення

    scene = CustomScene(colors, positions, rotations, corner_radius)
    view = QGraphicsView(scene)
    view.resize(900, 900)  # Розмір вікна
    view.show()

    sys.exit(app.exec())
