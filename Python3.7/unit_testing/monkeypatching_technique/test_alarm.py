import unittest

from unittest.mock import *
from alarm import Alarm


class AlarmTest(unittest.TestCase):

    def test_check_with_too_high_pressure(self):
        # all references in Alarm module to the Sensor class and get them to
        # replace with a test double and get reference to as test_sensor_class
        with patch('alarm.Sensor') as test_sensor_class:
            # create another test double
            test_sensor_instance = Mock()
            # respond to the method sample_pressure
            test_sensor_instance.sample_pressure.return_value = 22
            # we tell sensor class that is should return this test double when
            # it's constructor is called
            test_sensor_class.return_value = test_sensor_instance
            # when we call the Alarm constuctor, it will consctruct an instance
            # of test sense a class and that class will now how it gets a call
            # to the sample_pressure method
            alarm = Alarm()
            alarm.check()
            self.assertTrue(alarm.is_alarm_on)

    # the same as above by using decorator
    @patch("alarm.Sensor")
    def test_check_with_too_low_pressure(self, test_sensor_class):
        test_sensor_instance = Mock()
        test_sensor_instance.sample_pressure.return_value = 14
        test_sensor_class.return_value = test_sensor_instance

        alarm = Alarm()
        alarm.check()
        self.assertTrue(alarm.is_alarm_on)
