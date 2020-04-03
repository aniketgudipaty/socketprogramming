import socket
import threading

class Server:

	def __init__(self,port):
		self.host = ''
		self.port = port
		self.sock = socket.socket()
		self.sock.bind((self.host, self.port))
		self.sock.listen(5)

		self.c , addr = self.sock.accept()

		print("Connection from:",addr[0],addr[1])

		self.t1 = threading.Thread(target = self.reciever)
		self.t2 = threading.Thread(target = self.sender)

		self.t1.start()
		self.t1.join()
		self.t2.join()

		self.sock.close()

	def reciever(self):
		self.t2.start()

		while self.t2.is_alive():
			try:
				msg = self.c.recv(1024).decode()
				print("Client:",msg)
			except:
				print("Error Occured! Could not send your message")
				break

			if msg == "Bye server!":
				self.c.close()
				break

	def sender(self):
		while self.t1.is_alive():
			msg = input()
			try:
				self.c.send(msg.encode())
			except:
				print("Error Occured!Could not send your message")
				break

			if msg == "Bye client!":
				self.c.close()
				break

if __name__ == '__main__':
	port = int(input("Enter port to be used: "))
	serv = Server(port)