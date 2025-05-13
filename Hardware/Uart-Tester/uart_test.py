import serial
import time

# Adjust this with your correct serial port
serial_port = '/dev/cu.usbserial-0001'  # Replace with your port
baud_rate = 115200

with serial.Serial(serial_port, baud_rate, timeout=1) as ser:
    print("Listening to UART...")
    while True:
        line = ser.readline()  # Read a line
        if line:
            print(line.decode('utf-8').strip())  # Print the received line
