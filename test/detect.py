import serial.tools.list_ports as list_ports

# print USB connections
def print_port_list() -> None:
	ports = list_ports.comports()
	print('--------+-------')
	print('Port\t|Info')
	print('--------+-------')
	for port in ports:
		print(f'{port.device}\t|{port.usb_info()}')
	if 0 < len(ports):
		print('--------+-------')

# Show table of current USB connections
if __name__ == "__main__":
    while True:
        print_port_list()
        print('Input "r" for refresh or "q" for quit')
        user_input = input(':')
        # quit
        if 'q' == user_input:
            break