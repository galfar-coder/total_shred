import os, sys, platform

def shredder():
	print "Shredder v1"
	print "Please enter a valid file name"
	#error handling = not yet implemented
	input = raw_input("File Name: ")
	confirm = raw_input("Really shred %s? y/n", %(input))
		if confirm == 'y':
			pass
		elif confirm == 'n':
			sys.exit(0)
		else:
			return False
	shred_obj = open("%s","rb+", %(input))
	#os.path.getsize(input) 
	size = os.stat(input)[6] #"%s", %(input)
	grbg = os.urandom(size)
	shred_obj.write(grbg)
	shred_obj.close()
	overwrite = open("%s","w", %(input))
	overwrite.close()
	if platform.system() == "Windows":
		os.system("cipher /w:C:")
	#elif platform.system() == "Linux":
	#	overwrite empty space in partition from /dev/urandom
	else:
		return False
	os.remove(input)
	
def main():
	shredder()
	
if __name__ == '__main__':
    main()