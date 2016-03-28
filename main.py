import serial

SERIAL_PORT = "/dev/ttyUSB0"
ser = serial.Serial(SERIAL_PORT)

while(True):
	line = ser.readline()
	print line, "x"
	

