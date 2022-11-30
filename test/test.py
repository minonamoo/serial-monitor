import serial

PORT_NAME = 'COM10' # ??

with serial.Serial(PORT_NAME) as ser:
	while True:
		b = ser.read(1)
		if b'\n' == b:
			print()
		elif b'\r' == b:
			continue
		else:
			print(b.hex(), b.decode('ascii'), end=' ')