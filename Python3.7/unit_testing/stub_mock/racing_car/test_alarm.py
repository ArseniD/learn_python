import unittest

from unittest.mock import Mock
from alarm import Alarm
from sensor import Sensor


class AlarmTest(unittest.TestCase):

    def test_alarm_is_off_by_default(self):
        alarm = Alarm()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_low_presure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(10))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_high_presure_sounds_alarm(self):
        alarm = Alarm(sensor=TestSensor(22))
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)

    def test_check_normal_presure_doesnt_sound_alarm(self):
        alarm = Alarm(sensor=TestSensor(19))
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)

    def test_check_with_pressure_ok_with_mock_fw(self):
        test_sensor = Mock(Sensor)
        test_sensor.sample_pressure.return_value = 18
        alarm = Alarm(test_sensor)
        alarm.check()
        self.assertFalse(alarm.is_alarm_on)


# defind stub class for testing
class TestSensor:

    def __init__(self, pressure):
        self.pressure = pressure

    def sample_pressure(self):
        return self.pressure
