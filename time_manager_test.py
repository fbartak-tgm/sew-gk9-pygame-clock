import unittest

import math

from time_manager.time_manager import TimeManager
import time,datetime
class TestTimeManager(unittest.TestCase):
    def setUp(self):
        self.time_manager = TimeManager()
    def test_string_representation(self):
        self.assertEqual(datetime.datetime.now().strftime("%H : %M : %S"),self.time_manager.__str__())
    def test_time_passes(self):
        before = self.time_manager.get_time()
        time.sleep(2)
        after = self.time_manager.get_time()
        self.assertNotEqual(before,after)
    # Do not run this test at midnight :)
    def test_time_passing_rate(self):
        start = self.time_manager.get_time()
        time.sleep(2)
        end = self.time_manager.get_time()
        self.assertEqual(2,end[0]*3600+end[1]*60+end[2]-(start[0]*3600+start[1]*60+start[2]))
    def test_pointer_rotations(self):
        pointer_rotations = self.time_manager.get_arm_rotations_for_clock()
        self.assertGreaterEqual(math.pi * 2,pointer_rotations[0])
        self.assertGreaterEqual(math.pi * 2,pointer_rotations[1])
        self.assertGreaterEqual(math.pi * 2,pointer_rotations[2])
        self.assertLessEqual(0,pointer_rotations[0])
        self.assertLessEqual(0,pointer_rotations[0])
        self.assertLessEqual(0,pointer_rotations[0])
    def test_pointer_rotations_change(self):
        pointer_rotations = self.time_manager.get_arm_rotations_for_clock()
        time.sleep(1)
        pointer_rotations_end = self.time_manager.get_arm_rotations_for_clock()
        self.assertNotEqual(pointer_rotations,pointer_rotations_end)
    def test_pointer_rotations_change_continuos(self):
        self.time_manager.toggle_continuous_mode()
        pointer_rotations = self.time_manager.get_arm_rotations_for_clock()
        time.sleep(0.01)
        pointer_rotations_end = self.time_manager.get_arm_rotations_for_clock()
        self.assertNotEqual(pointer_rotations,pointer_rotations_end)
    def test_continuous_mode(self):
        self.time_manager.toggle_continuous_mode()
        start = self.time_manager.get_time()
        time.sleep(0.2)
        end  = self.time_manager.get_time()
        self.assertNotEqual(start[0],int(start[0]))
        self.assertNotEqual(start[1],int(start[1]))
        self.assertNotEqual(start[2],int(start[2]))
        self.assertNotEqual(end[0],int(end[0]))
        self.assertNotEqual(end[1],int(end[1]))
        self.assertNotEqual(end[2],int(end[2]))


if __name__ == "__main__":
    unittest.main()