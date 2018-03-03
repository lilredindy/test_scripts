matrix1 = []
row = [0,0,0]
for i in range(3):
	print i
	matrix1.append(row)
print matrix1
matrix1[2][2] = 1
print matrix1


matrix2 = [[0,0,0],[0,0,0],[0,0,0]]
print matrix2
matrix2[0][2] = 1
print matrix2

#matrix = [[0 for _ in range(width)] for _ in range(height)].