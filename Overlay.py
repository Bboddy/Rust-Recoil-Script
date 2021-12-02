import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Crosshair(QtWidgets.QWidget):
    def __init__(self, parent=None, windowSize=24, penWidth=2, w=" AK"):
        QtWidgets.QWidget.__init__(self, parent)
        self.weapon = w
        self.ws = windowSize
        self.resize(24+1, 50+1)
        self.pen = QtGui.QPen(QtGui.QColor(231, 60, 126, 255))
        self.pen.setWidth(penWidth)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowTransparentForInput)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.move(QtWidgets.QApplication.desktop().screen().rect().center() - self.rect().center() + QtCore.QPoint(1,1))
        self.setWindowFlag(QtCore.Qt.Tool)
        self.setWindowTitle("Easy4.me")

    def paintEvent(self, event):
        ws = self.ws
        d = 5
        painter = QtGui.QPainter(self)
        painter.setPen(self.pen)
        painter.drawLine(int(ws/2), 0 + 13, int(ws/2), int(ws/2) - int(ws/d) + 13) # Top
        painter.drawLine(int(ws/2), int(ws/2) + int(ws/d) + 13, int(ws/2), int(ws) + 13) # Bottom
        painter.drawLine(0, int(ws/2) + 13, int(ws/2) - int(ws/d), int(ws/2) + 13) # Left
        painter.drawLine(int(ws/2) + int(ws/d), int(ws/2) + 13, int(ws), int(ws/2) + 13) # Right

        wep = painter.drawText(3,50, self.weapon)

def draw(weapon):
    global overlay
    app1 = QtWidgets.QApplication(sys.argv)

    overlay = Crosshair(windowSize=24, penWidth=1, w=weapon)
    overlay.show()

    app1.exec_()