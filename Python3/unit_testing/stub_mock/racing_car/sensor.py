import random


class Sensor(object):
    """
    The reading if the pressure value from the sensor is simulated in this
    implementation. Because the focus of the exercise os on the other class.
    """

    _OFFSET = 16

    def sample_pressure(self):
        pressure_telemetry_value = self.sample_pressure()
        return Sensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def sample_actual_pressure():
        # placeholder implementatuin that simulate a real sensor in real
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value
