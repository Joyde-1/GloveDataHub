import re
import csv
import os

class UserData:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.path_directory = ""

    def set_name(self, name):
        if not re.match("^[A-Za-z0-9]+$", name):
            raise ValueError("Name must contain only letters and numbers.")
        self.name = name

    def set_surname(self, surname):
        if not re.match("^[A-Za-z0-9]+$", surname):
            raise ValueError("Surname must contain only letters and numbers.")
        self.surname = surname

    def set_path_directory(self, path_directory):
        self.path_directory = path_directory

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_path_directory(self):
        return self.path_directory

    def _calculate_name_csv(self):
        return f"{self.name}_{self.surname}.csv"

    def create_path_csv(self):
        name_csv = self._calculate_name_csv()
        path_csv = os.path.join(self.path_directory, name_csv)
        
        return path_csv
