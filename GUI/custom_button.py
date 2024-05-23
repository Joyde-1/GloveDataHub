from PyQt6 import QtWidgets, QtGui, QtCore

class CustomButton(QtWidgets.QPushButton):
    def __init__(self, title, width, height, font_size, parent=None):
        super().__init__(title, parent)
        self.setFont(QtGui.QFont("Arial", font_size))
        self.setStyleSheet(self.normal_style())
        # Imposta le dimensioni del pulsante
        self.setFixedSize(width, height)
        self.setMouseTracking(True)  # Enables mouse tracking

    def normal_style(self):
        return """
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                  stop:0 #E9E6DB, stop:1 #C8C5B8);
                color: black;
                border: 2px solid #C8C5B8;
                border-radius: 15px;
                padding: 0px 0px;
            }
        """

    def hover_style(self):
        return """
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                  stop:0 #C8C5B8, stop:1 #A9A69B);
                border-color: #A9A69B;
                color: black;
                border: 2px solid #A9A69B;
                border-radius: 15px;
                padding: 0px 0px;
            }
        """

    def pressed_style(self):
        return """
            QPushButton {
                background-color: #A9A69B;
                border-color: #8B887E;
                color: black;
                border: 2px solid #8B887E;
                border-radius: 15px;
                padding: 0px 0px;
            }
        """

    def enterEvent(self, event):
        self.setStyleSheet(self.hover_style())
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet(self.normal_style())
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        self.setStyleSheet(self.pressed_style())
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setStyleSheet(self.hover_style() if self.underMouse() else self.normal_style())
        super().mouseReleaseEvent(event)

    def action_next(self):
        print("Next button pressed")

    def action_cancel(self):
        print("Cancel button pressed")
        self.close()  # Example of closing the application
