#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



from PyQt6.QtWidgets import QMessageBox


class MessageManager:
    """
    MessageManager class manages the style of message box to show when an error or information occured.
    
    Attributes
    ----------
    title: str (istance attribute)
        Title of message box.
    message: str (istance attribute)
        Message to show.
    dialog : QMessageBox (istance attribute)
        The output dialog for the message to show.
    """
    
    def __init__(self, title, message):
        """
        Constructor, initializes the elements of a message box.
        
        Parameters
        ----------
        title: str
            Title of message box.
        message: str
            Message to show.
        """
        
        self.title = title
        self.message = message
        
    def show_message_box(self):
        """
        Shows a message with an output dialog.
        """
        
        # Set the message box
        if self.title == "Error":
            self.dialog = QMessageBox(QMessageBox.Icon.Critical, self.title, self.message)
        else:
            self.dialog = QMessageBox(QMessageBox.Icon.Information, self.title, self.message)
        
        # Set the style for the output dialog
        self._set_output_dialog_style()
        
        # Show the output dialog
        self.dialog.exec()
        
    def _set_output_dialog_style(self):
        """
        Sets the style for the output dialog.
        """
        
        if self.dialog:
            self.dialog.setStyleSheet("""
                QMessageBox {
                    color: #023E58;
                    background-color: #CFDCE6;
                }
                QLabel {
                    color: #023E58;
                    font: ("Merriweather", 16);
                }
                QPushButton {
                    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #F5FBFF, stop:1 #B0BCC4);
                    color: #023E58;
                    border: 2px solid #A1ABB3;
                    border-radius: 15px;
                    padding: 5px 7px;
                    min-width: 30px;
                }
                QPushButton:hover {
                    background-color: #B6C7D1;
                    color: #023E58;
                    border: 2px solid #747B82;
                    border-radius: 15px;
                    padding: 5px 7px;
                }
                QPushButton:pressed {
                    background-color: #9EACB5;
                    color: #023E58;
                    border: 2px solid #606C78;
                    border-radius: 15px;
                    padding: 5px 7px;
                }
            """)