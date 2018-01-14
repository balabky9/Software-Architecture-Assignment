import socket
class client:
	def Main(self,port):
		host = "127.0.0.1"
		#port = 5001
		sock=socket.socket()
		sock.connect((host,port))

		msg = input("Enter expression -> ")
		while msg!="q":
			sock.send(msg.encode())
			data = sock.recv(4096).decode()
			print("Calculated answer is: "+data)
			msg = input("Enter expression -> ")

		sock.close()

if __name__ == '__main__':
	port = input("Port :")
	obj=client()
	obj.Main(int(port))
