row_hash_table = [[0 for i in range(9)]for j in range(9)]
col_hash_table = [[0 for i in range(9)]for j in range(9)]
sudoku = [[0 for i in range(9)]for j in range(9)]
while True:
	for i in sudoku:
		for j in i:
			print(j,end=' ')
		print()
	print()
	row = int(input("enter row : "))
	col = int(input("enter col : "))
	value = int(input("enter value : "))
	if row_hash_table[row-1][value-1]==1:
		print("you lose")
		break
	else:
		row_hash_table[row-1][value-1]=1
	if col_hash_table[value-1][col-1]==1:
		print("you lose")
		break
	else:
		col_hash_table[value-1][col-1]=1
	sudoku[row-1][col-1]=value
	for i in sudoku:
		if 0 not in i:
			print("you win")
			break

