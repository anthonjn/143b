from PageTable import *
from SegTable import *
from Page import *
def createPM():
	filePath = "input.txt"
	# fname = input("Enter File Name: ")
	# while(not FileCheck(filePath+fname)):
	# 	print("not valid path, enter in a valid one")
	# 	filePath = input("Enter path: ")
	# 	fname = input("Enter File Name: ")
	inputs = open(filePath,"r")
	count = 0
	for line in inputs:
		line = line.strip("\n").split()
		if (not count):
			print("! count",count)
			for i in range(0,len(line),2):
					print(line[i] + " " + line[i+1])
			count=1
		else:
			print("else statement")
			for i in range(0,len(line),3):
				print(line[i] + " " + line[i+1] + " " +line[i+2])


if __name__ == '__main__' :
	#createPM()
	physicalAddr = [None]*1024 #524,288 integers in the array, 1024*512, each element holds 512 other elements
	bitmap = [0 for i in range(1024)]
	segmentTable = SegTable()

	physicalAddr[0] = segmentTable #this sets it up for us. 
	physicalAddr[1] = PageTable()
	physicalAddr[2] = PageTable()
	physicalAddr[3] = Page()


	#int divide(i think 512 too) to get the frame #. mod by 512 to get the addr within the frame.
	#mod by 512 to get to the next frame within physical addr. then you add another num to get to the right addr w/in PageTable

	#EXAMPLE OF HOW IT'S SUPPOSED TO WORK: 
	# physicalAddr[0] = segmentTable #this sets it up for us. 
	# physicalAddr[0][0] = 512	
	# physicalAddr[1] = PageTable()
	# physicalAddr[2] = PageTable()
	# physicalAddr[1][0] = 1536
	# physicalAddr[3] = Page()
	# physicalAddr[3][0] = 1000

	# print(physicalAddr[0][0])

	# print(physicalAddr[0][0]%512) #gives the correct addr within the frame
	# print(physicalAddr[physicalAddr[0][0]//512])	#gives the correct frame

	#WANT TO // FIRST THEN %

	# print(physicalAddr[physicalAddr[0][0]//512][physicalAddr[0][0]%512])

	# print(physicalAddr[physicalAddr[physicalAddr[0][0]//512][physicalAddr[0][0]%512]//512][physicalAddr[physicalAddr[0][0]//512][physicalAddr[0][0]%512]%512])