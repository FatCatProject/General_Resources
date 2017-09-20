from time import sleep

def ready():
	import socket
	from zeroconf import ServiceInfo
	from zeroconf import Zeroconf
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = socket.inet_aton(socket.gethostbyname(s.getsockname()[0]))
	s.close()
	port = 9998 
	info = ServiceInfo(type_="_FatCatBB._tcp.local.", name="_FatCatBB._tcp.local.", address=ip, port=port, properties={}, server=None)

	zeroconf = Zeroconf()
	zeroconf.register_service(info)

	print("\nPublishing service, press Ctrl-C to exit...\n")
	try:
		while True:
			sleep(0.1)
	except KeyboardInterrupt:
		pass
	finally:
		zeroconf.unregister_service(info)
		zeroconf.close()

ready()
