class DurationTime:
    def __init__(self):
        self.time_sec = 0
        self.time_min = 0

    def set_time_min(self, minutes=None):
        if minutes == None:
            minutes = -1
        elif not isinstance(minutes, int) or minutes < 0:
            raise ValueError("Invalid format for minutes. Must be a non-negative integer.")
        self.time_min = minutes
        self._convert_time_to_seconds()

    def get_time_sec(self):
        return self.time_sec

    def is_time_over(self, current_time):
        return current_time <= self.time_sec

    def _convert_time_to_seconds(self):
        self.time_sec = self.time_min * 60
