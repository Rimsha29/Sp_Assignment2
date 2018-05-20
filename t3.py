import sys 

def findMatrix(mylist,matrix):
	mylist = [int(i) for i in mylist] # converting mylist of str to int
	row = 0 
	l_c = 0
	while(row != 7):
		col = 0
		while(col != 7):
			if mylist[l_c] is matrix[row][col] and mylist[l_c + 1] is matrix[row][col+1] and mylist[l_c + 2] is matrix[row+1][col] and mylist[l_c + 3] is matrix[row+1][col+1]:
				print "Matrix found at (%d,%d)" %(row,col)
				return; 
			col = col + 1
		row = row + 1
	print "Matrix not found"
	return;
	

if __name__ == "__main__":
	matrix = [[1,2,3,4,5,6,7,8],
		[9,10,11,12,13,14,15,16],
	 	[17,18,19,20,21,22,23,24],
	 	[25,26,17,28,29,30,31,32],
	 	[33,34,35,36,37,38,39,40],
	 	[41,42,43,44,45,46,47,48],
		[49,50,51,52,53,54,55,56],
	 	[57,58,59,60,61,62,63,64]]
	
	if len(sys.argv[1:]) == 4 :	
		findMatrix(sys.argv[1:],matrix)
	else :
		print "Given matrix is not a 2x2 matrix"


