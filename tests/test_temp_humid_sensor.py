import unittest
from unittest.mock import patch
from sensors.dht22_sensor import read_dht22_sensor
from your_module import collect_sensor_data

class TestSensorDataCollection(unittest.TestCase):

    @patch('sensors.dht22_sensor.read_dht22_sensor')
    def test_collect_sensor_data(self, mock_read_sensor):
        # Mock the sensor reading
        mock_read_sensor.return_value = (25.0, 50.0)

        # Call the function
        result = collect_sensor_data()

        # Check if the DataFrame is updated correctly
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]['Temperature'], 25.0)
        self.assertEqual(result.iloc[0]['Humidity'], 50.0)

        # Add more tests for edge cases, like sensor read failures

if __name__ == '__main__':
    unittest.main()
