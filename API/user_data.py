#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



import re
import random
import os


class UserData:
    """
    A class to represent user data and operations on it.
    
    Attributes
    ----------
    first name : str (istance attribute)
        The first name of the user.
    last_name : str (istance attribute)
        The last name of the user.
    code : str (istance attribute)
        The code of the user.
    path_directory : str (istance attribute)
        The directory path for user's CSV files.
    """

    def __init__(self):
        """
        Constructor, initialize UserData object.
        """
        
        self.first_name = ""
        self.last_name = ""
        self.code = ""
        self.path_directory = ""

    def set_first_name(self, first_name):
        """
        Sets the first name of the user.
        
        Parameters
        ----------
        first_name : str 
            The first name of the user.
    
        Raises
        ------
        ValueError 
            If first_name contains non-letter characters or is empty.
        """
        
        # Check if the first name contains non-letter characters or is empty
        if not re.match("^[A-Za-z]+$", first_name) and first_name != "":
            raise ValueError('<b><span style="color: #025885;">First Name</span></b> must contain only letters. <br>')
        self.first_name = first_name

    def set_last_name(self, last_name):
        """
        Sets the last name of the user.
        
        Parameters
        ----------
        last_name : str 
            The last name of the user.
    
        Raises
        ------
        ValueError 
            If last name contains non-letter characters or is empty.
        """
        
        # Check if the last name contains non-letter characters or is empty
        if not re.match("^[A-Za-z]+$", last_name) and last_name != "":
            raise ValueError('<b><span style="color: #025885;">Last Name</span></b> must contain only letters. <br>')
        self.last_name = last_name
        
    def set_code(self, code):
        """
        Sets the user code.
        
        Parameters
        ----------
        code : str 
            The the user code.
    
        Raises
        -----
        ValueError 
            If code contains non-numeric characters or is not 4 digits long.
        """
        
        # Check if the code is black, with character different from numbers and with a length of 4 numbers
        if not re.match("^[0-9]+$", code) and code != "":
            raise ValueError('<b><span style="color: #025885;">Code</span></b> must contain only numbers. <br>')
        if len(code) != 4 and code != "":
            raise ValueError('<b><span style="color: #025885;">Code</span></b> must have a length of 4 numbers. <br>')
        self.code = code

    def set_path_directory(self, path_directory):
        """
        Sets the directory path for user's CSV files.
        
        Parameters
        ----------
        path_directory : str 
            The directory path for user's CSV files.
        
        Raises
        -----
        ValueError
            If the specified directory path does not exist.
        """
        
        # Check if the directory exist in the file system
        if not os.path.exists(path_directory):
            raise ValueError('<b><span style="color: #025885;">Path</span></b> does not exist. <br>')
        self.path_directory = path_directory
            
    def get_first_name(self):
        """
        Returns the first name of the user.
        
        Returns
        -------
        str
            The first name of the user.
        """
        
        return self.first_name

    def get_last_name(self):
        """
        Returns the last name of the user.
        
        Returns
        -------
        str
            The last name of the user.
        """
        
        return self.last_name

    def get_path_directory(self):
        """
        Returns the directory path for user's CSV files.
        
        Returns
        -------
        str
            The directory path for user's CSV files.
        """
        
        return self.path_directory

    def _calculate_name_csv(self):
        """
        Calculates the name of the user's CSV file based on first name, last name, and code.
        
        Returns
        -------
        str
            The name of the user's CSV file.
        """
        
        # Checks the user fields to calculate the correct file .CSV name
        if self.first_name == "" and self.last_name == "":
            return f"{self.code}.csv"
        elif self.first_name == "" and self.code == "":
            return f"{self.last_name}.csv"
        elif self.last_name == "" and self.code == "":
            return f"{self.first_name}.csv"
        elif self.first_name == "":
            return f"{self.last_name}_{self.code}.csv"
        elif self.last_name == "":
            return f"{self.first_name}_{self.code}.csv"
        elif self.code == "":
            return f"{self.first_name}_{self.last_name}.csv"
        else:
            return f"{self.first_name}_{self.last_name}_{self.code}.csv"

    def create_path_csv(self):
        """
        Creates the full path of the user's CSV file based on the destination directory and calculated CSV file name.
        
        Returns
        -------
        str 
            The normalized full path of the user's CSV file.
        """
        
        name_csv = self._calculate_name_csv()
        
        # Joint the directory selected to save the .CSV file and the name for the .CSV file
        path_csv = os.path.join(self.path_directory, name_csv)
        normalized_path_csv = os.path.normpath(path_csv)
        
        return normalized_path_csv
    
    def generate_random_code(self, length=4):
        """
        Generates a random code of specified length.
        
        Attributes
        ----------
        length : int
            The length of the random code, it is an optional parama and by defaults is set to 4.
        
        Returns
        -------
        str 
            The randomly generated code.
        """
        
        random_code = ""
        
        # Generate 4 integer numbers from 0 to 9
        random_code = ''.join(str(random.randint(0, 9)) for _ in range(length))
        
        return random_code