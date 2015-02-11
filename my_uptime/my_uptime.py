from datetime import timedelta
import platform

#
#

def get_platform():
	return platform.system() 

def uptime():
	system = get_platform()
	if system == 'Linux':
		print("System in use is %s" % system)
		with open('/proc/uptime', 'r') as f:
		    uptime_seconds = float(f.readline().split()[0])
		    uptime_string = str(timedelta(seconds = uptime_seconds))
		print(uptime_string)
	else:
		print("%s is not supported!" %system)

def main():
	uptime()

if __name__ == '__main__':
	main()