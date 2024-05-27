import re
import random
import os

class UserData:
    """A class to represent user data and operations on it."""

    def __init__(self):
        """
        Constructor, initialize UserData object.

        Attributes
        ----------
        name : str 
            The name of the user.
        surname : str 
            The surname of the user.
        code : str 
            The code of the user.
        path_directory : str 
            The directory path for user's CSV files.
        """
        self.name = ""
        self.surname = ""
        self.code = ""
        self.path_directory = ""

    def set_name(self, name):
        """
        Sets the name of the user.
        
        Parameters
        ----------
        name : str 
            The name of the user.
    
        Raises
        ------
        ValueError 
            If name contains non-letter characters or is empty.
        """
        if not re.match("^[A-Za-z]+$", name) and name != "":
            raise ValueError("<b>Name</b> must contain only letters. <br>")
        self.name = name

    def set_surname(self, surname):
        """
        Sets the surname of the user.
        
        Parameters
        ----------
        surname : str 
            The surname of the user.
    
        Raises
        ------
        ValueError 
            If surname contains non-letter characters or is empty.
        """
        if not re.match("^[A-Za-z]+$", surname) and surname != "":
            raise ValueError("<b>Surname</b> must contain only letters. <br>")
        self.surname = surname
        
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
        if not re.match("^[0-9]+$", code):
            raise ValueError("<b>Code</b> must contain only numbers. <br>")
        if len(code) != 4:
            raise ValueError("<b>Code</b> must have a length of 4 numbers. <br>")
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
        if not os.path.exists(path_directory):
            raise ValueError("<b>Path</b> does not exist. \n")
        self.path_directory = path_directory
            
    def get_name(self):
        """
        Returns the name of the user.
        
        Returns
        -------
        str
            The name of the user.
        """
        return self.name

    def get_surname(self):
        """
        Returns the surname of the user.
        
        Returns
        -------
        str
            The surname of the user.
        """
        return self.surname

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
        Calculates the name of the user's CSV file based on name, surname, and code.
        
        Returns
        -------
        str
            The name of the user's CSV file.
        """
        if self.name == "" and self.surname == "":
            return f"{self.code}.csv"
        elif self.name == "" and self.code == "":
            return f"{self.surname}.csv"
        elif self.surname == "" and self.code == "":
            return f"{self.name}.csv"
        elif self.name == "":
            return f"{self.surname}_{self.code}.csv"
        elif self.surname == "":
            return f"{self.name}_{self.code}.csv"
        elif self.code == "":
            return f"{self.name}_{self.surname}.csv"
        else:
            return f"{self.name}_{self.surname}_{self.code}.csv"

    def create_path_csv(self):
        """
        Creates the full path of the user's CSV file based on the destination directory and calculated CSV file name.
        
        Returns
        -------
        str 
            The normalized full path of the user's CSV file.
        """
        name_csv = self._calculate_name_csv()
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
        random_code = ''.join(str(random.randint(0, 9)) for _ in range(length))
        
        return random_code
