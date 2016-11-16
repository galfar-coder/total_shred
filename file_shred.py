import os
import sys
import platform

def shredder():
	print("Permanent File Shredder")
	userInput = input("File Name: ")
	shred_obj = open(userInput, "rb+")
	size = os.stat(userInput)[6] 
	garbage = os.urandom(size)
	shred_obj.write(garbage)
	shred_obj.close()
	overwrite = open(userInput,"w")
	overwrite.close()
	os.remove(userInput)
	paranoid = input("Paranoid deletion Y/N: ")
	if paranoid == "Y":
		if platform.system() == "Windows":
			os.system("cipher /w:C:")
		elif platform.system() == "Linux":
			os.system("cat /dev/urandom > all.file")
			os.system("shred -vunz all.file")
		else:
			return False
	else:
		pass
	print("{} has been derezzed".format(userInput))
	
def main():
	shredder()
	
if __name__ == "__main__":
    main()
