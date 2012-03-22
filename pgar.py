import sys
import hashlib

MIN_ARGS = 2

def main():
	if len(sys.argv) < MIN_ARGS:
		print 'Missing Arguments'
		exit(1)
	apple = sys.argv[1]
	juice = sys.argv[2]
	print apple + juice

if __name__ == '__main__':
	main()
