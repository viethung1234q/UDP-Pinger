import time
from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout on blocking socket operations
client_socket.settimeout(1.0)

server_addr = ('localhost', 12000)

for i in range(1, 11):
	start = time.time()

	# Converts a time expressed in seconds since the epoch to a string representing local time.
	message = 'Ping #' + str(i) + " " + time.ctime(start)
	try:
		client_socket.sendto(message.encode(), server_addr)
		print(message)

		# Receive data from the socket. 
		# The return value is a pair (bytes, address) where bytes is a bytes object 
		# representing the data received and address is the address of the socket sending the data.
		data, server = client_socket.recvfrom(1024)
		print(data.decode('utf8'))

		end = time.time()
		RTT = end - start
		print("RTT: " + str(RTT) + " seconds\n")

	except timeout:
		print("#" + str(i) + " Requested Time Out\n")