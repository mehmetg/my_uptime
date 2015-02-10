from datetime import timedelta
import platform

#
#

def main():
	system = platform.system() 
	print("System in use is %s" % system)
	if system == 'Linux':
		with open('/proc/uptime', 'r') as f:
		    uptime_seconds = float(f.readline().split()[0])
		    uptime_string = str(timedelta(seconds = uptime_seconds))
		    print("Testing the webhook again! Will it work? Sunny days ahead.")
		print(uptime_string)

if __name__ == '__main__':
	main()