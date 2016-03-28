import serial

SERIAL_PORT = "/dev/ttyUSB0"
ser = serial.Serial(SERIAL_PORT)

while(True):
	print ser.readline()
	

