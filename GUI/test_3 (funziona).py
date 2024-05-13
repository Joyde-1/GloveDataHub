import sys
import subprocess
import ctypes
import psutil
from PyQt6 import QtWidgets, QtGui, QtCore
import pygetwindow as gw

# Costanti per i messaggi di Windows
WM_SYSCOMMAND = 0x0112
WM_NCLBUTTONDOWN = 0x00A1
SC_MOVE = 0xF010

# Definisci la funzione di callback per il filtro di messaggi
def window_proc(hwnd, msg, wparam, lparam):
    if msg == WM_SYSCOMMAND and (wparam == SC_MOVE or wparam == SC_MOVE + 1):
        return 0  # Ignora il comando di movimento
    if msg == WM_NCLBUTTONDOWN:
        return 0  # Ignora il click non-client (movimento)
    return ctypes.windll.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

# Converti la funzione di callback in un puntatore di funzione
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int)
window_proc_pointer = WNDPROC(window_proc)

class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.sensecom_process = None

    def initUI(self):
        self.setWindowTitle("GloveDataHub")
        self.setGeometry(100, 100, 1024, 768)

        # Crea un widget centrale e imposta il layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Sezione header
        header_layout = QtWidgets.QHBoxLayout()
        self.gdh_logo = QtWidgets.QLabel()
        self.gdh_logo.setPixmap(QtGui.QPixmap('GUI/images/logo_GloveDataHub_new.png'))
        self.kore_logo = QtWidgets.QLabel()
        self.kore_logo.setPixmap(QtGui.QPixmap('GUI/images/kore_Logo.png'))

        self.title_label = QtWidgets.QLabel("GloveDataHub")
        self.title_label.setFont(QtGui.QFont("Arial", 30, QtGui.QFont.Weight.Bold))

        header_layout.addWidget(self.gdh_logo)
        header_layout.addStretch()
        header_layout.addWidget(self.title_label)
        header_layout.addStretch()
        header_layout.addWidget(self.kore_logo)

        layout.addLayout(header_layout)

        # Sezione bottoni
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

        # Contenitore SenseCom
        self.sensecom_container = QtWidgets.QWidget()
        self.sensecom_container.setFixedSize(1200, 600)
        layout.addWidget(self.sensecom_container)

        # Imposta il colore di sfondo del widget principale
        central_widget.setStyleSheet("background-color: #E9E6DB;")

    def back_action(self):
        print("Back button pressed")

    def next_action(self):
        print("Next button pressed")

    def embed_sensecom(self):
        # Controlla se il processo SenseCom è già attivo
        sensecom_running = False
        for process in psutil.process_iter():
            if process.name() == "SenseCom.exe":
                sensecom_running = True
                break

        if sensecom_running:
            # Termina il processo SenseCom
            for process in psutil.process_iter():
                if process.name() == "SenseCom.exe":
                    process.terminate()
                    break

        # Avvia SenseCom application
        self.sensecom_process = subprocess.Popen("C:/Program Files/SenseCom/SenseCom.exe")

        # Delay per consentire a SenseCom di avviarsi
        QtCore.QTimer.singleShot(1000, self.embed_sensecom_window)

    def embed_sensecom_window(self):
        try:
            sensecom_hwnd = gw.getWindowsWithTitle("SenseCom")[0]
            sensecom_hwnd.restore()  # Restore the window if it's minimized or maximized
            sensecom_hwnd.moveTo(0, 0)  # Move the window to a specific position
            sensecom_hwnd.resize(400, 300)  # Resize the window to fit inside the GUI container

            container_hwnd = int(self.sensecom_container.winId())
            ctypes.windll.user32.SetParent(sensecom_hwnd._hWnd, container_hwnd)
           
            #Get the current style of the SenseCom window
            style = ctypes.windll.user32.GetWindowLongW(sensecom_hwnd._hWnd, -16)

            # Remove the system buttons from the window
            style &= ~0x00C00000  # Remove WS_CAPTION (title bar) and WS_BORDER (border)
            ctypes.windll.user32.SetWindowLongW(sensecom_hwnd._hWnd, -16, style)

            # Set the anchor to pin the SenseCom window to the main GUI window
            ex_style = ctypes.windll.user32.GetWindowLongW(sensecom_hwnd._hWnd, -20)
            ex_style |= 0x00000008  # Set WS_EX_CONTROLPARENT
            ctypes.windll.user32.SetWindowLongW(sensecom_hwnd._hWnd, -20, ex_style)    

        except IndexError:
            print("SenseCom window not found.")
            QtWidgets.QMessageBox.critical(self, "Error", "SenseCom window not found.")

    def closeEvent(self, event):
        if self.sensecom_process:
            self.sensecom_process.terminate()
        event.accept()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    manager = WindowManager()
    manager.show()
    sys.exit(app.exec())
