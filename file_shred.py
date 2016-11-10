import os
import sys
import platform

def shredder():
	print("Permanent File Shredder")
	userInput = input("File Name: ")
	shred_obj = open(userInput, "rb+")
	#os.path.getsize(input) 
	size = os.stat(userInput)[6] 
	garbage = os.urandom(size)
	shred_obj.write(garbage)
	shred_obj.close()
	overwrite = open(userInput,"w")
	overwrite.close()
	os.remove(userInput)
	if platform.system() == "Windows":
		os.system("cipher /w:C:")
	elif platform.system() == "Linux":
		os.system("cat /dev/urandom > all.file")
		os.system("shred -vunz all.file")
	else:
		return False
	
def main():
	shredder()
	
if __name__ == "__main__":
    main()
