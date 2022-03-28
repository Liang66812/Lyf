import numpy as np

def rotateArr(arr):
	lens = len(arr)
	# 打印二维数组对角线右上半部分
	i = lens - 1
	while i > 0:
		row = 0
		col = i
		while col < lens:
			print("%d".center(8) % arr[row][col], end="")
			row += 1
			col += 1
		print("\n")
		i -= 1
	# 打印二维数组对角先左下半部分(包括对角线)
	i = 0
	while i < lens:
		row = i
		col = 0
		while row < lens:
			print("%d".center(8) % arr[row][col], end="")
			row += 1
			col += 1
		print("\n")
		i += 1


if __name__ == "__main__":
	arr = [[1, 2, 3, 4], [4, 5, 6, 9], [7, 8, 9,10]]
	print(np.array(arr))
	rotateArr(arr)