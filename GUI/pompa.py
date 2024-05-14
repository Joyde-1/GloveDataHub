from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class WindowManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("GloveDataHub")
        self.setFixedSize(800, 600)

        # Setup central widget and layout
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QtWidgets.QVBoxLayout(central_widget)

        # Permanent top area for SenseCom
        self.setup_sensecom_area(main_layout)

        # Dynamic content area
        self.content_area = QtWidgets.QStackedWidget()
        main_layout.addWidget(self.content_area)

    def setup_sensecom_area(self, layout):
        # Container for SenseCom and the Start button
        sensecom_layout = QtWidgets.QVBoxLayout()

        # SenseCom display (just a placeholder here)
        self.sensecom_display = QtWidgets.QLabel("SenseCom UI Placeholder")
        self.sensecom_display.setFixedSize(512, 250)
        self.sensecom_display.setStyleSheet("background-color: white; border: 1px solid black;")
        sensecom_layout.addWidget(self.sensecom_display)

        # Start SenseCom button
        self.start_sensecom_button = QtWidgets.QPushButton("Start SenseCom")
        sensecom_layout.addWidget(self.start_sensecom_button)

        # Add to the main layout
        layout.addLayout(sensecom_layout)

    def change_content(self, widget):
        """Switch the displayed widget in the content area."""
        self.content_area.setCurrentWidget(widget)

    def add_content(self, widget):
        """Add a widget to the stack in the content area."""
        self.content_area.addWidget(widget)

# Example usage
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window_manager = WindowManager()
    # Example widgets that could be swapped in and out
    calibration_screen = QtWidgets.QLabel("Calibration Screen")
    data_entry_screen = QtWidgets.QLabel("Data Entry Screen")
    window_manager.add_content(calibration_screen)
    window_manager.add_content(data_entry_screen)
    window_manager.change_content(calibration_screen)
    window_manager.show()
    sys.exit(app.exec())
