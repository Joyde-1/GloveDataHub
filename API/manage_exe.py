import subprocess

class ManageExe:
    def __init__(self):
        self.path_script = "/path/to/script"
        self.path_sensecom = "/path/to/sensecom"

    def run_sensecom(self):
        subprocess.run([self.path_sensecom])

    def run_script(self):
        subprocess.run([self.path_script])

    def close_sensecom(self):
        subprocess.run(["killall", self.path_sensecom])

    def close_script(self):
        subprocess.run(["killall", self.path_script])
