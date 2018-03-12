class SegTable:
	def __init__ (self):
		self.size = 512
		self.elements = [0 for i in range(self.size)] #creates a block has 512 elements
	
	def __iter__(self):
		for i in range(self.size):
			yield self.elements[i]

	def __getitem__(self,arg):
		return self.elements[arg]

	def __setitem__(self,key,item):
		self.elements[key] = item

	def inSize(self, index):
		return 1 if index<self.size else 0

	def getElement(self,index):
		if(self.inSize(index)):
			return self.elements[index]

	def setElement(self,index,value):
		if(self.inSize(index)):
			self.elements[index] = value
