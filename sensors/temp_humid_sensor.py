import pandas as pd
import time
import logging
from sensors.dht22_sensor import read_dht22_sensor

def collect_dht22_sensor_data(number_of_readings, sleep_time=30):
    """
    Collects data from the DHT22 sensor for a specified number of readings.

    Args:
        number_of_readings (int): Number of sensor readings to collect.
        sleep_time (int): Time in seconds to sleep after a successful reading.

    Returns:
        DataFrame: DataFrame with Timestamp, Temperature, and Humidity.

    Raises:
        sensor_reading_exceptions: Specific exceptions related to sensor reading.
    """
    data = []
    for _ in range(number_of_readings):
        try:
            temperature, humidity = read_dht22_sensor()
            if temperature is not None and humidity is not None:
                timestamp = pd.Timestamp.now()
                data.append({'Timestamp': timestamp, 'Temperature': temperature, 'Humidity': humidity})
                time.sleep(sleep_time)
        except sensor_reading_exceptions as e:  # Replace with specific exceptions
            logging.error(f"Error reading sensor: {e}")

    return pd.DataFrame(data, columns=['Timestamp', 'Temperature', 'Humidity'])

def save_sensor_data_to_csv(sensor_data, file_path):
    """
    Saves sensor data to a CSV file.

    Args:
        sensor_data (DataFrame): Data to save.
        file_path (str): Path to save the CSV file.
    """
    sensor_data.to_csv(file_path, index=False)

# Initialize Logging
logging.basicConfig(level=logging.INFO)

# Parameters
number_of_readings = 10  # Define or pass as a parameter
file_path = 'path_to_save/sensor_data.csv'  # Define or pass as a parameter

# Collect and Save Data
sensor_data = collect_dht22_sensor_data(number_of_readings)
save_sensor_data_to_csv(sensor_data, file_path)
