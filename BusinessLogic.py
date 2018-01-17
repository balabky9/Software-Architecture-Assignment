import socket
import threading
import sys

class Server:

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	calculations = {}

	def __init__(self):
		self.sock.bind(('127.0.0.1', 5000))
		print("Server started!")
		self.sock.listen(1)

	def handler(self, con, addr):
		while True:
			data = con.recv(1024).decode('utf-8')
			host = str(addr[0]) + ':' + str(addr[1])
			print("Address:", host)
			if not data or data == 'q':
				print(host, 'disconnected.')
				final_answer = ""
				for i in self.calculations[host]:
					final_answer += i + '\n'
				break 
			try:
				answer = str(eval(data))
				if host not in self.calculations:
					self.calculations[host] = [data + ' = ' + answer]
				else:
					self.calculations[host] += [data + ' = ' + answer]
				con.send(str.encode(answer))
			except:
				con.send(str.encode("Exception!"))
		con.send(str.encode(final_answer))
		con.close()

	def run(self):
		while True:
			con, addr = self.sock.accept()
			print(str(addr[0]) + ':' + str(addr[1]), 'connected.')
			cThread = threading.Thread(target=self.handler, args=(con, addr))
			cThread.daemon = True 
			cThread.start()			

if __name__ == '__main__':
	server = Server()
	server.run()

