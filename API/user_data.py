import re
import random
import os

class UserData:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.code = ""
        self.path_directory = ""

    def set_name(self, name):
        if not re.match("^[A-Za-z]+$", name) and name != "":
            raise ValueError("Name must contain only letters. \n")
        self.name = name

    def set_surname(self, surname):
        if not re.match("^[A-Za-z]+$", surname) and surname != "":
            raise ValueError("Surname must contain only letters. \n")
        self.surname = surname
        
    def set_code(self, code):
        if not re.match("^[0-9]+$", code):
            raise ValueError("Code must contain only numbers. \n")
        if len(code) != 4:
            raise ValueError("Code must have a length of 4 numbers. \n")
        self.code = code

    def set_path_directory(self, path_directory):
        if not os.path.exists(path_directory):
            raise ValueError("Path does not exist. \n")
        self.path_directory = path_directory
            
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_path_directory(self):
        return self.path_directory

    def _calculate_name_csv(self):
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
        name_csv = self._calculate_name_csv()
        path_csv = os.path.join(self.path_directory, name_csv)
        normalized_path_csv = os.path.normpath(path_csv)
        
        return normalized_path_csv
    
    def generate_random_code(self, length=4):
        random_code = ""
        random_code = ''.join(str(random.randint(0, 9)) for _ in range(length))
        
        return random_code
