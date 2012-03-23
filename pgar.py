import sys
import hashlib

MIN_ARGS = 2
PASSWORD_SIZE = 10

def capitalizeHalf(string):
	return string[0:5].upper() + string[5:10]

def hashCut(string):
	return string[0:PASSWORD_SIZE]	

def hash(string):
	return hashlib.sha256(string).hexdigest()

def main():
	PASSWORD = hashlib.sha256() 
	if len(sys.argv) < MIN_ARGS:
		print 'Missing Arguments'
		exit(1)
	for arg in sys.argv:
		PASSWORD.update(hash(arg))
	PASSWORD = capitalizeHalf(hashCut(PASSWORD.hexdigest()))
	print "Password:" +  PASSWORD

if __name__ == '__main__':
	main()
