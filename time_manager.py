import datetime
import math
class TimeManager(object):
    JUMP = 0
    CONTINOUS = 1

    def __init__(self):
        self.analog_mode = self.JUMP

    def toggle_continuous_mode(self):
        if self.analog_mode == self.JUMP:
            self.analog_mode = self.CONTINOUS
        else:
            self.analog_mode = self.JUMP

    def get_time(self):
        current_time = datetime.datetime.now()
        hour = current_time.hour + (
        current_time.minute / 60 + current_time.second / 3600 if self.analog_mode == self.CONTINOUS else 0)
        minute = current_time.minute + (current_time.second / 60 if self.analog_mode == self.CONTINOUS else 0)
        second = current_time.second + (current_time.microsecond / 1000000 if self.analog_mode == self.CONTINOUS else 0)
        return hour, minute, second

    def get_arm_rotations_for_clock(self):
        hour, minute, second = self.get_time()
        hour_prog = hour % 12 / 6
        minute_prog = minute / 30
        second_prog = second / 30
        hour_deg = hour_prog * math.pi
        minute_deg = minute_prog * math.pi
        second_deg = second_prog * math.pi
        return hour_deg, minute_deg, second_deg

    def __repr__(self):
        return datetime.datetime.now().strftime("%H : %M : %S")

    def __str__(self):
        return datetime.datetime.now().strftime("%H : %M : %S")