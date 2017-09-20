import socket
import sys
from time import sleep

from zeroconf import ServiceBrowser, ServiceStateChange, Zeroconf


def on_service_state_change(zeroconf, service_type, name, state_change):
	print("Service %s of type %s state changed: %s" % (name, service_type, state_change))

	if state_change is ServiceStateChange.Added:
		info = zeroconf.get_service_info(service_type, name)
		if info:
			print("  Address: %s:%d" % (socket.inet_ntoa(info.address), info.port))
			print("  Weight: %d, priority: %d" % (info.weight, info.priority))
			print("  Server: %s" % (info.server,))
			if info.properties:
				print("  Properties are:")
				for key, value in info.properties.items():
					print("    %s: %s" % (key, value))
			else:
				print("  No properties")
		else:
			print("  No info")
		print('\n')
	if state_change is ServiceStateChange.Removed:
		print('\n')

if __name__ == '__main__':

	zeroconf = Zeroconf()
	print("\nBrowsing services, press Ctrl-C to exit...\n")
	browser = ServiceBrowser(zeroconf, "_FatCatBB._tcp.local.", handlers=[on_service_state_change])

	try:
		while True:
			sleep(0.1)
	except KeyboardInterrupt:
		pass
	finally:
		zeroconf.close()
