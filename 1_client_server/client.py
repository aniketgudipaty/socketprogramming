import socket
import threading
import sys

class Client:
	def __init__(self,host,port):
		self.sock = socket.socket()

		try:
			self.sock.connect((host, port))
		except:
			print("Could not connect to server!")
			if __name__ == '__main__':
				sys.exit()

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
				msg = self.sock.recv(1024).decode()
				print("Server:",msg)
			except:
				print("Error Occured! Could not send your message")
				break

			if msg == "Bye client!":
				self.sock.close()
				break

	def sender(self):
		while self.t1.is_alive():
			msg = input()
			try:
				self.sock.send(msg.encode())
			except:
				print("Error Occured! Could not send your message")
				break

			if msg == "Bye server!":
				self.sock.close()
				break

if __name__ == '__main__':
	host = input('Enter host: ')
	port = int(input("Enter port: "))

	c = Client(host,port)