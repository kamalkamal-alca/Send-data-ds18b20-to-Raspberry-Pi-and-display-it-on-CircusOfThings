import requests
import json
import time
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()

KEY_C = "........"  # Temp in Celsius
KEY_F = "........"  # Temp in Fahrenheit
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

def write_signal(key, value):
    """Write a single signal to Circus of Things"""
    payload = {
        'Key': key,
        'Value': value,
        'Token': TOKEN
    }
    
    response = requests.put(
        'https://circusofthings.com/WriteValue',
        json=payload,  # Use json parameter instead of data=json.dumps()
        headers={'Content-Type': 'application/json'}
    )
    return response

def read_signal(key):
    """Read a single signal from Circus of Things"""
    payload = {
        'Key': key,
        'Token': TOKEN
    }
    
    response = requests.get(
        'https://circusofthings.com/ReadValue',
        json=payload,  # Use json parameter
        headers={'Content-Type': 'application/json'}
    )
    return response

while True:
    try:
        temp_c = sensor.get_temperature()
        temp_c_rounded = round(temp_c, 1)  # Keep some decimal precision
        temp_f = round(temp_c * 1.8 + 32, 1)
        
        print(f"The temperature: {temp_c_rounded} *C / {temp_f} *F")

        # Send values separately (more reliable)
        response_c = write_signal(KEY_C, temp_c_rounded)
        if response_c.status_code == 200:
            print("Celsius temperature sent successfully!")
        else:
            print(f"Write Error C {response_c.status_code}: {response_c.text}")

        response_f = write_signal(KEY_F, temp_f)
        if response_f.status_code == 200:
            print("Fahrenheit temperature sent successfully!")
        else:
            print(f"Write Error F {response_f.status_code}: {response_f.text}")

        # Read back to verify
        read_response = read_signal(KEY_C)
        if read_response.status_code == 200:
            data = read_response.json()
            print(f"Verified C value on server: {data['Value']}")
        else:
            print(f"Read Error {read_response.status_code}: {read_response.text}")

    except Exception as e:
        print(f"Sensor/API Error: {e}")

    time.sleep(4)
