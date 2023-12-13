import pandas as pd
import time
import logging
from sensors.dht22_sensor import read_dht22_sensor

def collect_dht22_sensor_data(number_of_readings, sleep_time=30, log_level=logging.INFO):
    """
    Collects data from the DHT22 sensor for a specified number of readings.

    Args:
        number_of_readings (int): Number of sensor readings to collect.
        sleep_time (int): Time in seconds to sleep after a successful reading.
        log_level (int): Logging level.

    Returns:
        DataFrame: DataFrame with Timestamp, Temperature, and Humidity.

    Raises:
        ValueError: If number_of_readings or sleep_time is not a positive integer.
    """
    if not isinstance(number_of_readings, int) or number_of_readings <= 0:
        raise ValueError("number_of_readings must be a positive integer")
    if not isinstance(sleep_time, int) or sleep_time <= 0:
        raise ValueError("sleep_time must be a positive integer")

    logging.basicConfig(level=log_level)
    data = []
    consecutive_errors = 0
    max_consecutive_errors = 5  # Configurable

    for _ in range(number_of_readings):
        try:
            temperature, humidity = read_dht22_sensor()
            if temperature is not None and humidity is not None:
                timestamp = pd.Timestamp.now(tz='UTC')  # Timezone aware
                data.append({'Timestamp': timestamp, 'Temperature': temperature, 'Humidity': humidity})
                consecutive_errors = 0
                time.sleep(sleep_time)
            else:
                raise ValueError("Sensor returned None values")
        except Exception as e:  # Replace with specific exceptions from the sensor
            logging.error(f"Error reading sensor: {e}")
            consecutive_errors += 1
            if consecutive_errors >= max_consecutive_errors:
                logging.error("Maximum consecutive errors reached, skipping further readings")
                break

    return pd.DataFrame(data, columns=['Timestamp', 'Temperature', 'Humidity'])

def save_sensor_data_to_csv(sensor_data, file_path):
    """
    Saves sensor data to a CSV file.

    Args:
        sensor_data (DataFrame): Data to save.
        file_path (str): Path to save the CSV file.
    """
    sensor_data.to_csv(file_path, index=False)

# Usage example
number_of_readings = 10  # Define or pass as a parameter
file_path = 'path_to_save/sensor_data.csv'  # Define or pass as a parameter

sensor_data = collect_dht22_sensor_data(number_of_readings, log_level=logging.INFO)
save_sensor_data_to_csv(sensor_data, file_path)
