import socket
import calci
class server:
	def Main(self):
		host = '127.0.0.1'
		port = 5001

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((host,port))
		sock.listen(1)
		conn,addr = sock.accept()
		print ("Connection from: " + str(addr))
		while True:
			data = conn.recv(1024).decode()
			if not data:
				break
			ans = calci.Infix(data)
			print("from client"+str(data))
			conn.send(ans.encode())
		conn.close()


if __name__ == '__main__':
	obj=server()
	obj.Main()
