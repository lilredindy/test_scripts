import requests



for i in range(0, 0):
	r = requests.get("http://www.theguardian.com/environment/2015/jul/07/zimbabwe-activists-deplore-sale-of-24-elephant-calves-to-china#comment-55235133")
	print r.status_code


import socket
print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1])