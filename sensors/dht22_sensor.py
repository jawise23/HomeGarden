import pandas as pd
import time
from sensors.dht22_sensor import read_dht22_sensor

# Initialize an empty DataFrame with appropriate columns
data_columns = ['Timestamp', 'Temperature', 'Humidity']
sensor_data = pd.DataFrame(columns=data_columns)

def collect_sensor_data():
    """
    Collects data from the DHT22 sensor and appends it to a global DataFrame.

    This function reads temperature and humidity from the DHT22 sensor. 
    Each reading is timestamped and appended to a global DataFrame named 'sensor_data'.

    Returns:
        DataFrame: A pandas DataFrame with columns for Timestamp, Temperature, and Humidity.
                   Each row corresponds to a sensor reading at a specific time.

    Note: 
        - The function uses a global variable 'sensor_data' for storing the readings.
        - If the sensor read fails, no data is appended to the DataFrame.
    """
    global sensor_data

    temperature, humidity = read_dht22_sensor()
    if temperature is not None and humidity is not None:
        # Get the current timestamp
        timestamp = pd.Timestamp.now()
        # Append the data to the DataFrame
        new_data = pd.DataFrame([[timestamp, temperature, humidity]], columns=data_columns)
        sensor_data = sensor_data.append(new_data, ignore_index=True)
    
    return sensor_data

# Example usage
while True:
    sensor_data = collect_sensor_data()
    time.sleep(30)  # Adjust the frequency of readings as needed

# Optionally, save the data to a CSV file
sensor_data.to_csv('path_to_save/sensor_data.csv', index=False)
