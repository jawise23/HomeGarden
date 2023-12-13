import pandas as pd
import time
from sensors.dht22_sensor import read_dht22_sensor

def collect_sensor_data(sensor_data, sleep_time=30):
    """
    Collects data from the DHT22 sensor and returns the updated DataFrame.

    Args:
        sensor_data (DataFrame): The DataFrame to append new sensor data.
        sleep_time (int): The time in seconds to sleep after each reading.

    Returns:
        DataFrame: Updated DataFrame with new sensor readings.

    Note:
        - If the sensor read fails, the failure is logged and no data is appended.
    """
    try:
        temperature, humidity = read_dht22_sensor()
        if temperature is not None and humidity is not None:
            timestamp = pd.Timestamp.now()
            sensor_data = sensor_data.append(
                {'Timestamp': timestamp, 'Temperature': temperature, 'Humidity': humidity},
                ignore_index=True
            )
    except Exception as e:
        print(f"Error reading sensor: {e}")

    time.sleep(sleep_time)
    return sensor_data

# Initialize DataFrame
data_columns = ['Timestamp', 'Temperature', 'Humidity']
sensor_data = pd.DataFrame(columns=data_columns)

# Collect data
for _ in range(number_of_readings):  # Replace with a suitable condition
    sensor_data = collect_sensor_data(sensor_data)

# Save to CSV
sensor_data.to_csv('path_to_save/sensor_data.csv', index=False)
