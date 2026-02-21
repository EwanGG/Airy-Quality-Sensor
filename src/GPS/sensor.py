import serial
import pynmea2

def get_gps_data():
    port = '/dev/ttyUSB0'
    ser = serial.Serial(port, baudrate=9600, timeout=1)

    while True:
        data = ser.readline().decode('ascii', errors='replace')
        if data.startswith('GPS'):
            msg = pynmea2.parse(data)
            return msg.latitude, msg.longitude

