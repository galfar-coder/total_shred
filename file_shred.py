import os
import sys
import platform

def shredder():
	session = True
	while session == True:
		try:
			print("Permanent File Shredder")
			userInput = input("File Name or Exit: ")
			if userInput == "Exit" or userInput == "exit":
				session = False
				print("Session terminated")
			else:
				print("test")
				shred_obj = open(userInput, "rb+")
				size = os.stat(userInput)[6] 
				garbage = os.urandom(size)
				shred_obj.write(garbage)
				shred_obj.close()
				overwrite = open(userInput,"w")
				overwrite.close()
				os.remove(userInput)
				print("The author is not responsible for any unintended side effects of using the paranoid deletion option")
				paranoid = input("Paranoid deletion Y/N: ")
				if paranoid == "Y":
					if platform.system() == "Windows":
						os.system("cipher /w:C:")
					elif platform.system() == "Linux":
						os.system("cat /dev/urandom > all.file")
						os.system("shred -vunz all.file")
					else:
						pass
				else:
					pass
				print("{} has been derezzed".format(userInput))
		except Exception as e:
			print(e)
	
def main():
	shredder()
	
if __name__ == "__main__":
    main()
