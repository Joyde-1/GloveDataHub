from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont
import sys
import os
import ctypes
import psutil
import pygetwindow as gw

# Aggiungi il percorso della directory 'API' al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))

from exe_manager import ExeManager

class WindowManager(QtWidgets.QMainWindow):

    def __init__(self, ghd_logo_path, kore_logo_path, window_title, window_width, window_height, background, frontground, header_title, header_font):
        super().__init__()
        
        self.ghd_logo_path = ghd_logo_path
        self.kore_logo_path = kore_logo_path
        self.window_title = window_title
        self.window_width = window_width
        self.window_height = window_height
        self.background = background
        self.frontground = frontground
        self.header_title = header_title
        self.header_font = header_font

        self.exe_manager = ExeManager()
        
        self._init_window()

    def _init_window(self):
        self._create_window()
        self._set_window_header()
        self._center_window()  # Centra la finestra sullo schermo

    def _create_window(self):
        self.setWindowTitle(self.window_title)
        self.setFixedSize(self.window_width, self.window_height)
        self.setStyleSheet(f"background-color: {self.background};")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QtWidgets.QVBoxLayout(central_widget)

    def _set_window_header(self):
        header_layout = QtWidgets.QHBoxLayout()

        # Carica le immagini dei loghi
        gdh_image = QtGui.QPixmap(self.ghd_logo_path)
        kore_image = QtGui.QPixmap(self.kore_logo_path)

        # Crea i label per le immagini
        self.gdh_logo = QtWidgets.QLabel()
        self.gdh_logo.setPixmap(gdh_image)

        self.kore_logo = QtWidgets.QLabel()
        self.kore_logo.setPixmap(kore_image)

        # Crea il titolo dell'applicazione
        self.title_label = QtWidgets.QLabel(self.header_title)
        self.title_label.setFont(self.header_font)
        self.title_label.setStyleSheet(f"color: {self.frontground};")

        # Aggiungi i loghi e il titolo all'header layout
        header_layout.addWidget(self.gdh_logo)
        header_layout.addStretch()
        header_layout.addWidget(self.title_label)        
        header_layout.addStretch()
        header_layout.addWidget(self.kore_logo)
        header_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignTop)

        # Imposta il margine e padding per posizionare correttamente gli elementi
        header_layout.setContentsMargins(10, 10, 10, 10)

        # Aggiungi l'header layout alla parte superiore del layout principale
        self.layout.addLayout(header_layout)

    def _center_window(self):
        # Ottieni le dimensioni dello schermo
        screen_geometry = QtGui.QGuiApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calcola la posizione x e y per centrare la finestra
        x = (screen_width - self.width()) // 2
        y = (screen_height - self.height()) // 2

        # Imposta la posizione della finestra
        self.move(x, y)

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
                
        self.sensecom_process = self.exe_manager.run_sensecom()
        QtCore.QTimer.singleShot(1000, self._embed_sensecom_window)

    def _embed_sensecom_window(self):
        try:
            sensecom_hwnd = gw.getWindowsWithTitle("SenseCom")[0]
            sensecom_hwnd.restore()  # Restore the window if it's minimized or maximized
            sensecom_hwnd.moveTo(0, 0)  # Move the window to a specific position
            sensecom_hwnd.resize(400, 300)  # Resize the window to fit inside the GUI container

            container_hwnd = int(self.sensecom_container.winId())
            ctypes.windll.user32.SetParent(sensecom_hwnd._hWnd, container_hwnd)
           
            # Get the current style of the SenseCom window
            style = ctypes.windll.user32.GetWindowLongW(sensecom_hwnd._hWnd, -16)
            
            # Remove the system buttons from the window
            style &= ~0x00C00000  # Remove WS_CAPTION (title bar) and WS_BORDER (border)
            ctypes.windll.user32.SetWindowLongW(sensecom_hwnd._hWnd, -16, style)

             # Set the anchor to pin the SenseCom window to the main GUI window
            ex_style = ctypes.windll.user32.GetWindowLongW(sensecom_hwnd._hWnd, -20)
            ex_style |= 0x00000008  # Set WS_EX_CONTROLPARENT
            ctypes.windll.user32.SetWindowLongW(sensecom_hwnd._hWnd, -20, ex_style)    

        except IndexError:
            QtWidgets.QMessageBox.critical(self, "Error", "SenseCom window not found.")

    def closeEvent(self, event):
        if self.sensecom_process:
            self.sensecom_process.terminate()
        event.accept()