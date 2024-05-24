class DurationTime:
    """
    Class to manage duration time in seconds.

    Attributes
    ----------
    time_sec : int 
        The duration time in seconds.
    time_min : int 
        The duration time in minutes.
    """
    def __init__(self):
        """
        Constructoe, initialize DurationTime with default values.
        """
        self.time_sec = 0
        self.time_min = 0

    def set_time_min(self, minutes=None):
        """
        Set the duration time in minutes.

        Parameters
        ----------
        minutes : int 
            The duration time in minutes, 
            it is an optional parametr by defaults it is set to None.
            If None, sets time_min and time_sec to -1.
        
        Raises
        -----
        ValueError
            If minutes is not a non-negative integer.
        """
        if minutes == None:
            self.time_min = -1
            self.time_sec = -1
        elif not isinstance(minutes, int) or minutes < 0:
            raise ValueError("Invalid format for minutes. \n"
                             "Must be a non-negative integer.")
        else:
            self.time_min = minutes
            self._convert_time_to_seconds()

    def get_time_sec(self):
        """
        Get the duration time in seconds.

        Returns
        -------
        int
            The duration time in seconds.
        """
        return self.time_sec

    def is_time_over(self, current_time):
        """
        Check if the given time has exceeded the duration time.

        Parameters
        ----------
        current_time : float 
            The current time in seconds.

        Returns
        -------
        bool
            True if the current time has not exceeded the duration time, False otherwise.
        """
        if self.time_sec == -1:
            return False
        return current_time <= self.time_sec

    def _convert_time_to_seconds(self):
        """
        Convert the duration time from minutes to seconds.
        """
        self.time_sec = self.time_min * 60
