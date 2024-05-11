import subprocess
import os
import signal

class ExeManager:
    def __init__(self):
        self.path_script = "Data-Acquisition/prova.exe"
        self.path_sensecom = "C:/Program Files/SenseCom/SenseCom.exe"
        self.sensecom_process = None
        self.script_process = None

    def run_sensecom(self):
        self.sensecom_process = subprocess.Popen([self.path_sensecom], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    def run_script(self, path_to_csv, total_time):
        self.script_process = subprocess.Popen([self.path_script, path_to_csv, str(total_time)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        
    def get_sensecom_process_pid(self):
        return self.sensecom_process.pid
    
    def get_script_process_pid(self):
        return self.script_process.pid

    def is_sensecom_running(self):
        if self.sensecom_process is None:
            return False
        return self.sensecom_process.poll() is None

    def is_script_running(self):
        if self.script_process is None:
            return False
        return self.script_process.poll() is None

    def close_sensecom(self):
        # subprocess.run(["killall", self.path_sensecom])
        
        if self.is_sensecom_running():
            os.killpg(os.getpgid(self.get_sensecom_process_pid()), signal.SIGTERM)

    def close_script(self):
        # subprocess.run(["killall", self.path_script])
        
        if self.is_script_running():
            os.killpg(os.getpgid(self.get_script_process_pid()), signal.SIGTERM)
