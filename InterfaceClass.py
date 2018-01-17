import socket
import threading
import sys

class Client:

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		

	def __init__(self, addr):
		try:
			self.sock.connect((addr, 5000))
			print("Connected to the server!")
			print("Press 'q' to quit.")
			iThread = threading.Thread()
			iThread.daemon = True 
			iThread.start()
		except:
			print("No response from server!")

		while True:
			inp = input("Enter Message: ")
			self.sock.send(str.encode(inp))
			data = self.sock.recv(1024).decode('utf-8')
			if not data:
				break 
			print("From Server: " + data)
			if inp == 'q':
				break

if __name__ == '__main__':
	client = Client(sys.argv[1])