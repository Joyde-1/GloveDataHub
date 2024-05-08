import subprocess

class ExeManager:
    def __init__(self):
        self.path_script = "C:/Users/Alfredo/Desktop/test_gloves/build/Debug/prova.exe"
        self.path_sensecom = "C:/Program Files/SenseCom/SenseCom.exe"
        self.sensecom_process = None
        self.script_process = None

    def run_sensecom(self):
        self.sensecom_process = subprocess.Popen([self.path_sensecom], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    def run_script(self, path_to_csv, total_time):
        self.script_process = subprocess.Popen([self.path_script, path_to_csv, str(total_time)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)

    def is_sensecom_running(self):
        return self.sensecom_process.poll() is None

    def is_script_running(self):
        return self.script_process.poll() is None

    def close_sensecom(self):
        subprocess.run(["killall", self.path_sensecom])

    def close_script(self):
        subprocess.run(["killall", self.path_script])
