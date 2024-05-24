import subprocess

class ExeManager:
    """
    Class to manage execution of external scripts and processes.

    Attributes
    ----------
    path_script : str 
        The path to the script for data acquisition.
    path_sensecom : str 
        The path to the SenseCom executable.
    sensecom_process : subprocess.Popen 
        The process for SenseCom.
    script_process : subprocess.Popen 
        The process for the data acquisition script.
    """
    def __init__(self):
        """
        Constructor, initialize ExeManager with default paths and None for processes.
        """
        self.path_script = "Data-Acquisition/glove_data_acquisition.exe"
        self.path_sensecom = "C:/Program Files/SenseCom/SenseCom.exe"
        self.sensecom_process = None
        self.script_process = None

    def start_sensecom(self):
        """
        Start the SenseCom process.
        """
        self.sensecom_process = subprocess.Popen([self.path_sensecom], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    def start_script(self, path_to_csv, total_time):
        """
        Start the data acquisition script process.

        Parameters
        ----------
        path_to_csv : str 
            The path to the CSV file for data storage.
        total_time : int 
            The total time for data acquisition in seconds.
        """
        self.script_process = subprocess.Popen([self.path_script, path_to_csv, str(total_time)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    def is_sensecom_running(self):
        """
        Check if the SenseCom process is running.

        Returns
        -------
        bool
            True if SenseCom process is running, False otherwise.
        """
        if self.sensecom_process is None:
            return False
        return self.sensecom_process.poll() is None

    def is_script_running(self):
        """
        Check if the data acquisition script process is running.

        Returns
        -------
        bool 
            True if data acquisition script process is running, False otherwise.
        """
        if self.script_process is None:
            return False
        return self.script_process.poll() is None

    def close_sensecom(self):
        """
        Close the SenseCom process if it is running.
        """
        if self.is_sensecom_running():
            self.sensecom_process.terminate()

    def close_script(self):
        """
        Close the data acquisition script process if it is running.
        """
        if self.is_script_running():
            self.script_process.terminate()
