import sys
import subprocess
import ctypes
from PyQt5 import QtWidgets, QtGui, QtCore

class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sensecom_process = None
        self.sensecom_hwnd = None

    def initUI(self):
        self.setWindowTitle("GloveDataHub")
        self.setGeometry(100, 100, 1024, 768)

        # Create a central widget and set layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Header section
        header_layout = QtWidgets.QHBoxLayout()
        self.gdh_logo = QtWidgets.QLabel()
        self.gdh_logo.setPixmap(QtGui.QPixmap('GUI/images/logo_GloveDataHub_new.png').scaled(50, 50, QtCore.Qt.KeepAspectRatio))
        self.kore_logo = QtWidgets.QLabel()
        self.kore_logo.setPixmap(QtGui.QPixmap('GUI/images/kore_Logo.png').scaled(50, 50, QtCore.Qt.KeepAspectRatio))
        
        self.title_label = QtWidgets.QLabel("GloveDataHub Application")
        self.title_label.setFont(QtGui.QFont("Arial", 20))

        header_layout.addWidget(self.gdh_logo)
        header_layout.addStretch()
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.kore_logo)

        layout.addLayout(header_layout)

        # Buttons section
        buttons_layout = QtWidgets.QHBoxLayout()
        back_button = QtWidgets.QPushButton("Back")
        back_button.clicked.connect(self.back_action)
        next_button = QtWidgets.QPushButton("Next")
        next_button.clicked.connect(self.next_action)
        start_button = QtWidgets.QPushButton("Start SenseCom")
        start_button.clicked.connect(self.embed_sensecom)

        buttons_layout.addWidget(back_button)
        buttons_layout.addWidget(start_button)
        buttons_layout.addWidget(next_button)

        layout.addLayout(buttons_layout)

        # SenseCom container
        self.sensecom_container = QtWidgets.QWidget()
        self.sensecom_container.setFixedSize(800, 600)
        layout.addWidget(self.sensecom_container)

    def back_action(self):
        print("Back button pressed")

    def next_action(self):
        print("Next button pressed")

    def embed_sensecom(self):
        # Start SenseCom application
        self.sensecom_process = subprocess.Popen("C:/Program Files/SenseCom/SenseCom.exe")  # Replace with your executable path

        # Delay to allow SenseCom to start
        QtCore.QTimer.singleShot(2000, self.embed_sensecom_window)

    def embed_sensecom_window(self):
        self.sensecom_hwnd = ctypes.windll.user32.FindWindowW(None, "SenseCom 1.2.0")  # Replace with the actual window title
        if self.sensecom_hwnd == 0:
            print("Error: SenseCom window not found.")
            return

        # Embed SenseCom window into the container
        container_hwnd = int(self.sensecom_container.winId())
        ctypes.windll.user32.SetParent(self.sensecom_hwnd, container_hwnd)

        # Update window styles to fix and disable moving/resizing
        style = ctypes.windll.user32.GetWindowLongW(self.sensecom_hwnd, -16)
        style = style & ~0x40000000  # Remove WS_CHILD
        style = style & ~0x00040000  # Remove WS_SIZEBOX to prevent resizing
        style = style & ~0x00020000  # Remove WS_MINIMIZEBOX to prevent minimizing
        style = style & ~0x00010000  # Remove WS_MAXIMIZEBOX to prevent maximizing
        style = style & ~0x00080000  # Remove WS_CAPTION to remove title bar
        ctypes.windll.user32.SetWindowLongW(self.sensecom_hwnd, -16, style)

        # Resize and move the window
        ctypes.windll.user32.SetWindowPos(self.sensecom_hwnd, None, 0, 0, self.sensecom_container.width(), self.sensecom_container.height(), 0x0040)

        # Start monitoring the position
        self.monitor_position()

    def monitor_position(self):
        if self.sensecom_hwnd:
            # Ensure the window stays at the fixed position
            ctypes.windll.user32.SetWindowPos(self.sensecom_hwnd, None, 0, 0, self.sensecom_container.width(), self.sensecom_container.height(), 0x0040)
            # Call this function again after 100 milliseconds
            QtCore.QTimer.singleShot(100, self.monitor_position)

    def closeEvent(self, event):
        if self.sensecom_process:
            self.sensecom_process.terminate()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    manager = WindowManager()
    manager.show()
    sys.exit(app.exec_())
