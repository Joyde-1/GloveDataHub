#   Authors:
#   Giovanni Fanara
#   Alfredo Gioacchino MariaPio Vecchio
#
#   Date: 2024-05-30



import subprocess
import psutil
import os

class ExeManager:
    """
    Class to manage execution of external scripts and processes.

    Attributes
    ----------
    sensecom_psutil_process : subprocess.Popen (class attribute)
        The sensecom process opened outside the API.
    sensecom_subprocess_process : psutil.process (class attribute)
        The sensecom process opened inside the API.
    script_process : subprocess.Popen (class attribute)
        The process for the data acquisition script.
    path_script : str (istance attribute)
        The path to the script for data acquisition.
    path_sensecom : str (istance attribute)
        The path to the SenseCom executable.
    script_return_code : int (istance attribute)
        Return code of the script program.
    """
    
    sensecom_psutil_process = None
    sensecom_subprocess_process = None
    script_process = None
        
    def __init__(self):
        """
        Constructor, initialize ExeManager with default paths processes.
        """
        
        self.path_script = "Data-Acquisition/gloves_data_acquisition.exe"
        
        # Check if SenseCom application is saved in 'Program Files' or 'Program Files (x86)'
        self._check_sensecom_path()
        
        self.script_return_code = None
        
    def _check_sensecom_path(self):
        """
        Check and set the SenseCom path.
        """
        
        # SenseCom paths
        sensecom_primary_path = "C:/Program Files/SenseCom/SenseCom.exe"
        sensecom_fallback_path = "C:/Program Files (x86)/SenseCom/SenseCom.exe"
        
        # Check if the SenseCom primary path exists
        if os.path.exists(sensecom_primary_path):
            self.path_sensecom = sensecom_primary_path
        else:
            # If SenseCom primary path does not exist, set the SenseCom fallback path
            self.path_sensecom = sensecom_fallback_path

    def start_sensecom(self):
        """
        Start the SenseCom process.
        """
        
        ExeManager.sensecom_psutil_process = None
        
        ExeManager.sensecom_subprocess_process = subprocess.Popen([self.path_sensecom], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

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
        
        self.script_return_code = None
        
        ExeManager.script_process = subprocess.Popen([self.path_script, path_to_csv, str(total_time)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    def set_sensecom_process(self, sensecom_process):
        """
        Set SenseCom process opened outside the API.
        
        Parameters
        ----------
        sensecom_process : psutil.process 
            The sensecom process opened outside the API.
        """
        
        ExeManager.sensecom_psutil_process = sensecom_process

    def is_sensecom_running(self):
        """
        Check if the SenseCom process is running.

        Returns
        -------
        bool
            True if SenseCom process is running, False otherwise.
        """
        
        # Check if SenseCom process is opened inside or outside the API
        if ExeManager.sensecom_psutil_process:
            # psutil does not have a direct equivalent of poll(), so we use is_running() as a proxy
            return ExeManager.sensecom_psutil_process.is_running()
        
        if ExeManager.sensecom_subprocess_process:
            return ExeManager.sensecom_subprocess_process.poll() is None

        return False

    def is_script_running(self):
        """
        Check if the data acquisition script process is running.

        Returns
        -------
        bool 
            True if data acquisition script process is running, False otherwise.
        """
        
        if ExeManager.script_process:
            
            # Try to catch the return code of the script program
            self.script_return_code = ExeManager.script_process.poll()
            
            return self.script_return_code is None

        return False
    
    def get_script_return_code(self):
        """
        Return the return code of the script program.
        
        Returns
        -------
        int
            The return code of the script program.
        """
        
        return self.script_return_code

    def close_sensecom(self):
        """
        Close the SenseCom process if it is running.
        """
        
        # Check if SenseCom process is opened inside or outside the API
        if ExeManager.sensecom_psutil_process:
            self.sensecom_psutil_process.terminate()
            
        if ExeManager.sensecom_subprocess_process:
            self.sensecom_subprocess_process.terminate()

    def close_script(self):
        """
        Close the data acquisition script process if it is running.
        """
        
        if self.is_script_running():
            ExeManager.script_process.terminate()
