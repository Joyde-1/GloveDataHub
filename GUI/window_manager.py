from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtGui import QFont
import sys
import os
import ctypes
import psutil
import pygetwindow as gw
from custom_button import CustomButton

# Aggiungi il percorso della directory 'API' al PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'API'))

from exe_manager import ExeManager

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
        self.main_layout = QtWidgets.QVBoxLayout(central_widget)

    def _set_window_header(self):
        header_layout = QtWidgets.QHBoxLayout()

        # Carica le immagini dei loghi
        gdh_image = QtGui.QPixmap(self.ghd_logo_path)
        kore_image = QtGui.QPixmap(self.kore_logo_path)
        
        # Ridimensiona le immagini a 100x100 pixel
        gdh_image = gdh_image.scaled(100, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        kore_image = kore_image.scaled(80, 80, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)

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
        header_layout.setContentsMargins(5, 5, 5, 5)
        
        # Aggiungi l'header layout alla parte superiore del layout principale
        self.main_layout.addLayout(header_layout)

        # Aggiungi un layout per il contenuto dinamico
        self.content_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.content_layout)
    
    def _center_window(self):
        # Ottieni le dimensioni dello schermo
        screen_geometry = QtGui.QGuiApplication.primaryScreen().geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # Calcola la larghezza e l'altezza della finestra
        window_width = self.width()
        window_height = self.height()

        # Definisci la distanza desiderata dai bordi
        margin_horizontal = 50  # Modifica questa variabile per regolare la distanza dai bordi
        margin_vertical = 50  # Modifica questa variabile per regolare la distanza dai bordi

        # Calcola le posizioni x e y per centrare la finestra orizzontalmente e verticalmente
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Calcola la distanza verticale dai bordi
        distance_top = y
        distance_bottom = screen_height - y - window_height

        # Calcola l'offset verticale aggiuntivo per compensare la differenza tra distanza superiore e inferiore
        additional_offset = (distance_bottom - distance_top) // 2  # Aumenta il divisore per sollevare ulteriormente la finestra

        # Aggiusta l'offset verticale
        y -= additional_offset + 50  # Modifica il valore di 50 per regolare ulteriormente il sollevamento

        # Assicurati che la finestra non esca fuori dallo schermo
        x = max(margin_horizontal, min(x, screen_width - window_width - margin_horizontal))
        y = max(margin_vertical, min(y, screen_height - window_height - margin_vertical))

        # Imposta la posizione della finestra
        self.move(x, y)
        
    def create_dynamic_content_layout(self):
        self.dynamic_content_box = QtWidgets.QHBoxLayout()
        self.content_layout.addLayout(self.dynamic_content_box)
        
        # Left widget for dynamic content
        self.dynamic_content_widget = QtWidgets.QVBoxLayout()
        # self.dynamic_content_widget.setFixedSize(500, 250)
        self.dynamic_content_widget.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.dynamic_content_box.addLayout(self.dynamic_content_widget)
        
    def add_dynamic_content(self, widget):
        """Add or switch dynamic content in the left widget."""
        self.dynamic_content_widget.addWidget(widget)
        self.dynamic_content_widget.addStretch()
        # self.dynamic_content_widget.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
        # self.dynamic_content_widget.setCurrentWidget(widget)
        
    def create_sensecom_layout(self):
        # Contenitore SenseCom
        self.sensecom_container = QtWidgets.QStackedWidget()
        self.sensecom_container.setFixedSize(512, 250)
        
        # Bottone per avviare SenseCom
        sensecom_button = CustomButton("Start SenseCom")
        sensecom_button.clicked.connect(self._embed_sensecom)
        button_layout = QtWidgets.QVBoxLayout()
        # button_layout.addStretch()
        button_layout.addWidget(sensecom_button)
                
        # Aggiungi un layout per sensecom
        self.sensecom_layout = QtWidgets.QVBoxLayout()
        
        self.sensecom_layout.addWidget(self.sensecom_container)
        self.sensecom_layout.addStretch()
        self.sensecom_layout.addLayout(button_layout)
        self.sensecom_layout.addStretch()
        self.sensecom_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignRight)

        self.dynamic_content_box.addLayout(self.sensecom_layout)
        # Aggiungi un layout per il contenuto dinamico
        # self.content_panel = QtWidgets.QStackedWidget()
        # self.content_layout.addWidget(self.content_panel)

    def _embed_sensecom(self):
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
            #sensecom_hwnd.resize(300, 200)  # Resize the window to fit inside the GUI container

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
        if hasattr(self, 'sensecom_process') and self.sensecom_process:
            self.sensecom_process.terminate()
        event.accept()
        
    """ def clear_content_layout(self):
        # Ciclo per rimuovere tutti i widget da un layout
        while self.main_layout.content_layout.count():
            item = self.main_layout.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clear_content_layout() """
                
    # Metodo per ripulire il content_layout
    def clear_content_layout(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout() is not None:
                # Se l'item è un layout, puliscilo ricorsivamente
                self._clear_layout(item.layout())

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            elif item.layout() is not None:
                self._clear_layout(item.layout())
