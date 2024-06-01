#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QFont


class CustomButton(QPushButton):
    """
    CustomButton class inherits from QPushButton and implements a button widget with dynamic styles for different states.
    """
    
    def __init__(self, title, width, height, font_size, parent=None):
        """
        Constructor method to initialize the CustomButton.

        Parameters
        ----------
        title : str 
            The title text of the button.
        width : int 
            The width of the button.
        height : int 
            The height of the button.
        font_size : int 
            The font size of the button text.
        parent : QWidget
            It is an optional param for the parent widget.
        """
        
        super().__init__(title, parent)

        # Set font type and dimensions 
        self.setFont(QFont("Montserrat", font_size))
        self.setStyleSheet(self.normal_style())

        # Set the button dimensions 
        self.setFixedSize(width, height)

        # Enables mouse tracking
        self.setMouseTracking(True)  

    def normal_style(self):
        """
        Defines the CSS style for the normal state of the button.

        Returns
        -------
        str
            CSS style for the normal state.
        """

        return """
            QPushButton {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                                stop:0 #F5FBFF, stop:1 #B0BCC4);
                color: #023E58;
                border: 2px solid #A1ABB3;
                border-radius: 15px;
                padding: 0px;
            }
        """

    def hover_style(self):
        """
        Defines the CSS style for the hover state of the button.

        Returns
        -------
        str 
            CSS style for the hover state.
        """
        
        return """
            QPushButton {
                background-color: #B6C7D1;
                color: #023E58;
                border: 2px solid #747B82;
                border-radius: 15px;
                padding: 5px 10px;
            }
        """

    def pressed_style(self):
        """
        Defines the CSS style for the pressed state of the button.

        Returns
        -------
        str
            CSS style for the pressed state.
        """
        
        return """
            QPushButton {
                background-color: #9EACB5;
                color: #023E58;
                border: 2px solid #606C78;
                border-radius: 15px;
                padding: 5px 10px;
            }
        """

    def enterEvent(self, event):
        """
        Event handler for when the mouse enters the button.
        """

        # Set the hover style when the mouse enters
        self.setStyleSheet(self.hover_style())
        super().enterEvent(event)

    def leaveEvent(self, event):
        """
        Event handler for when the mouse leaves the button.
        """
        
        # Set the normal style when the mouse leaves
        self.setStyleSheet(self.normal_style())
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        """
        Event handler for mouse press event.
        """

        # Set the pressed style when the button is pressed
        self.setStyleSheet(self.pressed_style())
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        """
        Event handler for mouse release event.
        """

        # Set the hover or normal style based on the mouse position
        self.setStyleSheet(self.hover_style() if self.underMouse() else self.normal_style())
        super().mouseReleaseEvent(event)

    def action_next(self):
        """
        Action performed when the button is clicked.
        """

        # Print a message indicating the next button was pressed
        print("Next button pressed")

    def action_cancel(self):
        """
        Action performed when the button is clicked.
        """

        # Print a message indicating the cancel button was pressed and close the button
        print("Cancel button pressed")
        self.close() 